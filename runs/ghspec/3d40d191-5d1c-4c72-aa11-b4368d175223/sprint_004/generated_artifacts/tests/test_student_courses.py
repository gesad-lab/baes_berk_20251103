import pytest
from fastapi.testclient import TestClient
from src.api import app  # Import your FastAPI app instance

@pytest.fixture()
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

def test_enroll_student(client):
    """Test enrolling a student in a course."""
    # Attempt to enroll a student in a course with valid IDs
    response = client.post("/students/1/courses", json={"course_id": 2})
    assert response.status_code == 201
    assert response.json()["message"] == "Enrollment successful"

def test_get_student_courses(client):
    """Test retrieving courses for a student."""
    # Fetch the courses for a student
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_enroll_student_missing_course(client):
    """Test enrolling a student without providing a course ID."""
    # Attempt to enroll a student without a course ID
    response = client.post("/students/1/courses", json={})
    assert response.status_code == 400
    assert response.json()["detail"] == "Course ID is required."