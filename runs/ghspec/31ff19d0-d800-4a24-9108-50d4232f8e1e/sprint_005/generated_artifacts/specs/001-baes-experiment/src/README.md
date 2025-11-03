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

def test_create_teacher_with_valid_data(client):
    """Test creating a new teacher with valid name and email."""
    response = client.post('/teachers', json={'name': 'Jane Doe', 'email': 'jane.doe@example.com'})
    assert response.status_code == 201
    assert 'teacher' in response.json
    assert response.json['teacher']['name'] == 'Jane Doe'
    assert response.json['teacher']['email'] == 'jane.doe@example.com'

def test_create_teacher_without_name(client):
    """Test creating a teacher without a name."""
    response = client.post('/teachers', json={'email': 'jane.doe@example.com'})
    assert response.status_code == 400
    assert response.json['error']['message'] == 'Name is required.'

def test_create_teacher_with_invalid_email(client):
    """Test creating a teacher with an incorrectly formatted email."""
    response = client.post('/teachers', json={'name': 'Jane Doe', 'email': 'invalid-email'})
    assert response.status_code == 400
    assert response.json['error']['message'] == 'Invalid email format.'

def test_retrieve_teachers(client):
    """Test retrieving all teachers."""
    # First, create a teacher for verification
    client.post('/teachers', json={'name': 'Jane Doe', 'email': 'jane.doe@example.com'})
    
    response = client.get('/teachers')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check if the response is a list
    assert len(response.json) > 0  # At least one teacher should be returned
    assert response.json[0]['name'] == 'Jane Doe'
    assert response.json[0]['email'] == 'jane.doe@example.com'