```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Main FastAPI application
from src.models import TeacherCreate  # Import the TeacherCreate model

client = TestClient(app)

# Integration tests for the teacher API endpoints
@pytest.mark.integration
def test_create_teacher_with_valid_data():
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Check for successful creation
    response_data = response.json()
    assert response_data["name"] == "John Doe"
    assert response_data["email"] == "john.doe@example.com"

@pytest.mark.integration
def test_create_teacher_without_name():
    """Test creating a teacher without a name should return an error."""
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400  # Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required"
        }
    }

@pytest.mark.integration
def test_create_teacher_without_email():
    """Test creating a teacher without an email should return an error."""
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 400  # Bad Request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email is required"
        }
    }

@pytest.mark.integration
def test_list_teachers():
    """Test retrieving the list of teachers."""
    response = client.get("/teachers")
    assert response.status_code == 200  # Successful retrieval
    response_data = response.json()
    assert isinstance(response_data, list)  # Should return a list
    # Optionally check for the presence of expected teacher if previously created
    assert len(response_data) >= 0  # There might be 0 or more teachers at this point
```