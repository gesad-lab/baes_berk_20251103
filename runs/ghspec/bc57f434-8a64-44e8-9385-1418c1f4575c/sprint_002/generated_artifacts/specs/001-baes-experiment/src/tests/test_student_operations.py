```
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py
from src.models import Student  # Assuming a Student model exists in src/models.py

# Fixture to create a test client
@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_create_student_with_email(test_client):
    """Test creating a student with a valid email."""
    response = test_client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": response.json()["id"], "name": "John Doe", "email": "john.doe@example.com"}

def test_create_student_without_email(test_client):
    """Test creating a student without an email should raise a validation error."""
    response = test_client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert any("email" in error["loc"] for error in response.json()["detail"])

def test_create_student_with_invalid_email(test_client):
    """Test creating a student with an invalid email format should raise a validation error."""
    response = test_client.post("/students", json={"name": "Invalid Email", "email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert any("email" in error["loc"] for error in response.json()["detail"])

def test_get_student(test_client):
    """Test retrieving a student's details."""
    # Assuming a student with ID 1 exists
    response = test_client.get("/students/1")
    assert response.status_code == 200
    assert "name" in response.json() and "email" in response.json()

def test_update_student_email(test_client):
    """Test updating a student's email."""
    response = test_client.put("/students/1", json={"email": "new.email@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "new.email@example.com"
```