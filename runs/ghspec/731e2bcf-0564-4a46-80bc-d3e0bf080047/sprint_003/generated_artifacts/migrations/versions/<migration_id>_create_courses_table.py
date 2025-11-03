```python
# File: tests/test_course_controller.py

import pytest
from flask import json
from src.app import create_app, db
from src.models.course import Course

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})

    with app.app_context():
        # Create the database and tables
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture for providing a test client for the application."""
    return app.test_client()

def test_retrieve_courses_empty(client):
    """Test retrieving courses when no courses exist in the database."""
    response = client.get('/courses')
    assert response.status_code == 200
    assert response.json == []  # Expecting an empty list

def test_create_course_valid(client):
    """Test creating a new course with valid inputs."""
    response = client.post('/courses', json={
        'name': 'Mathematics 101',
        'level': 'Beginner'
    })
    assert response.status_code == 201
    assert response.json['name'] == 'Mathematics 101'
    assert response.json['level'] == 'Beginner'

def test_create_course_empty_name(client):
    """Test creating a course with an empty name field."""
    response = client.post('/courses', json={
        'name': '',
        'level': 'Intermediate'
    })
    assert response.status_code == 400
    assert response.json == {
        "error": {
            "code": "E001",
            "message": "Name field is required."
        }
    }

def test_create_course_empty_level(client):
    """Test creating a course with an empty level field."""
    response = client.post('/courses', json={
        'name': 'Physics 101',
        'level': ''
    })
    assert response.status_code == 400
    assert response.json == {
        "error": {
            "code": "E002",
            "message": "Level field is required."
        }
    }

def test_retrieve_courses_populated(client):
    """Test retrieving courses when courses exist in the database."""
    # First create a course to populate the database
    client.post('/courses', json={
        'name': 'Chemistry 101',
        'level': 'Beginner'
    })
    
    response = client.get('/courses')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'Chemistry 101'
    assert response.json[0]['level'] == 'Beginner'
```