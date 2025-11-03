```python
import pytest
from flask import json
from src.app import app  # Assuming the Flask app is initialized in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Existing test function example for creating a course
def test_create_course_with_valid_data(client):
    """Test the creation of a course with valid data."""
    response = client.post('/courses', data=json.dumps({
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }), content_type='application/json')
    
    # (Assume course creation assertions are here)

def test_create_teacher_with_valid_data(client):
    """Test creation of a teacher with valid data."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }), content_type='application/json')
    
    assert response.status_code == 201  # Verify success status
    assert response.get_json()['name'] == 'John Doe'  # Verify returned name

def test_retrieve_teacher(client):
    """Test retrieving a teacher's information."""
    response = client.get('/teachers/1')  # Assuming a teacher with id=1 exists
    assert response.status_code == 200
    assert 'name' in response.get_json()  # Validate that name is included in response
    assert 'email' in response.get_json()  # Validate that email is included in response

def test_create_teacher_with_invalid_email(client):
    """Test creation of a teacher with invalid email format."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'Jane Doe',
        'email': 'not-an-email'
    }), content_type='application/json')
    
    assert response.status_code == 400  # Verify error status
    assert response.get_json()['error']['code'] == 'E001'  # Error is due to email

def test_create_teacher_with_missing_name(client):
    """Test creation of a teacher with missing name."""
    response = client.post('/teachers', data=json.dumps({
        'email': 'missing.name@example.com'
    }), content_type='application/json')
    
    assert response.status_code == 400  # Verify error status
    assert response.get_json()['error']['code'] == 'E002'  # Error due to missing name

def test_create_teacher_with_empty_fields(client):
    """Test creation of a teacher with empty fields."""
    response = client.post('/teachers', data=json.dumps({
        'name': '',
        'email': ''
    }), content_type='application/json')
    
    assert response.status_code == 400  # Verify error status
    assert 'error' in response.get_json()  # Check for error message in response
```