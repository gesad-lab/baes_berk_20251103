```python
import pytest
from flask import json
from src.app import app
from src.models import Student

@pytest.fixture
def client():
    """Create a test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_student_without_name(client):
    """Test case for attempting to create a Student without a name."""
    
    # Attempt to create a student without a name
    response = client.post('/students', data=json.dumps({'email': 'test@example.com'}),
                           content_type='application/json')
    assert response.status_code == 400  # Expect a bad request
    assert b'{"error":{"code":"E001","message":"Name is required"}}' in response.data

def test_create_student_with_email(client):
    """Test case for successfully creating a Student with name and email."""
    
    response = client.post('/students', data=json.dumps({'name': 'John Doe', 'email': 'john@example.com'}),
                           content_type='application/json')
    assert response.status_code == 201  # Expect created status
    data = json.loads(response.data)
    assert 'id' in data  # Ensure an ID was returned
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john@example.com'

def test_retrieve_student_email(client):
    """Test case for retrieving a Student's email by ID."""
    
    # First, create a student to retrieve
    create_response = client.post('/students', data=json.dumps({'name': 'Jane Doe', 'email': 'jane@example.com'}),
                                   content_type='application/json')
    student_id = json.loads(create_response.data)['id']

    # Now retrieve the student by ID
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200  # Expect OK status
    data = json.loads(response.data)
    assert data['email'] == 'jane@example.com'  # Ensure the email is correct

def test_update_student_email(client):
    """Test case for updating a Student's email address."""
    
    # First, create a student to update
    create_response = client.post('/students', data=json.dumps({'name': 'Mark Smith', 'email': 'mark@example.com'}),
                                   content_type='application/json')
    student_id = json.loads(create_response.data)['id']

    # Update the student's email
    update_response = client.put(f'/students/{student_id}/email', data=json.dumps({'email': 'newmark@example.com'}),
                                 content_type='application/json')
    assert update_response.status_code == 200  # Expect OK status
    updated_data = json.loads(update_response.data)
    assert updated_data['message'] == 'Email updated successfully'  # Confirm update message

    # Now retrieve the updated student to ensure email is changed
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200  # Expect OK status
    data = json.loads(response.data)
    assert data['email'] == 'newmark@example.com'  # Ensure the email has been updated correctly
```