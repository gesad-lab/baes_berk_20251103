import json
import pytest
from flask import Flask
from your_application import create_app, db, Student

# Instantiate the Flask app for testing
app = create_app()

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
    with app.app_context():
        db.drop_all()  # Cleanup after tests

def test_create_student(client):
    """Test that creating a student returns the expected JSON response."""
    response = client.post('/api/students', json={"name": "John Doe"})
    assert response.status_code == 201  # Check for created status
    assert response.is_json  # Check that response is JSON
    data = response.get_json()
    assert 'id' in data  # Ensure ID is returned
    assert data['name'] == "John Doe"  # Ensure the name matches

def test_create_student_missing_name(client):
    """Test that creating a student without a name returns an error."""
    response = client.post('/api/students', json={"name": ""})
    assert response.status_code == 400  # Bad request for missing name
    assert response.is_json
    data = response.get_json()
    assert data['error']['message'] == "Name is required."  # Check error message

def test_get_student(client):
    """Test that retrieving an existing student returns the expected JSON response."""
    response = client.post('/api/students', json={"name": "Jane Doe"})
    student_id = response.get_json()['id']
    response = client.get(f'/api/students/{student_id}')
    assert response.status_code == 200  # Check for OK status
    assert response.is_json
    data = response.get_json()
    assert data['id'] == student_id
    assert data['name'] == "Jane Doe"

def test_get_student_not_found(client):
    """Test that retrieving a non-existing student returns a 404 error."""
    response = client.get('/api/students/999')  # Non-existing ID
    assert response.status_code == 404  # Check for not found status
    assert response.is_json
    data = response.get_json()
    assert data['error']['message'] == "Student not found."  # Check error message

def test_update_student(client):
    """Test that updating an existing student's name returns the expected JSON response."""
    response = client.post('/api/students', json={"name": "James Smith"})
    student_id = response.get_json()['id']
    response = client.put(f'/api/students/{student_id}', json={"name": "James Bond"})
    assert response.status_code == 200  # Check for OK status
    assert response.is_json
    data = response.get_json()
    assert data['id'] == student_id
    assert data['name'] == "James Bond"  # Ensure name is updated

def test_delete_student(client):
    """Test that deleting a student returns a confirmation JSON response."""
    response = client.post('/api/students', json={"name": "Jake White"})
    student_id = response.get_json()['id']
    response = client.delete(f'/api/students/{student_id}')
    assert response.status_code == 200  # Check for successful deletion status
    assert response.is_json
    data = response.get_json()
    assert data['message'] == "Student deleted successfully."  # Check confirmation message

def test_delete_student_not_found(client):
    """Test that deleting a non-existing student returns a 404 error."""
    response = client.delete('/api/students/999')  # Non-existing ID
    assert response.status_code == 404  # Check for not found status
    assert response.is_json
    data = response.get_json()
    assert data['error']['message'] == "Student not found."  # Check error message