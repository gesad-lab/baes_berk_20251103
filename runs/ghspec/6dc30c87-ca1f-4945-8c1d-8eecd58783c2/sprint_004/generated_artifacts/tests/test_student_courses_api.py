```python
import pytest
from fastapi.testclient import TestClient
from myapp.main import app  # Assuming that the FastAPI app is defined in myapp/main.py
from myapp.database import create_database_schema
from myapp.models import Course, Student  # Assuming these models are defined
from myapp.models import StudentCourses  # Import the StudentCourses model

# Create a TestClient for making requests to the FastAPI app
client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Fixture to set up the database schema on startup."""
    create_database_schema()  # Ensure the database schema is created before tests

@pytest.fixture
def create_sample_data():
    """Fixture to create sample data for testing."""
    # Create a test student and course
    student = Student(name="Test Student")
    course = Course(name="Test Course")
    
    # Assuming there's a method in your database/session to add data
    session = get_session()  # Get a DB session
    session.add(student)
    session.add(course)
    session.commit()  # Save the changes
    session.refresh(student)  # Reload the instance with the new ID
    session.refresh(course)
    
    yield student, course  # Yield them for use in tests

    # Clean-up data after tests
    session.delete(student)
    session.delete(course)
    session.commit()

def test_enroll_student(create_sample_data):
    student, course = create_sample_data
    response = client.post(f"/students/{student.id}/enroll", json={"course_id": course.id})

    assert response.status_code == 201  # Ensure the enrollment is successful
    assert response.json() == {"message": "Enrollment successful"}  # Check response message

def test_retrieve_courses_for_student(create_sample_data):
    student, course = create_sample_data
    # Enroll student in the course
    client.post(f"/students/{student.id}/enroll", json={"course_id": course.id})

    response = client.get(f"/students/{student.id}/courses")

    assert response.status_code == 200  # Ensure the retrieval is successful
    assert len(response.json()) == 1  # Check if the course list has one course
    assert response.json()[0]["course_id"] == course.id  # Ensure the correct course is included

def test_student_not_found():
    response = client.get("/students/999/courses")  # Non-existent student ID
    assert response.status_code == 404  # Ensure the correct error status for non-existent student
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}

def test_enroll_non_existent_course(create_sample_data):
    student, _ = create_sample_data
    response = client.post(f"/students/{student.id}/enroll", json={"course_id": 999})  # Non-existent course ID

    assert response.status_code == 404  # Ensure correct error status for non-existent course
    assert response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}
```