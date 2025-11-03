```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in src/main.py
from src.db import init_db, shutdown_db  # Database management functions
from src.models import Course  # Assuming you have a Course model
from src.models import Student  # Assuming you have a Student model

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Set up the database for testing."""
    init_db()
    yield
    shutdown_db()

@pytest.fixture
def client():
    """Create a TestClient for the FastAPI application."""
    return TestClient(app)

def test_enroll_student_in_course(client):
    """Test enrolling a student in a valid course."""
    response = client.post("/enroll", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Enrollment successful"}

def test_retrieve_student_courses(client):
    """Test retrieving all courses for a specific student."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of courses

def test_enroll_student_with_invalid_course_id(client):
    """Test enrolling a student with an invalid course ID."""
    response = client.post("/enroll", json={"student_id": 1, "course_id": 999})  # 999 is an invalid ID
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid course ID"}}

def test_error_handling_for_unenrollment(client):
    """Test unenrollment when the student is not enrolled in the course."""
    response = client.delete("/unenroll", json={"student_id": 1, "course_id": 2})  # Assuming student is not enrolled in course 2
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not enrolled in the specified course"}}
```