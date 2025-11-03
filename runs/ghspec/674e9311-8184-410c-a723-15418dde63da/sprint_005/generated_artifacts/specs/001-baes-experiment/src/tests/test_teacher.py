```python
import pytest
from flask import Flask, jsonify, request
from src.api import create_app
from sqlalchemy.exc import IntegrityError
from src.models.teacher import Teacher  # Import the Teacher model
import re

# Regex for validating email format
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@pytest.fixture
def app():
    # Set up the Flask app for testing
    app = create_app()
    app.config['TESTING'] = True
    return app

def validate_email(email: str):
    """Validate the provided email address format."""
    if not re.match(EMAIL_REGEX, email):
        raise ValueError("E001: Invalid email format")

def test_create_teacher_with_valid_data(app):
    """Test creating a teacher with valid name and email."""
    with app.test_client() as client:
        response = client.post('/teachers', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
        assert response.status_code == 200
        assert response.get_json() == {"message": "Teacher created successfully"}

def test_create_teacher_with_missing_name(app):
    """Test creating a teacher with missing name."""
    with app.test_client() as client:
        response = client.post('/teachers', json={'email': 'john.doe@example.com'})
        assert response.status_code == 400  # Bad Request
        assert response.get_json() == {"error": {"code": "E002", "message": "Name is required"}}

def test_create_teacher_with_missing_email(app):
    """Test creating a teacher with missing email."""
    with app.test_client() as client:
        response = client.post('/teachers', json={'name': 'John Doe'})
        assert response.status_code == 400  # Bad Request
        assert response.get_json() == {"error": {"code": "E002", "message": "Email is required"}}

def test_create_teacher_with_invalid_email(app):
    """Test creating a teacher with invalid email format."""
    with app.test_client() as client:
        response = client.post('/teachers', json={'name': 'John Doe', 'email': 'invalid-email'})
        assert response.status_code == 400  # Bad Request
        assert response.get_json() == {"error": {"code": "E001", "message": "Invalid email format"}}
```