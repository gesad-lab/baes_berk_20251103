import json
import pytest
from src.app import app  # Assuming the Flask app is in src/app.py
from src.models import Course  # Import the Course model for interaction
from flask import jsonify

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_course_with_valid_data_succeeds(client):
    """Test the creation of a new course with valid data."""
    # Arrange
    payload = {
        "name": "Introduction to Programming",
        "level": "Beginner"
    }

    # Act
    response = client.post('/api/v1/courses', json=payload)

    # Assert
    assert response.status_code == 201  # HTTP 201 Created
    response_data = json.loads(response.data)
    assert "message" in response_data
    assert response_data["message"] == "Course created successfully."
    assert "course" in response_data
    assert response_data["course"]["name"] == payload["name"]
    assert response_data["course"]["level"] == payload["level"]
    assert "id" in response_data["course"]  # Check for course ID

def test_get_all_courses_succeeds(client):
    """Test retrieval of all courses."""
    # Act
    response = client.get('/api/v1/courses')

    # Assert
    assert response.status_code == 200  # HTTP 200 OK
    response_data = json.loads(response.data)
    assert isinstance(response_data, list)  # Ensure response is a list
    for course in response_data:
        assert "id" in course
        assert "name" in course
        assert "level" in course
        assert isinstance(course["id"], int)  # ID should be an integer
        assert isinstance(course["name"], str)  # Name should be a string
        assert isinstance(course["level"], str)  # Level should be a string

# Add more tests as necessary to cover other edge cases and scenarios.