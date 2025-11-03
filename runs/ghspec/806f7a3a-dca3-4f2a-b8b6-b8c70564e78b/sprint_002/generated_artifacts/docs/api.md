---
# Updated tests/test_student.py

```python
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
    """Test creating a student with valid name and email."""
    response = client.post('/api/students', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_retrieve_student_email(client):
    """Test retrieving a student's details including email."""
    # First create a student
    client.post('/api/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    # Now retrieve the student by ID (assuming ID is 1 here)
    response = client.get('/api/students/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'

def test_update_student_email(client):
    """Test updating a student's email."""
    # Create a student first
    client.post('/api/students', json={
        'name': 'Alice Smith',
        'email': 'alice.smith@example.com'
    })
    # Update the student's email (assuming ID is 1)
    response = client.put('/api/students/1', json={
        'name': 'Alice Smith',
        'email': 'alice.newemail@example.com'
    })
    assert response.status_code == 200
    
    # Verify the email was updated
    updated_response = client.get('/api/students/1')
    updated_data = json.loads(updated_response.data)
    assert updated_data['email'] == 'alice.newemail@example.com'

def test_invalid_email_creation(client):
    """Test creating a student with an invalid email."""
    response = client.post('/api/students', json={
        'name': 'Invalid Email User',
        'email': 'invalid-email'
    })
    assert response.status_code == 400
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E001'  # Assuming this error code for invalid email
    assert 'Invalid email format' in error_data['error']['message']

def test_invalid_email_update(client):
    """Test updating a student's email with an invalid format."""
    # Create a student first
    client.post('/api/students', json={
        'name': 'Bob Brown',
        'email': 'bob.brown@example.com'
    })
    response = client.put('/api/students/1', json={
        'name': 'Bob Brown',
        'email': 'invalid-email'
    })
    assert response.status_code == 400
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E001'  # Assuming this error code for invalid email
    assert 'Invalid email format' in error_data['error']['message']

def test_retrieve_nonexistent_student(client):
    """Test retrieving details of a non-existent student."""
    response = client.get('/api/students/999')  # Assuming this ID does not exist
    assert response.status_code == 404
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E002'  # Assuming this error code for not found
    assert 'Student not found' in error_data['error']['message']
```
