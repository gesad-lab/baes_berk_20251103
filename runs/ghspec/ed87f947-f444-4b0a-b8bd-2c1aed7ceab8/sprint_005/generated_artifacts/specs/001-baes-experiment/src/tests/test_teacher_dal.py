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
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_get_teacher(client):
    """Test retrieving a teacher's details."""
    # First, create a teacher to test retrieval
    create_response = client.post("/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    teacher_id = create_response.json()["id"]
    
    get_response = client.get(f"/teachers/{teacher_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Jane Smith"
    assert get_response.json()["email"] == "jane.smith@example.com"

def test_update_teacher(client):
    """Test updating a teacher's information."""
    create_response = client.post("/teachers", json={"name": "Alice Johnson", "email": "alice.johnson@example.com"})
    teacher_id = create_response.json()["id"]
    
    update_response = client.put(f"/teachers/{teacher_id}", json={"name": "Alice M. Johnson"})
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Alice M. Johnson"

def test_delete_teacher(client):
    """Test deleting a teacher."""
    create_response = client.post("/teachers", json={"name": "Bob Brown", "email": "bob.brown@example.com"})
    teacher_id = create_response.json()["id"]
    
    delete_response = client.delete(f"/teachers/{teacher_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Teacher deleted successfully"

def test_create_teacher_with_missing_fields(client):
    """Test creating a teacher with missing name or email."""
    response = client.post("/teachers", json={"name": "", "email": "invalid.email@example.com"})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"
    assert "name" in response.json()["error"]["details"]
    
    response = client.post("/teachers", json={"name": "Valid Name", "email": ""})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"
    assert "email" in response.json()["error"]["details"]
```