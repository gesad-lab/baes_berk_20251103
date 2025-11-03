```python
import json
import pytest
from src.app import app  # Assuming the Flask app is in src/app.py
from src.models import Course, Teacher  # Import the Teacher model for interaction
from flask import jsonify

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_teacher_with_valid_data_succeeds(client):
    """Test the creation of a new teacher with valid data."""
    # Arrange
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    # Act
    response = client.post('/api/v1/teachers', json=payload)

    # Assert
    assert response.status_code == 201
    response_json = response.get_json()
    assert 'teacher_id' in response_json['message']
    assert response_json['message'] == 'Teacher created successfully'

def test_create_teacher_without_name_fails(client):
    """Test the creation of a new teacher without a name."""
    payload = {
        "email": "john.doe@example.com"
    }
    response = client.post('/api/v1/teachers', json=payload)
    
    assert response.status_code == 400
    response_json = response.get_json()
    assert response_json == {'error': {'code': 'E001', 'message': 'Name and email are required'}}

def test_create_teacher_without_email_fails(client):
    """Test the creation of a new teacher without an email."""
    payload = {
        "name": "John Doe"
    }
    response = client.post('/api/v1/teachers', json=payload)

    assert response.status_code == 400
    response_json = response.get_json()
    assert response_json == {'error': {'code': 'E001', 'message': 'Name and email are required'}}

def test_get_teacher_details_succeeds(client):
    """Test retrieving a teacher's details by ID."""
    # First, create a teacher to test retrieval
    create_response = client.post('/api/v1/teachers', json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    teacher_id = create_response.get_json()['teacher_id']

    # Act
    response = client.get(f'/api/v1/teachers/{teacher_id}')

    # Assert
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['name'] == "Jane Smith"
    assert response_json['email'] == "jane.smith@example.com"

def test_get_teacher_not_found_fails(client):
    """Test retrieving a teacher's details with a non-existing ID."""
    response = client.get('/api/v1/teachers/9999')  # Assume 9999 is an ID that doesn't exist

    assert response.status_code == 404
    response_json = response.get_json()
    assert 'error' in response_json
```
