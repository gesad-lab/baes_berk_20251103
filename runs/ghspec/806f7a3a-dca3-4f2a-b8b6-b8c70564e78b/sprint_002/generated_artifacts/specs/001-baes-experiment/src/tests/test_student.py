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
    response = client.post('/students', data=json.dumps({
        'name': 'John Doe',
        'email': 'john@example.com'
    }), content_type='application/json')
    
    assert response.status_code == 201  # Verify creation was successful
    data = json.loads(response.data)
    assert 'id' in data  # Verify that the response contains an ID
    assert data['name'] == 'John Doe'  # Check the name
    assert data['email'] == 'john@example.com'  # Check the email

def test_get_student_by_id(client):
    """Test retrieving a student's information by ID."""
    # First, create a student to retrieve
    response = client.post('/students', data=json.dumps({
        'name': 'Jane Doe',
        'email': 'jane@example.com'
    }), content_type='application/json')
    student_id = json.loads(response.data)['id']

    # Now retrieve the student
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == student_id  # Verify that the correct student is returned
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane@example.com'

def test_update_student_email(client):
    """Test updating a student's email."""
    # Create a student first
    response = client.post('/students', data=json.dumps({
        'name': 'John Smith',
        'email': 'johnsmith@example.com'
    }), content_type='application/json')
    student_id = json.loads(response.data)['id']

    # Update the student's email
    response = client.put(f'/students/{student_id}', data=json.dumps({
        'email': 'newjohn@example.com'
    }), content_type='application/json')
    
    assert response.status_code == 200  # Verify update was successful

    # Retrieve the updated student to confirm the email has changed
    response = client.get(f'/students/{student_id}')
    data = json.loads(response.data)
    assert data['email'] == 'newjohn@example.com'  # Check updated email

def test_create_student_with_invalid_email(client):
    """Test creating a student with an invalid email."""
    response = client.post('/students', data=json.dumps({
        'name': 'Invalid User',
        'email': 'invalid-email'
    }), content_type='application/json')

    assert response.status_code == 400  # Expecting a bad request for invalid email
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Check for specific error code
    assert 'Invalid email format' in data['error']['message']  # Check error message
```