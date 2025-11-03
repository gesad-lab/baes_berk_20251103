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

def test_assign_teacher_to_course(client):
    """Test assigning a teacher to a course."""
    response = client.post('/courses/1/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 200
    assert response.json['message'] == 'Teacher assigned successfully.'

def test_assign_teacher_to_nonexistent_course(client):
    """Test assigning a teacher to a non-existent course."""
    response = client.post('/courses/999/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 400
    assert response.json['error']['message'] == 'Invalid course ID.'

def test_assign_teacher_with_invalid_teacher_id(client):
    """Test assigning a teacher with an invalid teacher ID."""
    response = client.post('/courses/1/assign-teacher', json={'teacher_id': 999})
    assert response.status_code == 400
    assert response.json['error']['message'] == 'Invalid teacher ID.'

def test_retrieve_course_details(client):
    """Test retrieving course details including assigned teacher."""
    response = client.get('/courses/1')
    assert response.status_code == 200
    assert 'teacher' in response.json
```