import pytest
from flask import json
from app import create_app, db
from models.student import Student

@pytest.fixture
def client():
    app = create_app('testing')  # Use a separate testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create fresh database for each test
        yield client
        with app.app_context():
            db.drop_all()  # Clean up database after tests

def test_create_student(client):
    """Test creating a student with valid data."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert 'id' in response.get_json()

def test_create_student_invalid(client):
    """Test creating a student with invalid data (missing name)."""
    response = client.post('/students', json={})
    assert response.status_code == 400
    assert response.get_json()['error']['code'] == 'E001'  # Example error code for invalid input

def test_get_student(client):
    """Test retrieving a student by ID."""
    response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = response.get_json()['id']
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Jane Doe'

def test_get_student_not_found(client):
    """Test retrieving a non-existent student."""
    response = client.get('/students/999')  # Assuming 999 does not exist
    assert response.status_code == 404
    assert response.get_json()['error']['code'] == 'E002'  # Example error code for not found

def test_update_student(client):
    """Test updating a student's name."""
    response = client.post('/students', json={'name': 'Alice'})
    student_id = response.get_json()['id']
    response = client.put(f'/students/{student_id}', json={'name': 'Alice Updated'})
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Alice Updated'

def test_update_student_not_found(client):
    """Test updating a non-existent student."""
    response = client.put('/students/999', json={'name': 'Updated Name'})
    assert response.status_code == 404
    assert response.get_json()['error']['code'] == 'E002'  # Error code for not found

def test_delete_student(client):
    """Test deleting a student."""
    response = client.post('/students', json={'name': 'Bob'})
    student_id = response.get_json()['id']
    response = client.delete(f'/students/{student_id}')
    assert response.status_code == 204

def test_delete_student_not_found(client):
    """Test attempting to delete a non-existent student."""
    response = client.delete('/students/999')  # Assuming 999 does not exist
    assert response.status_code == 404
    assert response.get_json()['error']['code'] == 'E002'  # Error code for not found