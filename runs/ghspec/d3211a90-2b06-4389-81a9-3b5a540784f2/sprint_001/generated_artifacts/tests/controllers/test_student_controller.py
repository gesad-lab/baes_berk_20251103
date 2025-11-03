```python
import json
import pytest
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Import the application and database
from src.controllers.student_controller import app, db
from src.models.student import Student

# Test configuration
@pytest.fixture(scope='module')
def test_client():
    """Set up the test client and the database for testing."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()  # Create tables in the test database
        yield app.test_client()  # Provide the test client
        db.drop_all()  # Clean up after tests


def test_create_student(test_client):
    """Test the creation of a new student."""
    response = test_client.post('/api/v1/students', 
                                 data=json.dumps({'name': 'John Doe'}),
                                 content_type='application/json')
    
    assert response.status_code == 201  # Expecting 201 Created
    assert response.json['name'] == 'John Doe'


def test_create_student_invalid(test_client):
    """Test creating a student without required fields."""
    response = test_client.post('/api/v1/students', 
                                 data=json.dumps({}),  # No data
                                 content_type='application/json')
    
    assert response.status_code == 400  # Expecting 400 Bad Request
    assert response.json['error']['code'] == 'E001'  # Check specific error code


def test_get_student(test_client):
    """Test retrieving a student by ID."""
    # First create a student
    test_client.post('/api/v1/students', 
                     data=json.dumps({'name': 'Jane Doe'}),
                     content_type='application/json')
    
    # Then retrieve the student
    response = test_client.get('/api/v1/students/1')
    
    assert response.status_code == 200  # Expecting 200 OK
    assert response.json['name'] == 'Jane Doe'


def test_get_student_not_found(test_client):
    """Test retrieving a non-existent student."""
    response = test_client.get('/api/v1/students/999')  # ID that does not exist
    
    assert response.status_code == 404  # Expecting 404 Not Found
    assert response.json['error']['code'] == 'E002'  # Check specific error code


def test_update_student(test_client):
    """Test updating an existing student's name."""
    # First create a student
    test_client.post('/api/v1/students', 
                     data=json.dumps({'name': 'Mark Smith'}),
                     content_type='application/json')
    
    # Then update the student's name
    response = test_client.put('/api/v1/students/1', 
                                data=json.dumps({'name': 'Mark A. Smith'}),
                                content_type='application/json')
    
    assert response.status_code == 200  # Expecting 200 OK
    assert response.json['name'] == 'Mark A. Smith'


def test_delete_student(test_client):
    """Test deleting a student by ID."""
    # First create a student
    test_client.post('/api/v1/students', 
                     data=json.dumps({'name': 'Anna Turner'}),
                     content_type='application/json')
    
    # Then delete the student
    response = test_client.delete('/api/v1/students/1')
    
    assert response.status_code == 204  # Expecting 204 No Content

    # Check if the student has been deleted
    response = test_client.get('/api/v1/students/1')
    assert response.status_code == 404  # Expecting 404 Not Found
```