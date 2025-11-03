```python
import pytest
from flask import json
from student_management.app import app, db
from student_management.models import Student


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables for testing
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests


def test_create_student_success(client):
    """Test creating a student with valid data."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'


def test_create_student_without_name(client):
    """Test creating a student without a name field."""
    response = client.post('/students', json={'name': ''})
    assert response.status_code == 400
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E001'
    assert error_data['error']['message'] == "Name field is required."


def test_update_student_success(client):
    """Test updating an existing student with valid data."""
    # First, create a student
    response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = json.loads(response.data)['id']

    # Now update the student's name
    response = client.put(f'/students/{student_id}', json={'name': 'Jane Smith'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Jane Smith'


def test_update_student_not_found(client):
    """Test updating a non-existent student."""
    response = client.put('/students/9999', json={'name': 'Ghost Student'})
    assert response.status_code == 404


def test_delete_student_success(client):
    """Test deleting an existing student."""
    # Create a student first
    response = client.post('/students', json={'name': 'Mark Twain'})
    student_id = json.loads(response.data)['id']

    # Now delete the student
    response = client.delete(f'/students/{student_id}')
    assert response.status_code == 204


def test_delete_student_not_found(client):
    """Test deleting a non-existent student."""
    response = client.delete('/students/9999')
    assert response.status_code == 404


def test_get_student_success(client):
    """Test retrieving a student by ID."""
    response = client.post('/students', json={'name': 'Emily Bronte'})
    student_id = json.loads(response.data)['id']

    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Emily Bronte'


def test_get_student_not_found(client):
    """Test retrieving a non-existent student."""
    response = client.get('/students/9999')
    assert response.status_code == 404


def test_invalid_json(client):
    """Test handling invalid JSON requests."""
    response = client.post('/students', data='not a json')
    assert response.status_code == 400
```
