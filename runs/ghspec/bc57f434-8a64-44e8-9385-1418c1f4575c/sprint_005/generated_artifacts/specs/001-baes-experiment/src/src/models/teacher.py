```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_create_teacher(test_client):
    """Test creating a teacher."""
    response = test_client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_create_teacher_duplicate_email(test_client):
    """Test creating a teacher with a duplicate email."""
    # Create the first teacher
    test_client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    # Attempt to create another teacher with the same email
    response = test_client.post("/teachers", json={"name": "John Smith", "email": "jane.doe@example.com"})
    assert response.status_code == 409
    assert response.json() == {"error": {"code": "E002", "message": "Email already exists."}}

def test_get_teacher_details(test_client):
    """Test retrieving teacher details by ID."""
    response = test_client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_get_teacher_not_found(test_client):
    """Test retrieving a teacher that does not exist."""
    response = test_client.get("/teachers/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Teacher not found."}}
```