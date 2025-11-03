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

def test_create_student_with_valid_data(client):
    """Test case for creating a new Student with valid name and email."""
    response = client.post('/students', data=json.dumps({
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }), content_type='application/json')
    
    # Assert the response is successful and contains the correct data
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_student_without_email(client):
    """Test case for attempting to create a Student without an email."""
    response = client.post('/students', data=json.dumps({
        'name': 'John Doe'
    }), content_type='application/json')

    # Assert the response indicates a client error due to missing email
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data == {'error': {'code': 'E001', 'message': 'Email field is required.'}}

def test_retrieve_student_with_email(client):
    """Test case for retrieving a Student's details by ID."""
    # First, create a student to retrieve
    create_response = client.post('/students', data=json.dumps({
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com'
    }), content_type='application/json')
    student_id = json.loads(create_response.data)['id']

    # Now retrieve the created student by ID
    response = client.get(f'/students/{student_id}')
    
    # Assert the retrieved student data is correct
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == student_id
    assert data['name'] == 'Jane Smith'
    assert data['email'] == 'jane.smith@example.com'

def test_update_student_email(client):
    """Test case for updating an existing Student's email address."""
    # Create a new student for the update operation
    create_response = client.post('/students', data=json.dumps({
        'name': 'Tom Brown',
        'email': 'tom.brown@example.com'
    }), content_type='application/json')
    student_id = json.loads(create_response.data)['id']

    # Update the student's email address
    update_response = client.patch(f'/students/{student_id}', data=json.dumps({
        'email': 'tom.brown@newdomain.com'
    }), content_type='application/json')
    
    # Assert the update response is successful
    assert update_response.status_code == 200
    update_data = json.loads(update_response.data)
    assert update_data['message'] == 'Student email updated successfully.'

    # Retrieve the student again to confirm the email update
    retrieve_response = client.get(f'/students/{student_id}')
    assert retrieve_response.status_code == 200
    retrieve_data = json.loads(retrieve_response.data)
    assert retrieve_data['email'] == 'tom.brown@newdomain.com'
```