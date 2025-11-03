```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is instantiated in src/main.py
from src.models import Student, Course, StudentCourse  # Import relevant models for testing

client = TestClient(app)

@pytest.fixture(scope="module")
def create_student():
    # Setup: Create a student in the database for testing
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    yield response.json()
    # Teardown: Cleanup created student (add necessary deletion logic if applicable)

@pytest.fixture(scope="module")
def create_course():
    # Setup: Create a course in the database for testing
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    yield response.json()
    # Teardown: Cleanup created course (add necessary deletion logic if applicable)

def test_enroll_student(create_student, create_course):
    """Test enrolling a student in a course"""
    student_id = create_student["id"]
    course_id = create_course["id"]
    response = client.post(f"/students/{student_id}/enroll", json={"course_id": course_id})
    assert response.status_code == 200
    assert response.json()["enrolled_courses"][0]["course_id"] == course_id  # Verify the correct course is enrolled

def test_get_student_courses(create_student):
    """Test retrieving courses for a specific student"""
    student_id = create_student["id"]
    response = client.get(f"/students/{student_id}/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list

def test_remove_course_from_enrollment(create_student, create_course):
    """Test removing a course from a student's enrollment"""
    student_id = create_student["id"]
    course_id = create_course["id"]
    client.post(f"/students/{student_id}/enroll", json={"course_id": course_id})  # Enroll first before removal
    response = client.delete(f"/students/{student_id}/enroll/{course_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Course removed successfully"  # Confirm the course representation

def test_enroll_student_invalid_course(create_student):
    """Test error handling when enrolling in a non-existent course"""
    student_id = create_student["id"]
    response = client.post(f"/students/{student_id}/enroll", json={"course_id": -1})  # Assuming -1 is invalid
    assert response.status_code == 400  # Expecting a Bad Request response
    assert "error" in response.json()  # Confirm there's an error key in the response
    assert response.json()["error"]["code"] == "E001"  # Check for specific error code indicating invalid course
```