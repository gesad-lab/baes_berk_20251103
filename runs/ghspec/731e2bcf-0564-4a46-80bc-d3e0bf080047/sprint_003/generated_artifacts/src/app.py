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

def test_create_course(client):
    """Test creating a course with valid inputs."""
    response = client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    assert response.status_code == 201
    assert b'Mathematics' in response.data

def test_create_course_missing_name(client):
    """Test creating a course without a name."""
    response = client.post('/courses', json={'level': 'Beginner'})
    assert response.status_code == 400
    assert b'Name field is required.' in response.data

def test_create_course_missing_level(client):
    """Test creating a course without a level."""
    response = client.post('/courses', json={'name': 'Mathematics'})
    assert response.status_code == 400
    assert b'Level field is required.' in response.data

def test_get_courses_empty(client):
    """Test retrieving courses when none exist."""
    response = client.get('/courses')
    assert response.status_code == 200
    assert json.loads(response.data) == []

def test_get_courses_with_existing_data(client):
    """Test retrieving courses when some exist."""
    client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    response = client.get('/courses')
    assert response.status_code == 200
    courses = json.loads(response.data)
    assert len(courses) == 1
    assert courses[0]['name'] == 'Mathematics'
    assert courses[0]['level'] == 'Beginner'
```