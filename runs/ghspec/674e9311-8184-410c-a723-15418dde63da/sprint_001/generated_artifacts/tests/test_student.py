import pytest
from flask import Flask, jsonify, request
import json

# Assuming the necessary methods for initializing the app and database are in place
# from src.api import create_app
# from src.models.student import init_db, Student

@pytest.fixture
def app():
    # Set up the Flask app for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # Initialize DB
    with app.app_context():
        # init_db()  # Uncomment once the actual DB initialization is implemented
        pass

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_student(client):
    """Test the creation of a student."""
    response = client.post('/students', json={'name': 'John Doe'})
    data = json.loads(response.data)

    assert response.status_code == 201  # HTTP 201 Created
    assert 'student' in data  # Check the response contains the student data
    assert data['student']['name'] == 'John Doe'  # Verify the student name is correct

def test_create_student_invalid(client):
    """Test creating a student with invalid data."""
    response = client.post('/students', json={})
    data = json.loads(response.data)

    assert response.status_code == 400  # HTTP 400 Bad Request
    assert 'error' in data  # Check the response contains an error message

def test_get_students_empty(client):
    """Test getting students when none exist."""
    response = client.get('/students')
    data = json.loads(response.data)

    assert response.status_code == 200  # HTTP 200 OK
    assert data == []  # Verify the response is an empty list

def test_get_students(client):
    """Test getting students after creation."""
    client.post('/students', json={'name': 'John Doe'})
    client.post('/students', json={'name': 'Jane Doe'})

    response = client.get('/students')
    data = json.loads(response.data)

    assert response.status_code == 200  # HTTP 200 OK
    assert len(data) == 2  # Verify we have two students
    assert data[0]['name'] == 'John Doe'  # Verify the first student's name
    assert data[1]['name'] == 'Jane Doe'  # Verify the second student's name