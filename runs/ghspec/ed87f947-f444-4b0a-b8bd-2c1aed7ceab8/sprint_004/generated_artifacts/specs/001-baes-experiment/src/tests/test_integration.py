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
    """Test enrolling a student in a course successfully."""
    # Create a test student and course (Replace with appropriate endpoint or method)
    student_id = 1  # Assuming student with ID 1 exists
    course_id = 1   # Assuming course with ID 1 exists
    
    response = client.post(f"/api/v1/students/{student_id}/courses", json={"courseId": course_id})
    
    assert response.status_code == 201
    assert "enrollmentId" in response.json()  # Assuming it returns enrollment details

def test_get_student_courses(client):
    """Test retrieving all courses for a student."""
    student_id = 1  # Assuming student with ID 1 exists
    
    response = client.get(f"/api/v1/students/{student_id}/courses")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of courses

def test_remove_student_from_course(client):
    """Test removing a student from a course successfully."""
    student_id = 1  # Assuming student with ID 1 exists
    course_id = 1   # Assuming the student is enrolled in course 1

    response = client.delete(f"/api/v1/students/{student_id}/courses/{course_id}")
    
    assert response.status_code == 204  # No content for successful deletion

def test_enroll_student_invalid_course(client):
    """Test enrolling a student with invalid course ID."""
    student_id = 1  # Assuming student with ID 1 exists
    invalid_course_id = 999  # Non-existent course ID
    
    response = client.post(f"/api/v1/students/{student_id}/courses", json={"courseId": invalid_course_id})
    
    assert response.status_code == 400  # Bad request for invalid enrollment
    assert response.json() == {"error": {"code": "E001", "message": "Invalid course ID"}}  # Replace with actual error response

def test_get_courses_for_non_existent_student(client):
    """Test retrieving courses for a non-existent student."""
    non_existent_student_id = 999  # Non-existent student ID
    
    response = client.get(f"/api/v1/students/{non_existent_student_id}/courses")
    
    assert response.status_code == 404  # Not found for non-existent student
    assert response.json() == {"error": {"code": "E002", "message": "Student not found"}}  # Replace with actual error response
```