```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Main FastAPI application
from src.database import get_database  # Function to get the database
from src.models import EnrollmentCreate  # Assuming EnrollmentCreate is defined in src/models

client = TestClient(app)

# Integration tests for the enrollment service
@pytest.mark.integration
def test_enroll_student_in_course():
    """Test enrolling a student in a course successfully."""
    enrollment_data = {
        "student_id": 1,  # Assuming a student with ID 1 exists
        "course_id": 2    # Assuming a course with ID 2 exists
    }
    response = client.post("/enrollments", json=enrollment_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Student enrolled in course successfully."}

@pytest.mark.integration
def test_retrieve_courses_for_student():
    """Test retrieving courses for a specific student."""
    student_id = 1  # Assuming a student with ID 1 exists
    response = client.get(f"/students/{student_id}/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses
    for course in response.json():
        assert "name" in course
        assert "level" in course

@pytest.mark.integration
def test_enroll_student_missing_course_id():
    """Test error handling for missing course ID during enrollment."""
    enrollment_data = {
        "student_id": 1,  # Assuming a student with ID 1 exists
        # "course_id" is missing here
    }
    response = client.post("/enrollments", json=enrollment_data)
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Course ID is required."
        }
    }
```