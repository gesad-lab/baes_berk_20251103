```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import init_db, Base, SessionLocal
from src.models import Course, Student  # Assuming Course and Student models are defined in src/models.py
from src.api import app  # Assuming the FastAPI app is defined in src/api

# Define a database URL for SQLite
DATABASE_URL = "sqlite:///./test.db"

# Set up the FastAPI app and the test client
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Create the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def test_app():
    # Initialize the database and create a test client
    init_db()
    yield client
    # Clean up the database after tests are done
    Base.metadata.drop_all(bind=engine)

def test_get_student_courses_no_courses(test_app):
    """Test GET /students/{studentId}/courses when no courses are enrolled."""
    response = test_app.get("/students/1/courses")
    assert response.status_code == 200
    assert response.json() == []  # Expecting an empty list

def test_get_student_courses_invalid_id(test_app):
    """Test GET /students/{studentId}/courses with invalid student ID."""
    response = test_app.get("/students/999/courses")  # Assuming this ID does not exist
    assert response.status_code == 404  # Expecting a Not Found response

def test_post_enroll_student_in_course(test_app):
    """Test POST /students/{studentId}/courses to enroll a student in a course."""
    # First, we need to create a student and a course for testing
    student_response = test_app.post("/students", json={"name": "Test Student"})  # Initial API for creating the student
    assert student_response.status_code == 201
    student_id = student_response.json().get("id")

    course_response = test_app.post("/courses", json={"name": "Test Course"})  # Initial API for creating the course
    assert course_response.status_code == 201
    course_id = course_response.json().get("id")

    # Now we can enroll the student in the course
    enroll_response = test_app.post(f"/students/{student_id}/courses", json={"course_id": course_id})
    assert enroll_response.status_code == 201  # Expecting Created status

    # Check if the student can retrieve the list of enrolled courses
    courses_response = test_app.get(f"/students/{student_id}/courses")
    assert courses_response.status_code == 200
    assert len(courses_response.json()) == 1  # Expecting one course now

def test_post_enroll_student_invalid_course(test_app):
    """Test POST /students/{studentId}/courses with an invalid course ID."""
    student_response = test_app.post("/students", json={"name": "Student for Testing"})
    assert student_response.status_code == 201
    student_id = student_response.json().get("id")

    # Attempting to enroll the student in a non-existing course
    enroll_response = test_app.post(f"/students/{student_id}/courses", json={"course_id": 999})  # Invalid course ID
    assert enroll_response.status_code == 400  # Expecting a Bad Request status
```