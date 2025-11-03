import pytest
from src.api.student_routes import create_student, get_student, update_student
from src.models.student_model import Student
from flask import json

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_create_student_with_email(client):
    """Test creating a student with a valid email."""
    response = client.post('/students', 
                           data=json.dumps({"name": "John Doe", "email": "john.doe@example.com"}), 
                           content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data.decode())
    assert data['name'] == "John Doe"
    assert data['email'] == "john.doe@example.com"

def test_retrieve_student_email(client):
    """Test retrieving a student by ID including the email field."""
    # First, create a student to retrieve
    create_response = client.post('/students', 
                                   data=json.dumps({"name": "Jane Doe", "email": "jane.doe@example.com"}), 
                                   content_type='application/json')
    student_id = json.loads(create_response.data.decode())['id']
    
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data['id'] == student_id
    assert data['email'] == "jane.doe@example.com"

def test_update_student_email(client):
    """Test updating a student's email."""
    # First, create a student to update
    create_response = client.post('/students', 
                                   data=json.dumps({"name": "Alice Smith", "email": "alice.smith@example.com"}), 
                                   content_type='application/json')
    student_id = json.loads(create_response.data.decode())['id']
    
    # Update the student's email
    update_response = client.put(f'/students/{student_id}', 
                                 data=json.dumps({"name": "Alice Smith", "email": "alice.new@example.com"}), 
                                 content_type='application/json')
    
    assert update_response.status_code == 200
    updated_data = json.loads(update_response.data.decode())
    assert updated_data['email'] == "alice.new@example.com"

def test_create_student_with_invalid_email(client):
    """Test creating a student with an invalid email format."""
    response = client.post('/students', 
                           data=json.dumps({"name": "Bob", "email": "invalid-email"}), 
                           content_type='application/json')
    
    assert response.status_code == 400
    error_data = json.loads(response.data.decode())
    assert error_data['error']['message'] == "Invalid email format."  # Adjust the message according to your implementation

def test_create_student_without_email(client):
    """Test creating a student without an email."""
    response = client.post('/students', 
                           data=json.dumps({"name": "Charlie"}), 
                           content_type='application/json')
    
    assert response.status_code == 400
    error_data = json.loads(response.data.decode())
    assert error_data['error']['message'] == "Email is required."  # Adjust the message according to your implementation