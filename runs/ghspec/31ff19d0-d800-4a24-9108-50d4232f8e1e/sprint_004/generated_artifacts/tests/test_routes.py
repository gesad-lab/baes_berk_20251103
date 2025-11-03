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

def test_enroll_student_in_existing_course(client):
    """Test enrolling a student in an existing course."""
    response = client.post('/students/1/courses', json={'courseId': 1})
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == 'Student enrolled successfully.'

def test_enroll_non_existing_student(client):
    """Test error handling when enrolling a non-existing student."""
    response = client.post('/students/999/courses', json={'courseId': 1})
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E404'
    assert response.json['error']['message'] == 'Student does not exist.'

def test_enroll_non_existing_course(client):
    """Test error handling when enrolling a student in a non-existing course."""
    response = client.post('/students/1/courses', json={'courseId': 999})
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E404'
    assert response.json['error']['message'] == 'Course does not exist.'

def test_retrieve_enrolled_courses_for_valid_student(client):
    """Test retrieving courses for a valid student."""
    response = client.get('/students/1/courses')
    assert response.status_code == 200
    assert isinstance(response.json['courses'], list)
    # Assuming student 1 is enrolled in some courses
    assert len(response.json['courses']) > 0
```