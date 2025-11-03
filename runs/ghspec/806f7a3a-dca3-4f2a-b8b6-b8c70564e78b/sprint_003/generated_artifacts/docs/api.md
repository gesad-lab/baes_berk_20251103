---
File: tests/test_course.py
```python
import pytest
from flask import json
from app import create_app, db
from models.course import Course

@pytest.fixture
def client():
    app = create_app('testing')  # Use a separate testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create fresh database for each test
        yield client
        with app.app_context():
            db.drop_all()  # Clean up database after tests

def test_create_course(client):
    """Test creating a course with valid input."""
    response = client.post('/api/v1/courses', 
                           data=json.dumps({'name': 'Mathematics', 'level': 'Beginner'}),
                           content_type='application/json')
    assert response.status_code == 201
    assert 'id' in response.json

def test_create_course_with_empty_name(client):
    """Test creating a course with an empty name field."""
    response = client.post('/api/v1/courses', 
                           data=json.dumps({'name': '', 'level': 'Beginner'}),
                           content_type='application/json')
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E001'

def test_create_course_with_empty_level(client):
    """Test creating a course with an empty level field."""
    response = client.post('/api/v1/courses', 
                           data=json.dumps({'name': 'Science', 'level': ''}),
                           content_type='application/json')
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E001'

def test_get_course_by_id(client):
    """Test retrieving a course by its ID."""
    create_response = client.post('/api/v1/courses', 
                                   data=json.dumps({'name': 'History', 'level': 'Intermediate'}),
                                   content_type='application/json')
    
    course_id = create_response.json['id']
    
    response = client.get(f'/api/v1/courses/{course_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'History'
    assert response.json['level'] == 'Intermediate'

def test_get_non_existent_course(client):
    """Test retrieving a course that does not exist."""
    response = client.get('/api/v1/courses/99999')  # arbitrary non-existent ID
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E002'

def test_update_course(client):
    """Test updating an existing course."""
    create_response = client.post('/api/v1/courses', 
                                   data=json.dumps({'name': 'Geography', 'level': 'Advanced'}),
                                   content_type='application/json')
    
    course_id = create_response.json['id']
    
    response = client.put(f'/api/v1/courses/{course_id}', 
                          data=json.dumps({'name': 'Geography Updated', 'level': 'Advanced'}),
                          content_type='application/json')
    assert response.status_code == 200

    # Verify course was updated
    get_response = client.get(f'/api/v1/courses/{course_id}')
    assert get_response.json['name'] == 'Geography Updated'

def test_update_course_with_empty_fields(client):
    """Test updating a course with empty fields should fail."""
    create_response = client.post('/api/v1/courses', 
                                   data=json.dumps({'name': 'Physics', 'level': 'Intermediate'}),
                                   content_type='application/json')
    
    course_id = create_response.json['id']
    
    response = client.put(f'/api/v1/courses/{course_id}', 
                          data=json.dumps({'name': '', 'level': 'Advanced'}),
                          content_type='application/json')
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E001'
```