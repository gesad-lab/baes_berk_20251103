```python
import pytest
from flask import json
from src.app import app  # Assuming the Flask app is initialized in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_course_with_valid_data(client):
    """Test the creation of a course with valid data."""
    response = client.post('/courses', data=json.dumps({
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }), content_type='application/json')
    
    assert response.status_code == 201  # Check course is created
    assert 'id' in response.get_json()  # The response should have an ID for the created course

def test_associate_course_to_student(client):
    """Test associating a course with a student."""
    response = client.post('/students/1/courses', data=json.dumps({
        'course_id': '1'
    }), content_type='application/json')
    
    assert response.status_code == 200  # Verify the operation was successful
    assert response.get_json()['message'] == 'Course associated successfully'  # Check success message

def test_remove_course_from_student(client):
    """Test removing a course from a student's enrollments."""
    response = client.delete('/students/1/courses/1')
    
    assert response.status_code == 200  # Check for successful removal
    assert response.get_json()['message'] == 'Course removed successfully'  # Check success message

def test_associate_course_to_nonexistent_student(client):
    """Test associating a course with a non-existent student."""
    response = client.post('/students/999/courses', data=json.dumps({
        'course_id': '1'
    }), content_type='application/json')
    
    assert response.status_code == 404  # Expecting not found error
    assert response.get_json()['error']['code'] == 'E404'  # Custom error code for not found
    assert response.get_json()['error']['message'] == 'Student not found'  # Check the error message

def test_remove_nonexistent_course_from_student(client):
    """Test removing a non-existent course from a student's enrollments."""
    response = client.delete('/students/1/courses/999')
    
    assert response.status_code == 404  # Expecting not found error
    assert response.get_json()['error']['code'] == 'E404'  # Custom error code for not found
    assert response.get_json()['error']['message'] == 'Course not found'  # Check the error message
```