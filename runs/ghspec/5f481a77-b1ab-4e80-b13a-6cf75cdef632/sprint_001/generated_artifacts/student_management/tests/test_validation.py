```python
import pytest
from flask import json
from student_management.app import create_app, db
from student_management.models import Student

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_create_student_with_valid_name(client):
    """Test that a student can be created with a valid name."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert 'student' in response.json
    assert response.json['student']['name'] == 'John Doe'

def test_create_student_missing_name(client):
    """Test that the API returns an error when trying to create a student without a name."""
    response = client.post('/students', json={})
    assert response.status_code == 400  # Bad Request
    assert response.json == {
        'error': {
            'code': 'E001',
            'message': 'Name is required',
            'details': {}
        }
    }

def test_retrieve_student_with_valid_id(client):
    """Test that a student can be retrieved with a valid ID."""
    # First create a student to retrieve
    response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = response.json['student']['id']
    
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json['student']['name'] == 'Jane Doe'

def test_retrieve_student_with_invalid_id(client):
    """Test that the API returns an error when trying to retrieve a student with an invalid ID."""
    response = client.get('/students/999')  # Assuming 999 is an invalid ID
    assert response.status_code == 404  # Not Found
    assert response.json == {
        'error': {
            'code': 'E002',
            'message': 'Student not found',
            'details': {}
        }
    }
```