```python
import pytest
from flask import Flask, jsonify, request
from src.api import create_app
from src.models.course import Course, init_db  # Import the Course model and init_db method

@pytest.fixture
def app():
    # Set up the Flask app for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # Initialize DB
    with app.app_context():
        init_db()
    yield app

@pytest.fixture
def client(app):
    # Create a test client
    return app.test_client()

def test_create_course(client):
    """Test creating a new course with valid data."""
    response = client.post('/api/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Course created successfully'
    assert 'id' in data  # Ensure an ID is returned

def test_retrieve_courses(client):
    """Test retrieving the list of courses."""
    client.post('/api/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    response = client.get('/api/courses')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1  # Ensure one course is present
    assert data[0]['name'] == 'Mathematics'  # Check the course name
    assert data[0]['level'] == 'Beginner'  # Check the course level

def test_create_course_missing_name(client):
    """Test creating a course without a name."""
    response = client.post('/api/courses', json={'level': 'Beginner'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Ensure the correct error code is returned
    assert data['error']['message'] == 'Course name is required'  # Check the error message

def test_create_course_missing_level(client):
    """Test creating a course without a level."""
    response = client.post('/api/courses', json={'name': 'Mathematics'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error']['code'] == 'E002'  # Ensure the correct error code is returned
    assert data['error']['message'] == 'Course level is required'  # Check the error message
```