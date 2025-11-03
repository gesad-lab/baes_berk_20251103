---
File: tests/integration/test_course_api.py
```python
import pytest
from flask import json
from app import create_app, db  # Assuming create_app sets up the Flask app and db is the SQLAlchemy instance
from app.models import Course  # Import the Course model

@pytest.fixture
def client():
    app = create_app({'TESTING': True})  # Create a test instance of the application
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client

def test_create_course_with_valid_data(client):
    """Test successful creation of a course with valid data."""
    response = client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    assert response.status_code == 201
    assert 'id' in response.get_json()
    assert response.get_json()['name'] == 'Mathematics'
    assert response.get_json()['level'] == 'Beginner'

def test_create_course_with_missing_name(client):
    """Test response when creating a course with missing name."""
    response = client.post('/courses', json={'level': 'Beginner'})
    assert response.status_code == 400
    assert response.get_json() == {"error": {"code": "E001", "message": "Name and level are required."}}

def test_create_course_with_missing_level(client):
    """Test response when creating a course with missing level."""
    response = client.post('/courses', json={'name': 'Mathematics'})
    assert response.status_code == 400
    assert response.get_json() == {"error": {"code": "E001", "message": "Name and level are required."}}

def test_get_all_courses(client):
    """Test retrieval of all courses."""
    # First, add a course to retrieve
    client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    
    response = client.get('/courses')
    assert response.status_code == 200
    data = response.get_json()
    
    assert isinstance(data, list)  # Ensure it's a list
    assert len(data) == 1  # We should have one course
    assert data[0]['name'] == 'Mathematics'
    assert data[0]['level'] == 'Beginner'
```