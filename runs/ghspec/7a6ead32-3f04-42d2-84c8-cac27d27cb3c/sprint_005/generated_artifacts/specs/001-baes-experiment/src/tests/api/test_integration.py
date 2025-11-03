import json
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Teacher

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture
def setup_teachers(client):
    """Create test data for teachers."""
    # Create a teacher for testing
    teacher_response = client.post("/api/v1/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    assert teacher_response.status_code == 201
    return teacher_response.json()

def test_create_teacher(client):
    """Test successful creation of a teacher."""
    response = client.post("/api/v1/teachers", json={"name": "Alice Johnson", "email": "alice.johnson@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Alice Johnson"
    assert response.json()["email"] == "alice.johnson@example.com"

def test_create_teacher_duplicate_email(client, setup_teachers):
    """Test creating a teacher with a duplicate email returns an error."""
    response = client.post("/api/v1/teachers", json={"name": "Bob Brown", "email": "jane.smith@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email must be unique.", "details": {}}}

def test_create_teacher_invalid_email(client):
    """Test creating a teacher with an invalid email returns an error."""
    response = client.post("/api/v1/teachers", json={"name": "Charlie Black", "email": "charlie.black@invalid"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format.", "details": {}}}

def test_get_teacher(client, setup_teachers):
    """Test retrieving a teacher by ID."""
    teacher_id = setup_teachers["id"]
    response = client.get(f"/api/v1/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json()["id"] == teacher_id
    assert response.json()["name"] == "Jane Smith"
    assert response.json()["email"] == "jane.smith@example.com"