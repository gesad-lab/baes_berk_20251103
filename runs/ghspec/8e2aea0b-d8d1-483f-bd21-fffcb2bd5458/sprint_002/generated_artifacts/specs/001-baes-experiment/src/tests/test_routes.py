import json
import pytest
from flask import Flask
from flask.testing import FlaskClient
from src.app import create_app  # Assuming there is a function to create your Flask app
from src.models import db, Student  # Assuming the Student model is defined in models.py

@pytest.fixture
def client() -> FlaskClient:
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            # create database and add test data
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_create_student_with_email(client: FlaskClient):
    """Test creating a student with a valid name and email."""
    response = client.post('/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == "John Doe"
    assert data['email'] == "john.doe@example.com"
    assert 'id' in data  # Ensure an ID was generated

def test_create_student_with_empty_email(client: FlaskClient):
    """Test creating a student with a valid name but empty email."""
    response = client.post('/students', json={
        "name": "John Doe",
        "email": ""
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == "E001"  # Ensure the correct error code is returned
    assert 'message' in data['error']  # Ensure the message is present

def test_retrieve_students_with_email(client: FlaskClient):
    """Test retrieving registered students with their email addresses."""
    # First, create a student
    client.post('/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    
    # Now, retrieve the list of students
    response = client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    
    assert isinstance(data, list)  # Ensure the response is a list
    assert len(data) > 0  # Ensure there is at least one student
    assert 'email' in data[0]  # Ensure email field is present for the first student
    assert data[0]['email'] == "john.doe@example.com"  # Check email matches what was stored