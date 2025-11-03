import pytest
from fastapi.testclient import TestClient
from src.api import app  # Import your FastAPI app instance

@pytest.fixture()
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

def test_create_teacher(client):
    """Test creating a new teacher with valid data."""
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane@example.com"

def test_get_teacher(client):
    """Test retrieving a teacher's details by ID."""
    # Assuming a teacher with ID 1 exists, this may need to be modified based on your test setup
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert "name" in response.json()
    assert "email" in response.json()

def test_create_teacher_missing_fields(client):
    """Test creating a teacher without required fields throws an error."""
    response = client.post("/teachers", json={"name": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Name and email are required"

    response = client.post("/teachers", json={"email": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Name and email are required"

    response = client.post("/teachers", json={})
    assert response.status_code == 400
    assert response.json()["detail"] == "Name and email are required"