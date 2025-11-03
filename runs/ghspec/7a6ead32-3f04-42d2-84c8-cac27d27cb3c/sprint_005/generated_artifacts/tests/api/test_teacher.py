```python
import json
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Teacher

@pytest.fixture
def client():
    """Fixture to create a test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

@pytest.fixture
def teacher(client):
    """Create a test teacher for the API tests."""
    response = client.post("/api/v1/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    assert response.status_code == 201  # Assert that the teacher was created successfully
    return response.json()  # Return the JSON response for further assertions

def test_get_teacher_by_id(client, teacher):
    """Test retrieving an existing teacher by ID."""
    response = client.get(f"/api/v1/teachers/{teacher['id']}")
    assert response.status_code == 200  # Check for successful retrieval
    data = response.json()
    assert data['id'] == teacher['id']  # Confirm the retrieved ID matches
    assert data['name'] == teacher['name']  # Confirm the retrieved name matches
    assert data['email'] == teacher['email']  # Confirm the retrieved email matches

def test_get_teacher_not_found(client):
    """Test retrieving a teacher with a non-existent ID."""
    response = client.get("/api/v1/teachers/99999")  # Assuming this ID does not exist
    assert response.status_code == 404  # Check for Not Found response
    assert response.json() == {"error": {"code": "E404", "message": "Teacher not found"}}  # Confirm error message
```