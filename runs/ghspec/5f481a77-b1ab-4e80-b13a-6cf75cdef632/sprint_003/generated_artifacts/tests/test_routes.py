```python
import pytest
from flask import json
from src.app import app  # Assuming the Flask app is initialized in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_course_with_valid_data(client):
    """Test the creation of a course with valid data."""
    response = client.post('/courses', data=json.dumps({
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }), content_type='application/json')
    
    assert response.status_code == 201  # Check if course was created successfully
    assert 'id' in response.get_json()  # Ensure the response includes course ID

def test_create_course_with_missing_name(client):
    """Test the creation of a course without a name should fail."""
    response = client.post('/courses', data=json.dumps({
        'level': 'Beginner'
    }), content_type='application/json')

    assert response.status_code == 400  # Bad request due to missing name
    assert response.get_json()['error']['code'] == 'E001'  # Specific error code for validation

def test_retrieve_course(client):
    """Test retrieving an existing course by ID."""
    # First, create a course to retrieve
    create_response = client.post('/courses', data=json.dumps({
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }), content_type='application/json')

    course_id = create_response.get_json()['id']  # Get the ID of the newly created course

    # Now, try to retrieve the course by its ID
    response = client.get(f'/courses/{course_id}')
    
    assert response.status_code == 200  # Ensure retrieval is successful
    data = response.get_json()
    assert data['id'] == course_id  # Check the retrieved course ID matches

def test_retrieve_nonexistent_course(client):
    """Test retrieving a course that does not exist returns 404."""
    response = client.get('/courses/9999')  # Assuming 9999 does not exist
    assert response.status_code == 404  # Not Found
    assert response.get_json()['error']['code'] == 'E002'  # Specific error code for not found
```