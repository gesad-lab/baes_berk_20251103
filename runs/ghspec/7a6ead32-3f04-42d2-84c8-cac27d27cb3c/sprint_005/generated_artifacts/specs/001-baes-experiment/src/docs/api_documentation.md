---
File: tests/api/test_teacher_creation.py
```python
import json
import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture
def create_teacher(client):
    """Helper function to create a teacher in the test database."""
    def _create_teacher(name, email):
        response = client.post("/api/v1/teachers", json={"name": name, "email": email})
        return response
    return _create_teacher

def test_create_teacher_with_valid_input(client, create_teacher):
    """Test the successful creation of a Teacher with valid inputs."""
    response = create_teacher("Jane Doe", "jane.doe@example.com")
    assert response.status_code == 201  # Expecting a 201 Created response
    assert response.json() == {
        "id": 1,  # Assuming the ID will be auto-generated
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

def test_create_teacher_with_invalid_email(client, create_teacher):
    """Test the validation response for an invalid email format."""
    response = create_teacher("John Doe", "invalid_email_format")
    assert response.status_code == 400  # Expecting a 400 Bad Request response
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Invalid email format",
            "details": {}
        }
    }

def test_create_teacher_with_duplicate_email(client, create_teacher):
    """Test the response for attempting to create a Teacher with a duplicate email."""
    create_teacher("John Doe", "john.doe@example.com")  # Create the first teacher
    response = create_teacher("John Smith", "john.doe@example.com")  # Try to create another with the same email
    assert response.status_code == 400  # Expecting a 400 Bad Request response
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email is already in use",
            "details": {}
        }
    }
```