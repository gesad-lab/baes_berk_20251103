```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the main FastAPI application is in src/main.py
from src.models import EnrollmentCreate  # Importing EnrollmentCreate model

client = TestClient(app)

# Integration tests for the enrollment API endpoints
@pytest.mark.integration
def test_enroll_student_with_valid_data():
    """Test enrolling a student in a course with valid data."""
    response = client.post("/enroll", json={"student_id": 1, "course_id": 2})  # Replace with valid IDs
    assert response.status_code == 201  # Check for successful creation
    assert response.json() == {"message": "Student enrolled successfully."}  # Check response message

@pytest.mark.integration
def test_enroll_student_missing_course_id():
    """Test enrolling a student without course_id returns an error."""
    response = client.post("/enroll", json={"student_id": 1})  # Missing course_id
    assert response.status_code == 400  # Check for bad request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "The course_id is required."
        }
    }  # Check error message

@pytest.mark.integration
def test_enroll_student_missing_student_id():
    """Test enrolling a student without student_id returns an error."""
    response = client.post("/enroll", json={"course_id": 2})  # Missing student_id
    assert response.status_code == 400  # Check for bad request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "The student_id is required."
        }
    }  # Check error message

@pytest.mark.integration
def test_enroll_student_with_invalid_ids():
    """Test enrolling a student with invalid student_id or course_id."""
    response = client.post("/enroll", json={"student_id": "invalid", "course_id": 2})  # Invalid student_id
    assert response.status_code == 422  # Check for validation error

    response = client.post("/enroll", json={"student_id": 1, "course_id": "invalid"})  # Invalid course_id
    assert response.status_code == 422  # Check for validation error
```