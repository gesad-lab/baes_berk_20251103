```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py

@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

def test_enroll_student_in_course(client):
    """Test enrolling a student in a course with valid IDs."""
    response = client.post("/students/1/courses", json={"courseId": 1})
    assert response.status_code == 201
    assert response.json() == {"message": "Student enrolled successfully."}

def test_enroll_student_in_course_invalid_student(client):
    """Test enrolling a student with an invalid student ID."""
    response = client.post("/students/999/courses", json={"courseId": 1})  # Invalid student ID
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid student ID."}}

def test_enroll_student_in_course_invalid_course(client):
    """Test enrolling a student in an invalid course."""
    response = client.post("/students/1/courses", json={"courseId": 999})  # Invalid course ID
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid course ID."}}

def test_get_student_courses(client):
    """Test retrieving all courses for a specific student."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    # Assuming the student with ID 1 is enrolled in a course
    assert isinstance(response.json(), list)  # Response should be a list
    assert len(response.json()) >= 0  # Should return at least an empty array if no courses

def test_remove_student_from_course(client):
    """Test removing a student from a course successfully."""
    response = client.delete("/students/1/courses/1")
    assert response.status_code == 204  # No Content

def test_remove_student_from_course_invalid_student(client):
    """Test removing a student with an invalid student ID."""
    response = client.delete("/students/999/courses/1")  # Invalid student ID
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid student ID."}}

def test_remove_student_from_course_invalid_course(client):
    """Test removing a student from an invalid course."""
    response = client.delete("/students/1/courses/999")  # Invalid course ID
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid course ID."}}
```