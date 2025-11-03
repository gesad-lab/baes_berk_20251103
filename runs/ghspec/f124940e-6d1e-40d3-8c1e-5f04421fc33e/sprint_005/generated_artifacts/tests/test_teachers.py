```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is instantiated in src/main.py

client = TestClient(app)

def test_create_teacher():
    """Test creating a new teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert "id" in response.json()  # Check if an id is returned for the created teacher

def test_get_teacher():
    """Test retrieving information for a specific teacher by ID."""
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1  # Assuming a teacher with ID 1 exists
    assert "name" in response.json()  # Ensure name information is included

def test_get_all_teachers():
    """Test the endpoint that retrieves all teachers."""
    response = client.get("/teachers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Check if the output is a list
    assert len(response.json()) > 0  # Ensure there is at least one teacher in the list

def test_create_teacher_missing_fields():
    """Test creating a teacher without required fields."""
    response = client.post("/teachers", json={"email": "john@example.com"})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"  # Check for expected error code
    assert "message" in response.json()["error"]  # Ensure a message is present to explain the error
```