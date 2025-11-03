```python
import json
import pytest
from flask import Flask
from flask.testing import FlaskClient
from src.app import create_app
from src.models import db, Course  # Assuming the Course model is defined in models.py

@pytest.fixture
def client() -> FlaskClient:
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            # create database and add test data
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_create_course_success(client: FlaskClient):
    """Test creating a course with valid data."""
    response = client.post('/courses', json={
        'name': 'Mathematics',
        'level': 'Intermediate'
    })
    assert response.status_code == 201  # Expecting a Successful Creation
    data = response.get_json()
    assert data['name'] == 'Mathematics'
    assert data['level'] == 'Intermediate'

def test_create_course_empty_name(client: FlaskClient):
    """Test creating a course with an empty name."""
    response = client.post('/courses', json={
        'name': '',
        'level': 'Beginner'
    })
    assert response.status_code == 400  # Expecting Bad Request
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Assuming a specific error code for validation
    assert data['error']['message'] == 'Name is required'  # Expected error message

def test_create_course_empty_level(client: FlaskClient):
    """Test creating a course with an empty level."""
    response = client.post('/courses', json={
        'name': 'Physics',
        'level': ''
    })
    assert response.status_code == 400  # Expecting Bad Request
    data = response.get_json()
    assert data['error']['code'] == 'E002'  # Assuming a specific error code for validation
    assert data['error']['message'] == 'Level is required'  # Expected error message

def test_retrieve_courses(client: FlaskClient):
    """Test retrieving the list of courses."""
    # First create a course
    client.post('/courses', json={'name': 'Biology', 'level': 'Advanced'})
    
    response = client.get('/courses')
    assert response.status_code == 200  # Expecting OK
    data = response.get_json()
    assert isinstance(data, list)  # Ensure response is a list
    assert len(data) > 0  # Ensure there's at least one course
    assert all('name' in course for course in data)  # Ensure every course has a name
    assert all('level' in course for course in data)  # Ensure every course has a level
```