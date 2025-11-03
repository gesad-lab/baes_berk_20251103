```python
import pytest
from fastapi.testclient import TestClient
from src.api import app  # Import your FastAPI app instance

@pytest.fixture()
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

def test_create_student(client):
    """Test creating a student with a valid name."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_create_student_with_email(client):
    """Test creating a student with a valid name and email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "john@example.com"

def test_create_student_without_email(client):
    """Test creating a student without an email field."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email field is required."

def test_create_student_without_name(client):
    """Test creating a student without a name field."""
    response = client.post("/students", json={"email": "john@example.com"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Name field is required."
```