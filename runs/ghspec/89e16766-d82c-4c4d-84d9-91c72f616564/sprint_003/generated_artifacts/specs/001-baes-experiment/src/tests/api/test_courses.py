```python
import pytest
from flask import json
from app import create_app, db
from app.models import Course

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables for testing purposes
            yield client
            db.drop_all()  # Cleanup after tests

def test_create_course(test_client):
    # Test creating a course with valid data
    response = test_client.post('/courses', json={
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Course created successfully.'
    assert 'course_id' in response.json  # Ensure course_id is returned

def test_create_course_missing_fields(test_client):
    # Test course creation with missing fields
    response = test_client.post('/courses', json={
        'name': ''  # Missing level
    })
    assert response.status_code == 400  # Bad request due to validation failure
    assert response.json['error']['code'] == 'E001'
    assert response.json['error']['message'] == 'Missing required fields: level'

def test_get_course(test_client):
    # First create a course to ensure we have data to retrieve
    create_response = test_client.post('/courses', json={
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    })
    course_id = create_response.json['course_id']  # Get the created course ID

    # Now retrieve the created course
    response = test_client.get(f'/courses/{course_id}')  # Use the created course ID
    assert response.status_code == 200
    assert response.json['name'] == 'Introduction to Programming'
    assert response.json['level'] == 'Beginner'

def test_get_course_nonexistent(test_client):
    # Test retrieving a course that does not exist
    response = test_client.get('/courses/99999')  # Assuming this ID does not exist
    assert response.status_code == 404  # Not found error
    assert response.json['error']['code'] == 'E002'
    assert response.json['error']['message'] == 'Course not found.'
```