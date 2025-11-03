import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py


@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client


def test_create_student(client):
    """Test creating a new student."""
    response = client.post("/api/v1/students", json={"name": "John Doe", "age": 20})
    
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"


def test_get_student(client):
    """Test fetching a student by ID."""
    # First create a student
    create_response = client.post("/api/v1/students", json={"name": "Jane Doe", "age": 22})
    student_id = create_response.json()["id"]
    
    # Then fetch the student
    response = client.get(f"/api/v1/students/{student_id}")
    
    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert response.json()["name"] == "Jane Doe"


def test_update_student(client):
    """Test updating an existing student's information."""
    create_response = client.post("/api/v1/students", json={"name": "Alice", "age": 25})
    student_id = create_response.json()["id"]
    
    update_response = client.put(f"/api/v1/students/{student_id}", json={"name": "Alice Smith", "age": 26})
    
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Alice Smith"


def test_delete_student(client):
    """Test deleting a student."""
    create_response = client.post("/api/v1/students", json={"name": "Bob", "age": 23})
    student_id = create_response.json()["id"]
    
    delete_response = client.delete(f"/api/v1/students/{student_id}")
    
    assert delete_response.status_code == 204  # No Content
    # Verify the student was deleted
    fetch_response = client.get(f"/api/v1/students/{student_id}")
    assert fetch_response.status_code == 404  # Not Found


def test_create_student_invalid_data(client):
    """Test creating a student with invalid data."""
    response = client.post("/api/v1/students", json={"name": "", "age": -1})
    
    assert response.status_code == 400  # Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Invalid input data",
            "details": {"name": "Name cannot be empty", "age": "Age must be a positive number"}
        }
    }