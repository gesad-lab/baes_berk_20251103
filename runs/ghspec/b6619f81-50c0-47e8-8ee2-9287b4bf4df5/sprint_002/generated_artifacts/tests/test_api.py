import json
import pytest
from flask import Flask
from app import app, db
from models import Student  # Assuming student model is in models.py

@pytest.fixture
def client():
    with app.test_client() as client:
        # Setup code (e.g., database setup) can go here
        yield client
        # Teardown code (e.g., cleaning database) can go here

def test_create_student_with_email(client):
    """Test creating a new student with name and email."""
    response = client.post('/students', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    data = json.loads(response.data)
    
    assert response.status_code == 201  # Expect Created
    assert 'id' in data  # Check if the student ID is returned
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_retrieve_student_details(client):
    """Test retrieving details of a student, including email."""
    # First, create a student to retrieve
    create_response = client.post('/students', json={
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com'
    })
    student_id = json.loads(create_response.data)['id']

    # Now, retrieve the student
    response = client.get(f'/students/{student_id}')
    data = json.loads(response.data)

    assert response.status_code == 200  # Expect OK
    assert data['id'] == student_id
    assert data['name'] == 'Jane Smith'
    assert data['email'] == 'jane.smith@example.com'

def test_update_student_email(client):
    """Test updating the email of an existing student."""
    # Create a student to update
    create_response = client.post('/students', json={
        'name': 'Alice Johnson',
        'email': 'alice.johnson@example.com'
    })
    student_id = json.loads(create_response.data)['id']

    # Update the student's email
    update_response = client.put(f'/students/{student_id}', json={
        'email': 'alice.newemail@example.com'
    })
    assert update_response.status_code == 200  # Expect OK

    # Retrieve the updated student
    retrieve_response = client.get(f'/students/{student_id}')
    data = json.loads(retrieve_response.data)

    assert data['email'] == 'alice.newemail@example.com'

def test_create_student_without_email(client):
    """Test creating a student without providing an email."""
    response = client.post('/students', json={
        'name': 'No Email Student'
    })  # Missing email field
    assert response.status_code == 400  # Expect Bad Request
    assert 'error' in json.loads(response.data)  # Check error response

def test_create_student_with_invalid_email(client):
    """Test creating a student with an invalid email format."""
    response = client.post('/students', json={
        'name': 'Invalid Email',
        'email': 'invalid_email_format'
    })
    assert response.status_code == 400  # Expect Bad Request
    assert 'error' in json.loads(response.data)  # Check error response