```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py

@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

def test_create_teacher(client):
    """Test creating a teacher successfully."""
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane.doe@example.com"

def test_get_teacher(client):
    """Test retrieving a teacher's details."""
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert "name" in response.json()
    assert "email" in response.json()

def test_update_teacher(client):
    """Test updating a teacher's information successfully."""
    response = client.put("/teachers/1", json={"name": "Jane Smith"})
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Smith"

def test_delete_teacher(client):
    """Test deleting a teacher."""
    response = client.delete("/teachers/1")
    assert response.status_code == 204

def test_create_teacher_validation(client):
    """Test validation for creating a teacher with missing fields."""
    response = client.post("/teachers", json={"name": "", "email": "missing.name@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name must not be empty", "details": {}}}

    response = client.post("/teachers", json={"name": "Missing Email", "email": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email must not be empty", "details": {}}}

    response = client.post("/teachers", json={"email": "no.name@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name must not be empty", "details": {}}}
```