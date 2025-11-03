```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py


@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client


def test_create_student_with_email(client):
    """Test creating a new student with email."""
    # Test with valid data
    response = client.post("/api/v1/students", json={"name": "John Doe", "email": "john.doe@example.com", "age": 20})
    assert response.status_code == 201  # Expecting a successful creation
    assert response.json()["email"] == "john.doe@example.com"  # Verify email is returned

    # Test with missing email
    response = client.post("/api/v1/students", json={"name": "Jane Doe", "age": 22})
    assert response.status_code == 422  # Expecting validation error for missing email

    # Test with invalid email
    response = client.post("/api/v1/students", json={"name": "Invalid Email", "email": "invalid-email", "age": 20})
    assert response.status_code == 422  # Expecting validation error for invalid email


def test_update_student_email(client):
    """Test updating an existing student's email."""
    # First, create a student to update
    create_response = client.post("/api/v1/students", json={"name": "Mark Smith", "email": "mark.smith@example.com", "age": 21})
    student_id = create_response.json()["id"]

    # Update with a new email
    update_response = client.put(f"/api/v1/students/{student_id}", json={"name": "Mark Smith", "email": "mark.new@example.com"})
    assert update_response.status_code == 200  # Expecting a successful update
    assert update_response.json()["email"] == "mark.new@example.com"  # Verify email was updated

    # Try updating with an invalid email
    invalid_update_response = client.put(f"/api/v1/students/{student_id}", json={"name": "Mark Smith", "email": "not-an-email"})
    assert invalid_update_response.status_code == 422  # Expecting validation error for invalid email
```
