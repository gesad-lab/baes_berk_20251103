```python
import pytest
from flask import json
from src.routes import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_course_with_valid_data(client):
    """Test creating a new course with valid name and level."""
    response = client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    assert response.status_code == 201
    assert 'course' in response.json
    assert response.json['course']['name'] == 'Mathematics'
    assert response.json['course']['level'] == 'Beginner'

def test_retrieve_all_courses(client):
    """Test retrieving the list of all courses."""
    response = client.get('/courses')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check if the response is a list of courses
    # Additional checks could be included once you have pre-populated data

def test_create_course_without_name(client):
    """Test creating a course without providing a name."""
    response = client.post('/courses', json={'level': 'Intermediate'})
    assert response.status_code == 400  # Assuming 400 for bad request
    assert response.json['error']['code'] == 'E001'  # Example error code for missing name
    assert response.json['error']['message'] == 'Name is required'

def test_create_course_without_level(client):
    """Test creating a course without providing a level."""
    response = client.post('/courses', json={'name': 'Science'})
    assert response.status_code == 400  # Assuming 400 for bad request
    assert response.json['error']['code'] == 'E002'  # Example error code for missing level
    assert response.json['error']['message'] == 'Level is required'
```