# File: tests/test_api/test_performance.py

import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Importing the main FastAPI application

client = TestClient(app)

# Integration tests for the course update functionality
@pytest.mark.integration
def test_update_course_with_valid_teacher():
    """Test successfully updating a course with a valid teacher ID."""
    response = client.put("/courses/1", json={"teacher_id": 2})
    assert response.status_code == 200
    assert "course_details" in response.json()  # Adjust based on actual response structure

@pytest.mark.integration
def test_update_course_with_invalid_teacher():
    """Test error response when updating a course with a non-existent teacher ID."""
    response = client.put("/courses/1", json={"teacher_id": 9999})  # Assuming teacher_id 9999 does not exist
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Teacher ID does not exist"
        }
    }

@pytest.mark.integration
def test_retrieve_course_with_teacher():
    """Test successfully retrieving a course's details with the associated teacher."""
    response = client.get("/courses/1")  # Assume course ID 1 exists
    assert response.status_code == 200
    assert "teacher" in response.json()  # Ensure teacher info is included in the response

@pytest.mark.integration
def test_retrieve_non_existent_course():
    """Test error response when retrieving a non-existent course."""
    response = client.get("/courses/999")  # Assume course ID 999 does not exist
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E003",
            "message": "Course ID not found"
        }
    }