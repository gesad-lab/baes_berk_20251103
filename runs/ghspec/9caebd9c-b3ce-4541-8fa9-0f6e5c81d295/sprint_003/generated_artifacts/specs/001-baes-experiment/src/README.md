```python
import json
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from your_application import app, db, Course  # Adjust import based on your structure

# Reinitialize the Flask application and SQLAlchemy for testing
@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables
        yield client  # This will run the test

def test_create_course_success(test_client):
    """Test that a course can be created with valid data."""
    response = test_client.post('/courses', 
                                 data=json.dumps({'name': 'Mathematics', 'level': 'Beginner'}),
                                 content_type='application/json')
    assert response.status_code == 201  # HTTP 201 Created
    assert 'id' in response.get_json()  # Ensure the response contains course ID
    assert response.get_json()['message'] == 'Course created successfully.'

def test_create_course_missing_name(test_client):
    """Test that an error is returned when the course name is missing."""
    response = test_client.post('/courses',
                                 data=json.dumps({'level': 'Intermediate'}),
                                 content_type='application/json')
    assert response.status_code == 400  # HTTP 400 Bad Request
    assert response.get_json()['error']['code'] == 'E001'
    assert response.get_json()['error']['message'] == 'Name is required.'

def test_create_course_missing_level(test_client):
    """Test that an error is returned when the course level is missing."""
    response = test_client.post('/courses',
                                 data=json.dumps({'name': 'Science'}),
                                 content_type='application/json')
    assert response.status_code == 400  # HTTP 400 Bad Request
    assert response.get_json()['error']['code'] == 'E002'
    assert response.get_json()['error']['message'] == 'Level is required.'

def test_retrieve_course_details(test_client):
    """Test that course details can be retrieved successfully."""
    # First create a course to retrieve
    create_response = test_client.post('/courses', 
                                        data=json.dumps({'name': 'History', 'level': 'Advanced'}),
                                        content_type='application/json')
    course_id = create_response.get_json()['id']

    # Now retrieve that course
    response = test_client.get(f'/courses/{course_id}')
    assert response.status_code == 200  # HTTP 200 OK
    data = response.get_json()
    assert data['name'] == 'History'  # Validate course name
    assert data['level'] == 'Advanced'  # Validate course level

def test_retrieve_course_not_found(test_client):
    """Test retrieving a course that does not exist returns 404."""
    response = test_client.get('/courses/9999')  # Assuming 9999 doesn't exist
    assert response.status_code == 404  # HTTP 404 Not Found
    assert response.get_json()['error']['code'] == 'E003'
    assert response.get_json()['error']['message'] == 'Course not found.'
```