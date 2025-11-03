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
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }), content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data
    assert data['name'] == 'Introduction to Programming'
    assert data['level'] == 'Beginner'

def test_create_course_without_name(client):
    """Test case for attempting to create a Course without a name."""
    response = client.post('/courses', data=json.dumps({
        'level': 'Intermediate'
    }), content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'
    assert data['error']['message'] == 'Name field is required.'

def test_create_course_without_level(client):
    """Test case for attempting to create a Course without a level."""
    response = client.post('/courses', data=json.dumps({
        'name': 'Data Structures'
    }), content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'
    assert data['error']['message'] == 'Level field is required.'

def test_retrieve_course(client):
    """Test case for retrieving a Course by ID."""
    
    # First create a course to retrieve
    create_response = client.post('/courses', data=json.dumps({
        'name': 'Web Development',
        'level': 'Beginner'
    }), content_type='application/json')
    
    course_id = json.loads(create_response.data)['id']  # Get the ID of the created course
    
    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == course_id
    assert data['name'] == 'Web Development'
    assert data['level'] == 'Beginner'
```