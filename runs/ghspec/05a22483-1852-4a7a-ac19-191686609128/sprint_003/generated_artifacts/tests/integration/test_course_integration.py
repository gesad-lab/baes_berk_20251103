```python
import pytest
from flask import json
from your_app import create_app, db
from your_app.models import Course  # Assuming Course is defined in models.py


@pytest.fixture
def client():
    app = create_app('testing')  # Use testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema including the Student and Course tables
        yield client
        with app.app_context():
            db.drop_all()  # Cleanup after tests


def test_create_course_success(client):
    """Test creating a course successfully."""
    course_data = {
        "name": "Mathematics",
        "level": "101"
    }

    response = client.post('/courses', data=json.dumps(course_data), content_type='application/json')
    
    assert response.status_code == 201  # Check that the response status is 201 Created
    data = response.get_json()
    assert 'id' in data
    assert data['name'] == course_data['name']
    assert data['level'] == course_data['level']


def test_create_course_missing_fields(client):
    """Test creating a course without required fields returns a validation error."""
    course_data_missing_name = {
        "level": "101"
    }
    
    course_data_missing_level = {
        "name": "Mathematics"
    }

    response_name = client.post('/courses', data=json.dumps(course_data_missing_name), content_type='application/json')
    response_level = client.post('/courses', data=json.dumps(course_data_missing_level), content_type='application/json')
    
    assert response_name.status_code == 400  # Bad Request for missing name
    assert response_level.status_code == 400  # Bad Request for missing level
    assert 'error' in response_name.get_json()  # Check for validation error structure
    assert 'error' in response_level.get_json()  # Check for validation error structure


def test_get_course_by_id(client):
    """Test retrieving a course by ID."""
    course_data = {
        "name": "Science",
        "level": "102"
    }
    
    # First, create a course
    response = client.post('/courses', data=json.dumps(course_data), content_type='application/json')
    created_course_id = response.get_json()['id']

    # Now, attempt to retrieve the same course
    response = client.get(f'/courses/{created_course_id}')
    assert response.status_code == 200  # Check that the response status is 200 OK
    data = response.get_json()
    assert data['id'] == created_course_id
    assert data['name'] == course_data['name']
    assert data['level'] == course_data['level']
    

def test_get_course_not_found(client):
    """Test retrieving a course that does not exist returns a 404 error."""
    response = client.get('/courses/9999')  # Assuming 9999 is a non-existent ID
    assert response.status_code == 404  # Check that the response status is 404 Not Found
    assert 'error' in response.get_json()  # Check for error indication
```