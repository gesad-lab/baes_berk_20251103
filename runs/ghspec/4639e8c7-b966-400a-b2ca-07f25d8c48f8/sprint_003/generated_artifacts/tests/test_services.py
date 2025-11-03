```python
import pytest
from flask import json
from src.app import create_app  # Assuming you have a Flask application factory

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_course_with_empty_name(client):
    """Test that creating a course with an empty name returns an error."""
    response = client.post('/courses', json={'name': ''})  # Assuming the endpoint exists
    assert response.status_code == 400  # Bad Request
    assert response.json == {"error": {"code": "E001", "message": "Course name cannot be empty."}}

def test_create_course_with_valid_data(client):
    """Test that creating a course with valid data succeeds."""
    response = client.post('/courses', json={'name': 'Mathematics 101'})
    assert response.status_code == 201  # Created
    assert response.json['name'] == 'Mathematics 101'

def test_get_course_by_id(client):
    """Test retrieving a course by its ID returns the correct data."""
    # First create a course to retrieve
    response = client.post('/courses', json={'name': 'Science 101'})
    course_id = response.json['id']  # Assume response includes the course ID
    
    # Now retrieve the course
    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200  # OK
    assert response.json['id'] == course_id
    assert response.json['name'] == 'Science 101'

def test_get_non_existent_course(client):
    """Test that requesting a non-existent course returns a 404 error."""
    response = client.get('/courses/999')  # Assuming 999 is a non-existent ID
    assert response.status_code == 404  # Not Found
    assert response.json == {"error": {"code": "E002", "message": "Course not found."}}
```