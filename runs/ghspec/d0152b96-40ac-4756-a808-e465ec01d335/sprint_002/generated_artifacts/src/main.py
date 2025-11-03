```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

# Initialize the TestClient for testing the API
client = TestClient(app)

def test_create_student():
    """Test for creating a student with a valid name."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # Check for successful creation
    assert "id" in response.json()       # Check if the response contains the student ID

def test_create_student_with_email():
    """Test for creating a student with a valid email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "john.doe@example.com"

def test_create_student_with_invalid_email():
    """Test for attempted creation of a student with an invalid email format."""
    response = client.post("/students", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400  # Ensure that a bad request is returned
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}  # Check error message format

def test_create_student_with_empty_email():
    """Test for attempted creation of a student with an empty email."""
    response = client.post("/students", json={"name": "John Doe", "email": ""})
    assert response.status_code == 400  # Ensure that a bad request is returned
    assert response.json() == {"error": {"code": "E001", "message": "Email cannot be empty"}}  # Check error message format
```