```python
import pytest
from flask import Flask, jsonify, request
from your_app import create_app, db  # make sure to replace with actual import paths
from your_app.models import Course  # update with actual model import

@pytest.fixture
def client():
    app = create_app('testing')  # use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create the database schema
        yield client
        with app.app_context():
            db.drop_all()  # clean up after tests

def test_create_course_success(client):
    """Test creating a course successfully."""
    response = client.post('/courses', json={
        'title': 'Introduction to Python',
        'description': 'A basic course on Python programming.'
    })
    assert response.status_code == 201  # Check if the course is created
    data = response.get_json()
    assert 'id' in data  # Check if an ID is returned
    assert data['title'] == 'Introduction to Python'
    assert data['description'] == 'A basic course on Python programming.'

def test_create_course_missing_title(client):
    """Test response for missing title when creating a course."""
    response = client.post('/courses', json={
        'description': 'A basic course on Python programming.'
    })
    assert response.status_code == 400  # Check for bad request
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Check for specific error code
    assert data['error']['message'] == 'Title is required.'  # Check error message

def test_get_course_by_id_success(client):
    """Test retrieving a course by ID successfully."""
    # First, create a course to retrieve
    create_response = client.post('/courses', json={
        'title': 'Introduction to Python',
        'description': 'A basic course on Python programming.'
    })
    course_id = create_response.get_json()['id']

    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200  # Check if the retrieval is successful
    data = response.get_json()
    assert data['id'] == course_id  # Check if the correct course is returned

def test_get_course_by_id_not_found(client):
    """Test response for requesting a non-existent course by ID."""
    response = client.get('/courses/999')  # Assuming 999 does not exist
    assert response.status_code == 404  # Check for not found
    data = response.get_json()
    assert data['error']['code'] == 'E002'  # Check for specific error code
    assert data['error']['message'] == 'Course not found.'  # Check error message
```