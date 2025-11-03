# tests/test_student_course.py

import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is defined in src/main.py
from src.models.student import Student
from src.models.course import Course
from src.database import SessionLocal

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Setup the database with a student and courses for testing."""
    db = SessionLocal()
    
    # Create a student and a few courses
    student = Student(name="John Doe")
    course1 = Course(name="Mathematics", level="Intermediate")
    course2 = Course(name="History", level="Advanced")
    
    db.add(student)
    db.add(course1)
    db.add(course2)
    db.commit()
    
    # Associate courses with student
    student.courses.append(course1)
    student.courses.append(course2)
    db.commit()
    
    yield db  # Yield control back to the tests
    
    # Teardown - remove all added entries
    db.query(Student).delete()
    db.query(Course).delete()
    db.commit()
    db.close()

def test_retrieve_courses_by_student_existing(setup_database):
    """Test retrieving courses associated with an existing student."""
    student_id = setup_database.query(Student).first().id
    response = client.get(f"/students/{student_id}/courses")
    assert response.status_code == 200  # Expecting a successful retrieval
    assert isinstance(response.json(), list)  # Response should be a JSON array
    assert len(response.json()) == 2  # We associated 2 courses

def test_retrieve_courses_by_student_no_courses(setup_database):
    """Test retrieving courses for a student with no associated courses."""
    db = setup_database
    student_no_courses = Student(name="Jane Smith")
    db.add(student_no_courses)
    db.commit()

    response = client.get(f"/students/{student_no_courses.id}/courses")
    assert response.status_code == 200  # Expecting a successful retrieval
    assert response.json() == []  # No courses should be associated

def test_retrieve_courses_by_invalid_student(setup_database):
    """Test API behavior for requesting courses with an invalid student ID."""
    response = client.get("/students/999/courses")  # Assuming 999 is invalid
    assert response.status_code == 404  # Expecting a not found response
    assert response.json() == {"detail": "Student not found"}  # Check response body for error detail