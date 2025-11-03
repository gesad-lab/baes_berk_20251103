```python
# tests/test_course_integration.py

import pytest
from flask import json
from src.app import app
from src.models import Teacher, Course  # Assuming these are the models used for the courses and teachers

@pytest.fixture
def client():
    """Create a test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_assign_teacher_to_course(client):
    """Test assigning an existing teacher to a course."""
    response = client.patch('/courses/1/assign-teacher', data=json.dumps({
        'teacherId': 1
    }), content_type='application/json')
    
    assert response.status_code == 200
    assert response.json == {'message': 'Teacher has been assigned to the course.'}

def test_retrieve_course_details_with_teacher(client):
    """Test retrieving course details with assigned teacher information."""
    response = client.get('/courses/1')
    
    assert response.status_code == 200
    data = response.json
    assert data['courseId'] == 1
    assert 'teacher' in data
    assert data['teacher']['id'] == 1
    assert data['teacher']['name'] == 'John Doe'  # Assume this is the name of the teacher assigned

def test_handle_unassigned_course(client):
    """Test retrieving course details for a course with no assigned teacher."""
    response = client.get('/courses/2')  # Assuming course 2 has no teacher assigned
    
    assert response.status_code == 200
    data = response.json
    assert data['courseId'] == 2
    assert data['teacher'] is None  # Teacher should be None or equivalent

def test_error_on_assigning_non_existent_teacher(client):
    """Test error response when trying to assign a non-existent teacher to a course."""
    response = client.patch('/courses/1/assign-teacher', data=json.dumps({
        'teacherId': 999  # Assuming this ID does not exist
    }), content_type='application/json')
    
    assert response.status_code == 400
    assert response.json == {'error': {'code': 'E001', 'message': 'Teacher does not exist.'}}
```