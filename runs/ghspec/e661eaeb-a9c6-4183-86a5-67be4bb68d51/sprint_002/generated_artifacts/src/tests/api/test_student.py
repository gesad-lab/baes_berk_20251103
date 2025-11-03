import pytest
from fastapi.testclient import TestClient
from src.api.student import app

client = TestClient(app)

def test_create_student_with_invalid_email_format():
    """Test creating a student with an invalid email format."""
    invalid_email_data = {
        "name": "John Doe",
        "email": "john.doe.com"  # Missing "@" symbol
    }
    response = client.post("/students/", json=invalid_email_data)
    assert response.status_code == 400  # Expect Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Invalid email format.",
            "details": {}
        }
    }

def test_create_student_with_empty_email():
    """Test creating a student with an empty email."""
    empty_email_data = {
        "name": "Jane Smith",
        "email": ""  # Empty email
    }
    response = client.post("/students/", json=empty_email_data)
    assert response.status_code == 400  # Expect Bad Request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email must not be empty.",
            "details": {}
        }
    }

def test_create_student_with_null_email():
    """Test creating a student with a null email."""
    null_email_data = {
        "name": "Alice Jones",
        "email": None  # Null email
    }
    response = client.post("/students/", json=null_email_data)
    assert response.status_code == 400  # Expect Bad Request
    assert response.json() == {
        "error": {
            "code": "E003",
            "message": "Email must not be null.",
            "details": {}
        }
    }

def test_create_student_with_invalid_email_domain():
    """Test creating a student with an email that has an invalid domain."""
    invalid_domain_email_data = {
        "name": "Bob Brown",
        "email": "bob@invalid_domain"  # Invalid domain
    }
    response = client.post("/students/", json=invalid_domain_email_data)
    assert response.status_code == 400  # Expect Bad Request
    assert response.json() == {
        "error": {
            "code": "E004",
            "message": "Invalid email domain.",
            "details": {}
        }
    }