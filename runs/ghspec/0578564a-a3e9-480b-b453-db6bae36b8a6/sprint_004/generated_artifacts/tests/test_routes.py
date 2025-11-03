```python
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
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Course created successfully'}

def test_enroll_student_in_course_invalid_id(client):
    """Test enrolling a student in a course with an invalid course ID."""
    # Arrange
    payload = {
        "student_id": 1,  # Valid student ID
        "course_id": 9999  # Invalid course ID (assuming this ID does not exist)
    }
    # Act
    response = client.post('/api/v1/enroll', json=payload)
    # Assert
    assert response.status_code == 400  # Assume 400 Bad Request for invalid ID
    assert response.get_json() == {'error': {'code': 'E001', 'message': 'Invalid course ID provided'}}
```