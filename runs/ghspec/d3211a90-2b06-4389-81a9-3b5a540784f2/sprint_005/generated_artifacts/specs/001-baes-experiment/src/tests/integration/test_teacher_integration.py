```python
import pytest
from app import app  # Import the Flask app
from flask import json

@pytest.mark.integration
def test_create_teacher_without_required_fields(client):
    """
    Test case for attempting to create a Teacher without the required fields.
    Expected outcome: The application should respond with an error message
    indicating that both name and email are required.
    """
    response = client.post('/api/v1/teachers', json={})
    assert response.status_code == 400  # Bad Request
    assert response.json == {
        'error': {
            'code': 'E001',
            'message': 'Name and email are required.',
            'details': {}
        }
    }

@pytest.mark.integration
def test_create_teacher_with_duplicate_email(client):
    """
    Test case for attempting to create a Teacher with an email that already exists.
    Expected outcome: The application should respond with an error message stating
    that the email is already in use.
    """
    # First, create a Teacher with a specific email.
    teacher_data = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    client.post('/api/v1/teachers', json=teacher_data)

    # Now try to create another Teacher with the same email.
    response = client.post('/api/v1/teachers', json=teacher_data)
    assert response.status_code == 400  # Bad Request
    assert response.json == {
        'error': {
            'code': 'E002',
            'message': 'Email is already in use.',
            'details': {}
        }
    }

@pytest.mark.integration
def test_create_teacher_with_invalid_email_format(client):
    """
    Test case for attempting to create a Teacher with an invalid email format.
    Expected outcome: The application should respond with an error message
    indicating that the email format is invalid.
    """
    teacher_data = {
        "name": "Jane Doe",
        "email": "invalid-email"
    }
    response = client.post('/api/v1/teachers', json=teacher_data)
    assert response.status_code == 400  # Bad Request
    assert response.json == {
        'error': {
            'code': 'E003',
            'message': 'Invalid email format.',
            'details': {}
        }
    }

@pytest.mark.integration
def test_create_teacher_with_valid_data(client):
    """
    Test case for successfully creating a Teacher with valid data.
    Expected outcome: The application should create the Teacher and return
    the teacher's details in a confirmation message.
    """
    teacher_data = {
        "name": "Carlos Smith",
        "email": "carlos@example.com"
    }
    response = client.post('/api/v1/teachers', json=teacher_data)
    assert response.status_code == 201  # Created
    assert response.json['teacher'] == {
        'name': 'Carlos Smith',
        'email': 'carlos@example.com'
    }
    assert response.json['message'] == "Teacher successfully created."
```