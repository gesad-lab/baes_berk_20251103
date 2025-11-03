```python
import json
import pytest
from flask import Flask
from flask.testing import FlaskClient
from src.app import create_app
from src.models import db, Teacher  # Importing the Teacher model

@pytest.fixture
def client() -> FlaskClient:
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            # Create the database and add test data
            db.create_all()
            # Optionally add test data here if needed
            yield client
            db.drop_all()

def test_create_teacher_success(client: FlaskClient):
    """Test creation of a teacher with valid input."""
    response = client.post('/teachers', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == "Teacher successfully created."
    assert 'teacher_id' in data
    assert data['name'] == "John Doe"
    assert data['email'] == "john.doe@example.com"

def test_create_teacher_missing_name(client: FlaskClient):
    """Test error handling for missing name."""
    response = client.post('/teachers', json={
        "email": "john.doe@example.com"
    })

    assert response.status_code == 400  # Assuming 400 for bad request
    data = response.get_json()
    assert data['error']['code'] == "E001"  # Error code for missing fields
    assert data['error']['message'] == "Name is required."

def test_create_teacher_missing_email(client: FlaskClient):
    """Test error handling for missing email."""
    response = client.post('/teachers', json={
        "name": "John Doe"
    })

    assert response.status_code == 400  # Assuming 400 for bad request
    data = response.get_json()
    assert data['error']['code'] == "E002"  # Error code for missing fields
    assert data['error']['message'] == "Email is required."

def test_retrieve_teacher_success(client: FlaskClient):
    """Test retrieving a teacher's information."""
    # First create a teacher to retrieve
    create_response = client.post('/teachers', json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    })
    teacher_id = create_response.get_json()['teacher_id']
    
    # Now retrieve teacher information 
    response = client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['teacher_id'] == teacher_id
    assert data['name'] == "Jane Doe"
    assert data['email'] == "jane.doe@example.com"

def test_retrieve_teacher_not_found(client: FlaskClient):
    """Test response structure for teacher not found."""
    response = client.get('/teachers/99999')  # Assuming this ID doesn't exist
    assert response.status_code == 404  # Assuming 404 for not found
    data = response.get_json()
    assert data['error']['code'] == "E003"  # Error code for not found
    assert data['error']['message'] == "Teacher not found."
```