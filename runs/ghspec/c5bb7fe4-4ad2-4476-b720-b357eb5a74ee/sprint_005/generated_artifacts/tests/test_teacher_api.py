import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models.teacher import Teacher  # Import the Teacher model
from src.api.teacher_api import app  # Import the Flask app with the teacher API
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and db for testing
@pytest.fixture(scope='module')
def test_client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    
    # Create the tables
    with app.app_context():
        db.create_all()
    yield app.test_client()  # Return the test client
    with app.app_context():
        db.drop_all()  # Cleanup after tests


def test_create_teacher_success(test_client):
    """Test creating a teacher with valid data."""
    response = test_client.post('/api/v1/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201  # Assert creation successful
    assert b'Teacher created successfully' in response.data  # Assert success message


def test_create_teacher_missing_fields(test_client):
    """Test creating a teacher without mandatory fields raises error."""
    response = test_client.post('/api/v1/teachers', json={
        'name': 'Jane Doe'  # Missing email
    })
    
    assert response.status_code == 400  # Assert bad request error
    assert b'Missing required fields' in response.data  # Assert error message


def test_get_teacher_details_success(test_client):
    """Test retrieving teacher details by ID."""
    # First, create a teacher to be retrieved
    response = test_client.post('/api/v1/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    teacher_id = response.get_json()['id']  # Get the ID of the created teacher

    response = test_client.get(f'/api/v1/teachers/{teacher_id}')
    assert response.status_code == 200  # Assert fetch successful
    data = response.get_json()
    assert data['name'] == 'John Doe'  # Assert correct name
    assert data['email'] == 'john.doe@example.com'  # Assert correct email


def test_update_teacher_success(test_client):
    """Test updating an existing teacher's information."""
    # First, create a teacher to be updated
    response = test_client.post('/api/v1/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    teacher_id = response.get_json()['id']  # Get the ID of the created teacher

    response = test_client.put(f'/api/v1/teachers/{teacher_id}', json={
        'name': 'John Smith',
        'email': 'john.smith@example.com'
    })
    assert response.status_code == 200  # Assert update successful
    updated_response = test_client.get(f'/api/v1/teachers/{teacher_id}')
    updated_data = updated_response.get_json()
    assert updated_data['name'] == 'John Smith'  # Assert updated name
    assert updated_data['email'] == 'john.smith@example.com'  # Assert updated email


def test_update_teacher_invalid_email(test_client):
    """Test updating teacher with invalid email raises error."""
    # First, create a teacher to be updated
    response = test_client.post('/api/v1/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    teacher_id = response.get_json()['id']  # Get the ID of the created teacher

    response = test_client.put(f'/api/v1/teachers/{teacher_id}', json={
        'name': 'John Doe',
        'email': 'invalid-email'  # Invalid email format
    })
    assert response.status_code == 400  # Assert bad request error
    assert b'Invalid email format' in response.data  # Assert error message