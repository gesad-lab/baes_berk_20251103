```python
import pytest
from flask import json
from src.app import app
from src.models import Teacher

@pytest.fixture
def client():
    """Create a test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_teacher_success(client):
    """Test creating a new teacher with valid inputs."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }), content_type='application/json')

    assert response.status_code == 201
    teacher = json.loads(response.data)
    assert teacher['name'] == 'John Doe'
    assert teacher['email'] == 'john.doe@example.com'

def test_create_teacher_missing_name(client):
    """Test creating a teacher without a name."""
    response = client.post('/teachers', data=json.dumps({
        'email': 'john.doe@example.com'
    }), content_type='application/json')

    assert response.status_code == 400
    error_response = json.loads(response.data)
    assert error_response['error']['code'] == 'E001'
    assert error_response['error']['message'] == 'Name is required.'

def test_create_teacher_invalid_email(client):
    """Test creating a teacher with an invalid email."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'John Doe',
        'email': 'invalid-email'
    }), content_type='application/json')

    assert response.status_code == 400
    error_response = json.loads(response.data)
    assert error_response['error']['code'] == 'E002'
    assert error_response['error']['message'] == 'Invalid email format.'

def test_get_teacher_details_success(client):
    """Test retrieving a teacher's details by ID."""
    # First, create a teacher to retrieve
    create_response = client.post('/teachers', data=json.dumps({
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com'
    }), content_type='application/json')
    created_teacher = json.loads(create_response.data)

    # Now retrieve the teacher by ID
    response = client.get(f'/teachers/{created_teacher["id"]}')

    assert response.status_code == 200
    teacher = json.loads(response.data)
    assert teacher['name'] == 'Jane Smith'
    assert teacher['email'] == 'jane.smith@example.com'

def test_get_non_existent_teacher(client):
    """Test retrieving details of a non-existent teacher."""
    response = client.get('/teachers/999')  # Assuming 999 doesn't exist

    assert response.status_code == 404
    error_response = json.loads(response.data)
    assert error_response['error']['code'] == 'E003'
    assert error_response['error']['message'] == 'Teacher not found.'
```