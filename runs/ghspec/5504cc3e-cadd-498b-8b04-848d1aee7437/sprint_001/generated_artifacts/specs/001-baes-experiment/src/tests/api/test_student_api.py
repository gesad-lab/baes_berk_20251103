import pytest
from flask import Flask, json
from app import create_app, db  # Assuming you have a create_app function and db object

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup the database before tests
        yield client
        db.drop_all()  # Clean up after tests

def test_register_student(client):
    """Test registering a new student with a valid name."""
    response = client.post('/api/students', json={'name': 'John Doe'})
    assert response.status_code == 201  # Created
    assert response.json['message'] == 'Student registered successfully.'
    assert 'id' in response.json  # Ensure an ID is returned

def test_retrieve_students(client):
    """Test retrieving a list of all registered students."""
    client.post('/api/students', json={'name': 'John Doe'})
    response = client.get('/api/students')
    assert response.status_code == 200  # OK
    assert isinstance(response.json, list)  # Should be a list
    assert len(response.json) > 0  # Ensure there is at least one student

def test_update_student(client):
    """Test updating a student's name."""
    response = client.post('/api/students', json={'name': 'John Doe'})
    student_id = response.json['id']
    
    update_response = client.put(f'/api/students/{student_id}', json={'name': 'Jane Doe'})
    assert update_response.status_code == 200  # OK
    assert update_response.json['message'] == 'Student updated successfully.'
    
    # Verify the name has been changed
    fetch_response = client.get(f'/api/students/{student_id}')
    assert fetch_response.json['name'] == 'Jane Doe'

def test_delete_student(client):
    """Test deleting a student."""
    response = client.post('/api/students', json={'name': 'John Doe'})
    student_id = response.json['id']
    
    delete_response = client.delete(f'/api/students/{student_id}')
    assert delete_response.status_code == 200  # OK
    assert delete_response.json['message'] == 'Student deleted successfully.'
    
    # Verify the student has been removed
    fetch_response = client.get(f'/api/students/{student_id}')
    assert fetch_response.status_code == 404  # Not Found

def test_register_student_invalid_name(client):
    """Test that registering a student without a name returns a meaningful error."""
    response = client.post('/api/students', json={'name': ''})
    assert response.status_code == 400  # Bad Request
    assert response.json['error']['code'] == 'E001'  # Specific error code
    assert response.json['error']['message'] == 'Name cannot be empty.'  # Meaningful error message