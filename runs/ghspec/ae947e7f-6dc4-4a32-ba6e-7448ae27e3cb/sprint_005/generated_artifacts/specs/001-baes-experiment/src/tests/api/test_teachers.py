```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_create_teacher_with_valid_data(client):
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200  # 200 OK
    assert response.json() == {"message": "Teacher created successfully."}

def test_create_teacher_with_missing_name(client):
    """Test creating a teacher with a missing name field."""
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Name and email fields are required."}}

def test_create_teacher_with_missing_email(client):
    """Test creating a teacher with a missing email field."""
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Name and email fields are required."}}

def test_create_teacher_with_duplicate_email(client):
    """Test creating a teacher with a duplicate email."""
    client.post("/teachers", json={"name": "Jane Doe", "email": "john.doe@example.com"})
    response = client.post("/teachers", json={"name": "John Smith", "email": "john.doe@example.com"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {"error": {"code": "E002", "message": "Email address already in use."}}

def test_get_teacher(client):
    """Test getting a teacher's details."""
    # Setup by creating a teacher first
    client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    response = client.get("/teachers/1")
    assert response.status_code == 200  # 200 OK
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_get_teacher_with_invalid_id(client):
    """Test getting a teacher with an invalid ID."""
    response = client.get("/teachers/999")  # Assuming 999 does not exist
    assert response.status_code == 404  # 404 Not Found
    assert response.json() == {"error": {"code": "E003", "message": "Teacher not found."}}
```