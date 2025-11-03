```python
# tests/test_teacher.py

import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is defined in src/main.py
from src.database import init_db

@pytest.fixture
def client():
    """Fixture for FastAPI test client."""
    init_db()  # Initialize the database with tables
    with TestClient(app) as c:
        yield c

def test_create_teacher_success(client):
    """Test successful creation of a Teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()  # Check that the response contains an id
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_teacher_missing_name(client):
    """Test creation with missing name field."""
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required.",
            "details": {}
        }
    }

def test_create_teacher_missing_email(client):
    """Test creation with missing email field."""
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Email is required.",
            "details": {}
        }
    }

def test_create_teacher_missing_both_fields(client):
    """Test creation with both name and email fields missing."""
    response = client.post("/teachers", json={})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name and Email are required.",
            "details": {}
        }
    }

def test_verify_teacher_data_integrity(client):
    """Test retrieval of the created Teacher's information."""
    create_response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    teacher_id = create_response.json()["id"]

    retrieve_response = client.get(f"/teachers/{teacher_id}")
    assert retrieve_response.status_code == 200
    assert retrieve_response.json()["name"] == "Jane Doe"
    assert retrieve_response.json()["email"] == "jane.doe@example.com"
```