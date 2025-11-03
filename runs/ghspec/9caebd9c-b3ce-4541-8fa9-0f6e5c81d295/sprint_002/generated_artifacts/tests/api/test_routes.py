```python
import json
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from your_application import app, db, Student  # Adjust import based on your structure

# Reinitialize the Flask application and SQLAlchemy for testing
@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables
        yield client  # This will run the test

@pytest.fixture(autouse=True)
def run_around_tests():
    """This will run before each test."""
    db.create_all()  # Create the database before each test
    yield
    db.session.remove()
    db.drop_all()  # Clean up after each test

def test_add_student_with_email(test_client):
    """Test creating a new student with a valid name and email."""
    response = test_client.post('/students', json={"name": "John Doe", "email": "john@example.com"})
    data = json.loads(response.data)
    assert response.status_code == 201  # Check for created status
    assert "id" in data  # Ensure an ID is returned
    assert data["message"] == "Student created successfully."  # Confirmation message

def test_add_student_missing_email(test_client):
    """Test creating a student without providing an email."""
    response = test_client.post('/students', json={"name": "John Doe"})
    data = json.loads(response.data)
    assert response.status_code == 400  # Check for bad request
    assert data["error"]["code"] == "E001"  # Error code for missing email
    assert data["error"]["message"] == "Email is required."

def test_retrieve_student_details(test_client):
    """Test retrieving student details by ID."""
    # First, create a student
    post_response = test_client.post('/students', json={"name": "John Doe", "email": "john@example.com"})
    student_id = json.loads(post_response.data)["id"]

    # Now retrieve the student
    response = test_client.get(f'/students/{student_id}')
    data = json.loads(response.data)
    assert response.status_code == 200  # Check for OK status
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"

def test_data_preservation(test_client):
    """Test that existing students retain their name data."""
    # Create a student
    post_response = test_client.post('/students', json={"name": "Jane Doe", "email": "jane@example.com"})
    student_id = json.loads(post_response.data)["id"]
    
    # Check if the data is preserved
    response = test_client.get(f'/students/{student_id}')
    data = json.loads(response.data)
    assert data["name"] == "Jane Doe"

# Add additional tests here as required based on specifications
```