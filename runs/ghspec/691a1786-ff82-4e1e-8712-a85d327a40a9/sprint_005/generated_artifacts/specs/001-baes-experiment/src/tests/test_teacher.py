```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.teacher import Teacher
from src.db.database import get_db
from sqlalchemy.orm import Session

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def test_db():
    # Setup code for initializing the database
    # Ideally, this would include population with dummy data for testing...
    pass

def test_create_teacher(test_client):
    # Test creating a new teacher
    response = test_client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["data"]["name"] == "John Doe"
    assert response.json()["data"]["email"] == "john.doe@example.com"

def test_get_teacher(test_client):
    # Create a teacher first
    create_response = test_client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    teacher_id = create_response.json()["data"]["id"]
    
    # Test retrieving the created teacher
    response = test_client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == teacher_id
    assert response.json()["data"]["name"] == "Jane Doe"

def test_get_teacher_not_found(test_client):
    # Test retrieving a non-existing teacher
    response = test_client.get("/teachers/99999")  # Assuming 99999 is an invalid ID
    assert response.status_code == 404

def test_update_teacher(test_client):
    # Create a teacher to be updated
    create_response = test_client.post("/teachers", json={"name": "Alice", "email": "alice@example.com"})
    teacher_id = create_response.json()["data"]["id"]
    
    # Test updating the teacher's information
    update_response = test_client.put(f"/teachers/{teacher_id}", json={"name": "Alice Smith"})
    assert update_response.status_code == 200
    assert update_response.json()["data"]["name"] == "Alice Smith"
    assert update_response.json()["data"]["email"] == "alice@example.com"

def test_delete_teacher(test_client):
    # Create a teacher first for deletion
    create_response = test_client.post("/teachers", json={"name": "Bob", "email": "bob@example.com"})
    teacher_id = create_response.json()["data"]["id"]
    
    # Test deleting the teacher
    delete_response = test_client.delete(f"/teachers/{teacher_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Teacher deleted successfully."

def test_delete_teacher_not_found(test_client):
    # Test deleting a non-existing teacher
    response = test_client.delete("/teachers/99999")  # Assuming 99999 is an invalid ID
    assert response.status_code == 404
```