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
    """Test creating a new student with a valid email."""
    response = client.post("/api/v1/students", json={"name": "John Doe", "age": 20, "email": "john.doe@example.com"})
    
    assert response.status_code == 201
    assert response.json()["email"] == "john.doe@example.com"
    assert response.json()["name"] == "John Doe"
    assert "id" in response.json()  # Assuming id is generated


def test_create_student_with_invalid_email(client):
    """Test creating a new student with an invalid email."""
    response = client.post("/api/v1/students", json={"name": "Jane Doe", "age": 22, "email": "invalid-email"})
    
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format."}}


def test_update_student_email(client):
    """Test updating a student's email."""
    # First, create a student to update
    response = client.post("/api/v1/students", json={"name": "John Doe", "age": 20, "email": "john.doe@example.com"})
    student_id = response.json()["id"]
    
    # Now, update the email
    response = client.put(f"/api/v1/students/{student_id}", json={"email": "john.new@example.com"})
    
    assert response.status_code == 200
    assert response.json()["email"] == "john.new@example.com"


def test_update_student_with_invalid_email(client):
    """Test updating a student's email with an invalid email."""
    # Create a student to update
    response = client.post("/api/v1/students", json={"name": "John Doe", "age": 20, "email": "john.doe@example.com"})
    student_id = response.json()["id"]

    # Try to update with an invalid email
    response = client.put(f"/api/v1/students/{student_id}", json={"email": "invalid-email"})
    
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format."}}
```