import pytest
from flask import json
from src.app import app
from src.models import Teacher  # Import the Teacher model

@pytest.fixture
def client():
    """Create a test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_teacher_with_valid_data(client):
    """Test case for creating a teacher with valid data."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }), content_type='application/json')
    
    assert response.status_code == 201  # Created
    assert 'id' in response.json  # Ensure the response contains the teacher ID

def test_create_teacher_with_missing_name(client):
    """Test case for creating a teacher with missing name."""
    response = client.post('/teachers', data=json.dumps({
        'email': 'john.doe@example.com'
    }), content_type='application/json')
    
    assert response.status_code == 400  # Bad Request
    assert response.json['error']['code'] == 'E001'  # Expected error code for missing name

def test_create_teacher_with_invalid_email(client):
    """Test case for creating a teacher with invalid email format."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'Jane Doe',
        'email': 'not-an-email'
    }), content_type='application/json')
    
    assert response.status_code == 400  # Bad Request
    assert response.json['error']['code'] == 'E002'  # Expected error code for invalid email format

def test_get_teacher_by_id(client):
    """Test case for retrieving a teacher by ID."""
    # First create a teacher to ensure we have one to retrieve
    create_response = client.post('/teachers', data=json.dumps({
        'name': 'Alice Smith',
        'email': 'alice.smith@example.com'
    }), content_type='application/json')
    
    teacher_id = create_response.json['id']
    
    # Now retrieve the teacher by ID
    response = client.get(f'/teachers/{teacher_id}')
    
    assert response.status_code == 200  # OK
    assert response.json['name'] == 'Alice Smith'  # Check the name is correct
    assert response.json['email'] == 'alice.smith@example.com'  # Check the email is correct

def test_get_non_existent_teacher(client):
    """Test case for attempting to retrieve a non-existent teacher."""
    response = client.get('/teachers/99999')  # Assuming 99999 does not exist
    
    assert response.status_code == 404  # Not Found
    assert response.json['error']['code'] == 'E003'  # Expected error code for non-existent teacher