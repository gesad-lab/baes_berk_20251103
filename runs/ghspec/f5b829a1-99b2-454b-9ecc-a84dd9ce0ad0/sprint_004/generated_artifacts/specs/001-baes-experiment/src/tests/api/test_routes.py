```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app, get_db
from src.models import Base, Student, Course  # Ensure the Course model is imported
from src.services.enrollment_service import EnrollmentService  # Ensure the EnrollmentService is imported

# Setup the test database and client
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def test_client():
    """Fixture to provide a test client for the API."""
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup initial data for testing."""
    db = TestingSessionLocal()
    
    # Create test data
    student = Student(name="Test Student")
    course = Course(title="Test Course")
    db.add(student)
    db.add(course)
    db.commit()
    db.refresh(student)
    db.refresh(course)

    yield {"student_id": student.id, "course_id": course.id}

    # Cleanup logic if necessary
    db.close()

def test_enroll_student_success(test_client, setup_database):
    """Test enrolling a student into a course successfully."""
    student_id = setup_database["student_id"]
    course_id = setup_database["course_id"]
    
    response = test_client.post(f"/students/{student_id}/enroll", json={"course_id": course_id})
    assert response.status_code == 200
    assert response.json() == {"message": "Student enrolled successfully"}

def test_get_courses_for_student_success(test_client, setup_database):
    """Test retrieving courses for a student successfully."""
    student_id = setup_database["student_id"]
    
    # First enroll the student in a course
    course_id = setup_database["course_id"]
    test_client.post(f"/students/{student_id}/enroll", json={"course_id": course_id})

    response = test_client.get(f"/students/{student_id}/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1  # student should be enrolled in one course

def test_enroll_student_invalid_student(test_client):
    """Test error response when enrolling with a non-existent student ID."""
    response = test_client.post("/students/999/enroll", json={"course_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Student not found", "details": {}}}

def test_enroll_student_invalid_course(test_client, setup_database):
    """Test error response when enrolling into a non-existent course ID."""
    student_id = setup_database["student_id"]
    response = test_client.post(f"/students/{student_id}/enroll", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Course not found", "details": {}}}

def test_get_courses_for_nonexistent_student(test_client):
    """Test error response when retrieving courses for a non-existent student."""
    response = test_client.get("/students/999/courses")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Student not found", "details": {}}}
```