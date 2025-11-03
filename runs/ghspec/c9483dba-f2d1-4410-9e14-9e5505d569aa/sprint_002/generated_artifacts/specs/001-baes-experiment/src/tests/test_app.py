import pytest
from app import app  # Assuming 'app' is the Flask app instance
from models import Student  # Assuming 'Student' model is defined in 'models.py'
from unittest.mock import patch

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_student_success(client):
    """Test creating a student with a valid name and email."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john@example.com'})
    assert response.status_code == 201  # Expecting a 201 Created response
    json_data = response.get_json()
    assert 'id' in json_data
    assert json_data['name'] == 'John Doe'
    assert json_data['email'] == 'john@example.com'

def test_create_student_missing_name(client):
    """Test creating a student without a name."""
    response = client.post('/students', json={'email': 'john@example.com'})
    assert response.status_code == 400  # Expecting a 400 Bad Request response
    json_data = response.get_json()
    assert json_data['error']['code'] == 'E002'  # Example error code for missing name
    assert json_data['error']['message'] == 'Name is required.'

def test_create_student_missing_email(client):
    """Test creating a student without an email."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 400  # Expecting a 400 Bad Request response
    json_data = response.get_json()
    assert json_data['error']['code'] == 'E001'  # Example error code for missing email
    assert json_data['error']['message'] == 'Email is required.'

def test_create_student_duplicate_email(client):
    """Test creating a student with a duplicate email."""
    client.post('/students', json={'name': 'John Doe', 'email': 'john@example.com'})  # Create the first student
    response = client.post('/students', json={'name': 'Jane Doe', 'email': 'john@example.com'})  # Attempt to create duplicate
    assert response.status_code == 409  # Expecting a 409 Conflict response
    json_data = response.get_json()
    assert json_data['error']['code'] == 'E003'  # Example error code for duplicate email
    assert json_data['error']['message'] == 'Email already exists.'