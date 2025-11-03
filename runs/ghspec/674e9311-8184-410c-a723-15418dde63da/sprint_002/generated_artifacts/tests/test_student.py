```python
import pytest
from flask import Flask, jsonify, request
# Assuming the necessary methods for initializing the app and database are in place
from src.api import create_app
from src.models.student import init_db, Student

@pytest.fixture
def app():
    # Set up the Flask app for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # Initialize DB
    with app.app_context():
        init_db()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_student_with_email(client):
    """Test creating a student with a valid email"""
    response = client.post('/students', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201  # Created
    data = response.get_json()
    assert data['message'] == "Student created successfully"
    assert 'id' in data  # Assuming the response returns the new student ID
    assert data['email'] == "john@example.com"

def test_create_student_with_invalid_email(client):
    """Test creating a student with an invalid email"""
    response = client.post('/students', json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 400  # Bad Request
    data = response.get_json()
    assert data['error']['code'] == "E001"  # Example error code for invalid email
    assert data['error']['message'] == "Invalid email format"

def test_create_student_without_email(client):
    """Test creating a student without an email"""
    response = client.post('/students', json={"name": "Alice"})
    assert response.status_code == 400  # Bad Request
    data = response.get_json()
    assert data['error']['code'] == "E002"  # Example error code for missing email
    assert data['error']['message'] == "Email is required"

def test_retrieve_students_with_emails(client):
    """Test retrieving the list of all students including emails"""
    # Create a student for the test
    client.post('/students', json={"name": "John Doe", "email": "john@example.com"})
    client.post('/students', json={"name": "Jane Doe", "email": "jane@example.com"})
    
    response = client.get('/students')
    assert response.status_code == 200  # OK
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2  # We should have 2 students in the response
    assert any(student['email'] == "john@example.com" for student in data)
    assert any(student['email'] == "jane@example.com" for student in data)
```