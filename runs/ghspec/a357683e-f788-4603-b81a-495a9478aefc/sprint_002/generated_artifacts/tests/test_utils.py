```python
import pytest
from app.models import Student
from app import db

# This will be a set of unit tests for validating email addresses
def validate_email(email: str) -> bool:
    """Utility function to validate email format."""
    from email_validator import validate_email, EmailNotValidError
    try:
        # validate_email returns a dict with 'email' key
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


def test_valid_email():
    """Test that valid emails pass the validation."""
    valid_emails = [
        "test@example.com",
        "user.name+tag+sorting@example.com",
        "user@example.co",
        "user@subdomain.example.com"
    ]
    for email in valid_emails:
        assert validate_email(email) is True


def test_invalid_email():
    """Test that invalid emails do not pass the validation."""
    invalid_emails = [
        "plainaddress",
        "@missingusername.com",
        "username@.com",
        "username@.com.",
        "username@com",
        "username@-example.com"
    ]
    for email in invalid_emails:
        assert validate_email(email) is False


def test_student_creation_with_valid_email(test_client):
    """Test creating a student with a valid email address."""
    response = test_client.post('/students', json={
        'name': 'Test Student',
        'email': 'students@example.com'
    })
    data = response.get_json()
    assert response.status_code == 201
    assert 'email' in data
    assert data['email'] == 'students@example.com'


def test_student_creation_with_invalid_email(test_client):
    """Test creating a student with an invalid email address."""
    response = test_client.post('/students', json={
        'name': 'Test Student',
        'email': 'invalid_email'
    })
    data = response.get_json()
    assert response.status_code == 400
    assert data['error']['message'] == 'Invalid email format'
```