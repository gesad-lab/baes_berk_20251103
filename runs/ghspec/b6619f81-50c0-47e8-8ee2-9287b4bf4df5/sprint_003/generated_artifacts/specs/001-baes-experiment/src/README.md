import json
import pytest
from flask import Flask
from app import app, db
from models import Student, Course  # Assuming course model is in models.py

@pytest.fixture
def client():
    with app.test_client() as client:
        # Setup code for the database can be initialized here
        db.create_all()  # Create tables for the test
        yield client
        # Teardown code for cleaning the database after each test
        db.drop_all()

def test_create_course(client):
    """Test creating a new course with name and level."""
    response = client.post('/courses', json={
        'name': 'Mathematics 101',
        'level': 'Beginner'
    })
    assert response.status_code == 201  # Course created successfully
    data = json.loads(response.data)
    assert data['id'] is not None  # Check if ID is returned
    assert data['name'] == 'Mathematics 101'
    assert data['level'] == 'Beginner'

def test_create_course_missing_name(client):
    """Test creating a course without a name."""
    response = client.post('/courses', json={
        'level': 'Beginner'
    })
    assert response.status_code == 400  # Bad request due to missing name
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Invalid input error code
    assert 'name' in data['error']['details']  # Error details should show that name is required

def test_create_course_missing_level(client):
    """Test creating a course without a level."""
    response = client.post('/courses', json={
        'name': 'Mathematics 101'
    })
    assert response.status_code == 400  # Bad request due to missing level
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Invalid input error code
    assert 'level' in data['error']['details']  # Error details should show that level is required

def test_get_course(client):
    """Test retrieving a course."""
    create_response = client.post('/courses', json={
        'name': 'Mathematics 101',
        'level': 'Beginner'
    })
    course_id = json.loads(create_response.data)['id']

    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200  # Successfully retrieved
    data = json.loads(response.data)
    assert data['id'] == course_id
    assert data['name'] == 'Mathematics 101'
    assert data['level'] == 'Beginner'

def test_update_course(client):
    """Test updating an existing course."""
    create_response = client.post('/courses', json={
        'name': 'Mathematics 101',
        'level': 'Beginner'
    })
    course_id = json.loads(create_response.data)['id']

    response = client.put(f'/courses/{course_id}', json={
        'name': 'Mathematics 102',
        'level': 'Intermediate'
    })
    assert response.status_code == 200  # Successfully updated
    data = json.loads(response.data)
    assert data['id'] == course_id
    assert data['name'] == 'Mathematics 102'
    assert data['level'] == 'Intermediate'