```python
import pytest
from flask import json
from src.app import app
from src.models import Course

@pytest.fixture
def client():
    """Create a test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_course_with_valid_data(client):
    """Test case for creating a new Course with valid name and level."""
    response = client.post('/courses', data=json.dumps({
        'name': 'Mathematics 101',
        'level': 'Beginner'
    }), content_type='application/json')
    
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['name'] == 'Mathematics 101'
    assert data['level'] == 'Beginner'

def test_create_course_without_name(client):
    """Test case for attempting to create a Course without a name."""
    response = client.post('/courses', data=json.dumps({
        'level': 'Beginner'
    }), content_type='application/json')
    
    assert response.status_code == 400
    data = response.get_json()
    assert data == {'error': {'code': 'E001', 'message': 'Missing required fields: name'}}

def test_create_course_without_level(client):
    """Test case for attempting to create a Course without a level."""
    response = client.post('/courses', data=json.dumps({
        'name': 'Mathematics 101'
    }), content_type='application/json')
    
    assert response.status_code == 400
    data = response.get_json()
    assert data == {'error': {'code': 'E001', 'message': 'Missing required fields: level'}}

def test_retrieve_course_with_valid_id(client):
    """Test case for retrieving a Course with valid ID."""
    # First, create a course to retrieve
    create_response = client.post('/courses', data=json.dumps({
        'name': 'Science 101',
        'level': 'Intermediate'
    }), content_type='application/json')
    
    course_id = create_response.get_json()['id']
    
    # Now, retrieve the course
    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == course_id
    assert data['name'] == 'Science 101'
    assert data['level'] == 'Intermediate'

def test_retrieve_course_with_invalid_id(client):
    """Test case for retrieving a Course with invalid ID."""
    response = client.get('/courses/999')  # Assuming 999 does not exist
    assert response.status_code == 404
    data = response.get_json()
    assert data == {'error': {'message': 'Course not found'}}
```