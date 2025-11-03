import pytest
from flask import json
from app import create_app, db
from src.models.course import Course  # Assuming Course model exists in the specified path

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup the database before tests
        yield client
        db.drop_all()  # Clean up after tests

def test_create_course_with_valid_data(client):
    """Test creating a course with valid data."""
    data = {
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }
    response = client.post('/api/courses', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201  # Check for Created status
    json_response = json.loads(response.data)
    assert 'id' in json_response  # Check if course ID is returned
    assert json_response['name'] == data['name']
    assert json_response['level'] == data['level']

def test_create_course_with_missing_name(client):
    """Test creating a course without a name returns an error."""
    data = {
        'level': 'Beginner'
    }
    response = client.post('/api/courses', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400  # Check for Bad Request status
    json_response = json.loads(response.data)
    assert json_response['error']['code'] == 'E001'  # Example error code for missing fields

def test_create_course_with_invalid_level(client):
    """Test creating a course with an invalid level returns an error."""
    data = {
        'name': 'Introduction to Programming',
        'level': 'InvalidLevel'
    }
    response = client.post('/api/courses', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400  # Check for Bad Request status
    json_response = json.loads(response.data)
    assert json_response['error']['code'] == 'E002'  # Example error code for invalid level

def test_get_course_by_id(client):
    """Test retrieving a course by ID after creating it."""
    # First create a course
    data = {
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    }
    post_response = client.post('/api/courses', data=json.dumps(data), content_type='application/json')
    course_id = json.loads(post_response.data)['id']

    # Now retrieve that course by ID
    response = client.get(f'/api/courses/{course_id}')
    assert response.status_code == 200  # Check for OK status
    json_response = json.loads(response.data)
    assert json_response['id'] == course_id
    assert json_response['name'] == data['name']
    assert json_response['level'] == data['level']