```python
import pytest
from flask import Flask, json
from src.routes import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_user_with_valid_email(client):
    """Test the user creation with a valid email."""
    response = client.post('/users', json={'email': 'testuser@example.com'})
    assert response.status_code == 201
    assert response.json['message'] == "User created successfully."

def test_create_user_with_missing_email(client):
    """Test the user creation with a missing email."""
    response = client.post('/users', json={})
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E001'
    assert response.json['error']['message'] == "Email is required."

def test_create_user_with_duplicate_email(client):
    """Test the user creation with a duplicate email."""
    # First, create a user with the email
    client.post('/users', json={'email': 'duplicate@example.com'})
    
    # Try to create another user with the same email
    response = client.post('/users', json={'email': 'duplicate@example.com'})
    assert response.status_code == 409
    assert response.json['error']['code'] == 'E002'
    assert response.json['error']['message'] == "Email already exists."

def test_email_validation_format(client):
    """Test the user creation with an invalid email format."""
    response = client.post('/users', json={'email': 'invalid-email'})
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E003'
    assert response.json['error']['message'] == "Invalid email format."
```