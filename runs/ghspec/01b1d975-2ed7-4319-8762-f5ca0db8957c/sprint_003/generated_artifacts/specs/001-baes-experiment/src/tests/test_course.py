```python
import pytest
from flask import json
from src.app import create_app  # Assuming there's a create_app function to initialize the Flask app
from src.models import db, Course  # Importing the database and Course model

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app({'TESTING': True})  # Configure the app for testing
    with app.app_context():
        db.create_all()  # Create the database tables
        yield app
        db.drop_all()  # Clean up after the tests

@pytest.fixture
def client(app):
    """Provide a test client for the app."""
    return app.test_client()

def test_create_course(client):
    """Test the course creation endpoint."""
    response = client.post('/courses', json={'name': 'Math 101', 'level': 'Beginner'})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['course']['name'] == 'Math 101'
    assert data['course']['level'] == 'Beginner'

def test_create_course_missing_name(client):
    """Test course creation with missing name."""
    response = client.post('/courses', json={'level': 'Beginner'})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'
    assert 'name' in data['error']['message']

def test_create_course_missing_level(client):
    """Test course creation with missing level."""
    response = client.post('/courses', json={'name': 'Math 101'})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'
    assert 'level' in data['error']['message']

def test_get_courses(client):
    """Test retrieving the list of courses."""
    client.post('/courses', json={'name': 'Math 101', 'level': 'Beginner'})
    response = client.get('/courses')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['courses']) == 1
    assert data['courses'][0]['name'] == 'Math 101'
    assert data['courses'][0]['level'] == 'Beginner'
```