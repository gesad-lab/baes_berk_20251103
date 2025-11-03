import pytest
from flask import json
from src.app import create_app  # Assuming you have a Flask application factory

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_student_with_empty_name(client):
    """Test that creating a student with an empty name returns an error."""
    response = client.post('/students', json={'name': ''})  # Assuming the endpoint exists
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E001'  # Replace with actual error code for empty name

def test_create_student_with_valid_email(client):
    """Test that creating a student with a valid name and email succeeds."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201  # Assuming successful creation returns 201
    assert 'id' in response.json  # Check for student ID in response

def test_create_student_with_invalid_email(client):
    """Test that creating a student with an invalid email returns an error."""
    response = client.post('/students', json={'name': 'Jane Doe', 'email': 'invalid-email'})
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E002'  # Replace with actual error code for invalid email

def test_create_student_with_empty_email(client):
    """Test that creating a student with an empty email returns an error."""
    response = client.post('/students', json={'name': 'John Doe', 'email': ''})
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E002'  # Replace with actual error code for empty email

def test_get_all_students_includes_email(client):
    """Test that retrieving all students includes their email addresses."""
    # First create a student to ensure there is data to retrieve
    client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    
    response = client.get('/students')  # Assuming this endpoint retrieves all student records
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check the response is a list
    assert all('email' in student for student in response.json)  # Ensure each student has an email field