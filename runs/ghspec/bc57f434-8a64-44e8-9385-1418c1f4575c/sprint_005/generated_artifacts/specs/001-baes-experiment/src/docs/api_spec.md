---
File: tests/test_api_teachers.py
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_create_teacher_with_valid_data(test_client):
    """Test creating a teacher with valid name and email."""
    response = test_client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()  # Ensure ID is returned
    assert response.json()['name'] == "John Doe"
    assert response.json()['email'] == "john.doe@example.com"

def test_retrieve_teacher_with_invalid_id(test_client):
    """Test retrieving teacher details with an invalid ID."""
    invalid_id = 99999  # Assuming this ID does not exist
    response = test_client.get(f"/teachers/{invalid_id}")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Teacher not found", "details": {}}}

def test_create_teacher_without_required_fields(test_client):
    """Test creating a teacher without required fields returns validation errors."""
    response = test_client.post("/teachers", json={"name": "", "email": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E400", "message": "Validation failed", "details": {"name": ["field required"], "email": ["field required"]}}}

def test_create_teacher_with_duplicate_email(test_client):
    """Test creating a teacher with a duplicate email returns an error."""
    # First create a teacher
    test_client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    # Attempt to create another teacher with the same email
    response = test_client.post("/teachers", json={"name": "Jane Smith", "email": "jane.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E400", "message": "Email already exists", "details": {}}}
```
---