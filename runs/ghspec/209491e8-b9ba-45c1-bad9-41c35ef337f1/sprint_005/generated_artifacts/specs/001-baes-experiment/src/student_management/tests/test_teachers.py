import pytest
from fastapi.testclient import TestClient
from src.main import app 
from src.models import Teacher  # Assuming we define the Teacher model in models.py
from src.schemas import TeacherCreate  # Assuming we define Pydantic schema for teacher creation


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_create_teacher_with_valid_data(client):
    """Test creating a teacher with valid data."""
    teacher_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = client.post("/teachers", json=teacher_data)
    
    assert response.status_code == 201  # Expect 201 Created
    assert response.json()["name"] == teacher_data["name"]
    assert response.json()["email"] == teacher_data["email"]


def test_create_teacher_missing_required_fields(client):
    """Test creating a teacher without required fields returns an error."""
    # Missing name
    teacher_data = {
        "email": "john.doe@example.com"
    }
    response = client.post("/teachers", json=teacher_data)
    
    assert response.status_code == 422  # Expect 422 Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"  # Check for specific validation message

    # Missing email
    teacher_data = {
        "name": "John Doe"
    }
    response = client.post("/teachers", json=teacher_data)

    assert response.status_code == 422  # Expect 422 Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"  # Check for specific validation message


def test_retrieve_teacher(client):
    """Test retrieving a teacher by valid ID."""
    # First create a teacher to retrieve them
    teacher_data = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
    response = client.post("/teachers", json=teacher_data)
    teacher_id = response.json()["id"]
    
    # Now retrieve the teacher
    response = client.get(f"/teachers/{teacher_id}")
    
    assert response.status_code == 200  # Expect 200 OK
    assert response.json()["name"] == teacher_data["name"]
    assert response.json()["email"] == teacher_data["email"]


def test_retrieve_teacher_not_found(client):
    """Test retrieving a teacher that does not exist returns a 404."""
    response = client.get("/teachers/999")  # 999 is assumed to be a non-existent ID
    assert response.status_code == 404  # Expect 404 Not Found
    assert response.json()["detail"] == "Teacher not found"  # Check error message