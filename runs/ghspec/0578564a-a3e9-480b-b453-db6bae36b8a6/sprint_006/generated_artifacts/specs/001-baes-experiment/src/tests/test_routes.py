```python
# tests/test_routes.py

import json
import pytest
from src.app import app  # Assuming the Flask app is in src/app.py
from src.models import Course, Teacher  # Import the Teacher model for interaction
from flask import jsonify

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_teacher_with_valid_data_succeeds(client):
    """Test the creation of a new teacher with valid data."""
    # Arrange
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
    }
    response = client.post('/api/v1/teachers', json=payload)
    assert response.status_code == 201

def test_assign_teacher_to_course_succeeds(client):
    """Test assigning a teacher to a course successfully."""
    # Arrange
    # Create a course and a teacher first
    course_response = client.post('/api/v1/courses', json={'title': 'Math 101', 'description': 'Introductory Math'})
    teacher_response = client.post('/api/v1/teachers', json={'name': 'Jane Doe', 'email': 'jane.doe@example.com'})

    course_id = json.loads(course_response.data)['id']
    teacher_id = json.loads(teacher_response.data)['id']

    # Act
    payload = {'teacher_id': teacher_id}
    response = client.post(f'/api/v1/courses/{course_id}/assign_teacher', json=payload)

    # Assert
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'Teacher assigned successfully to course.'

def test_retrieve_course_details_with_teacher_succeeds(client):
    """Test retrieving course details including assigned teacher's information."""
    # Arrange
    course_response = client.post('/api/v1/courses', json={'title': 'Science 101', 'description': 'Introductory Science'})
    teacher_response = client.post('/api/v1/teachers', json={'name': 'Alice Smith', 'email': 'alice.smith@example.com'})

    course_id = json.loads(course_response.data)['id']
    teacher_id = json.loads(teacher_response.data)['id']

    # Assign teacher to course
    payload = {'teacher_id': teacher_id}
    client.post(f'/api/v1/courses/{course_id}/assign_teacher', json=payload)

    # Act
    response = client.get(f'/api/v1/courses/{course_id}')

    # Assert
    assert response.status_code == 200
    course_data = json.loads(response.data)
    assert course_data['title'] == 'Science 101'
    assert 'teacher' in course_data
    assert course_data['teacher']['name'] == 'Alice Smith'
    assert course_data['teacher']['email'] == 'alice.smith@example.com'

def test_assign_teacher_to_course_with_invalid_teacher(client):
    """Test assigning a course to a teacher with an invalid teacher ID."""
    # Arrange
    course_response = client.post('/api/v1/courses', json={'title': 'History 101', 'description': 'Introductory History'})
    course_id = json.loads(course_response.data)['id']

    # Act
    payload = {'teacher_id': 999}  # Assume 999 is an invalid teacher ID
    response = client.post(f'/api/v1/courses/{course_id}/assign_teacher', json=payload)

    # Assert
    assert response.status_code == 400
    assert json.loads(response.data) == {'error': {'code': 'E001', 'message': 'Valid teacher ID must be provided.'}}

def test_retrieve_nonexistent_course_details(client):
    """Test retrieving details for a non-existent course."""
    # Act
    response = client.get('/api/v1/courses/9999')  # Assume 9999 is an invalid course ID

    # Assert
    assert response.status_code == 404
    assert json.loads(response.data) == {'error': {'code': 'E002', 'message': 'Course not found.'}}
```