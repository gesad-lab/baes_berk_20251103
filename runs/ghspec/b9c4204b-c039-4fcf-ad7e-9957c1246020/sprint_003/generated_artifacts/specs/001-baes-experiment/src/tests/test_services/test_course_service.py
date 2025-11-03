```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Main FastAPI application
from src.database import get_database  # Assuming there is a function to get the database

client = TestClient(app)

# Integration tests for the course API endpoints
@pytest.mark.integration
def test_retrieve_courses():
    """Test retrieving all courses returns the correct structure and data."""

    # Sending a request to retrieve all courses
    response = client.get("/courses")
    
    # Ensure the response status code is 200 OK
    assert response.status_code == 200

    # Parse the JSON response
    courses = response.json()

    # Validate the structure of the returned data
    assert isinstance(courses, list)  # Should be a list
    for course in courses:
        assert "name" in course  # Each course should have a name field
        assert "level" in course  # Each course should have a level field
        assert isinstance(course["name"], str)  # Name should be a string
        assert isinstance(course["level"], str)  # Level should be a string

@pytest.mark.integration
def test_create_course():
    """Test creating a new course returns the correct data structure."""

    course_data = {"name": "Mathematics", "level": "Beginner"}
    response = client.post("/courses", json=course_data)

    # Ensure the response status code is 201 Created
    assert response.status_code == 201

    # Parse the JSON response
    created_course = response.json()

    # Validate the response structure
    assert "name" in created_course
    assert "level" in created_course
    assert created_course["name"] == course_data["name"]
    assert created_course["level"] == course_data["level"]

@pytest.mark.integration
def test_create_course_missing_level():
    """Test creating a course without a level returns an error response."""

    course_data = {"name": "Science"}  # Missing 'level'
    response = client.post("/courses", json=course_data)

    # Ensure the response status code is 400 Bad Request
    assert response.status_code == 400

    # Parse the JSON response
    error_response = response.json()

    # Check if the error response contains relevant error information
    assert "error" in error_response
    assert error_response["error"]["code"] == "E002"  # Assume this is the error code for missing fields
    assert "message" in error_response["error"]
```