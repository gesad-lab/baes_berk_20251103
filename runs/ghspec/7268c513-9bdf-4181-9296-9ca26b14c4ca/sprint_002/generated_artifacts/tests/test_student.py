import pytest
from flask import json
from app import create_app, db  # Assuming create_app sets up the Flask app and db is the SQLAlchemy instance
from app.models import Student  # Assuming the Student model is defined in models.py

@pytest.fixture
def client():
    app = create_app({'TESTING': True})  # Create a test instance of the application
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client

# New tests for email handling
def test_create_student_with_email(client):
    """Test successful creation of a student with email."""
    response = client.post('/students', json={
        "name": "John Doe",
        "email": "john@example.com"
    })
    assert response.status_code == 201
    assert response.json['name'] == "John Doe"
    assert response.json['email'] == "john@example.com"

def test_create_student_missing_email(client):
    """Test creation of a student with missing email, expecting a validation error."""
    response = client.post('/students', json={
        "name": "John Doe",
        "email": ""
    })
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert "Email is required." in response.json['error']['message']

def test_create_student_missing_name(client):
    """Test creation of a student with missing name, expecting a validation error."""
    response = client.post('/students', json={
        "name": "",
        "email": "john@example.com"
    })
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert "Name is required." in response.json['error']['message']

def test_get_all_students(client):
    """Test retrieval of all student records, ensuring email presence."""
    # Create a student to test retrieval
    client.post('/students', json={
        "name": "Jane Doe",
        "email": "jane@example.com"
    })
    
    response = client.get('/students')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Ensure the response is a list
    assert len(response.json) > 0  # Ensure we have students in the response

    # Check that the student we created is present
    assert any(student['email'] == "jane@example.com" for student in response.json)