```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Importing main FastAPI application
from src.models import TeacherCreate  # Importing TeacherCreate model

client = TestClient(app)

# Integration tests for the teacher API endpoints
@pytest.mark.integration
def test_create_teacher_with_valid_data():
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    
    assert response.status_code == 201  # Expecting 201 Created
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

@pytest.mark.integration
def test_create_teacher_without_name():
    """Test creating a teacher without a name."""
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    
    assert response.status_code == 400  # Expecting 400 Bad Request
    error = response.json()
    assert error["error"]["code"] == "E001"
    assert error["error"]["message"] == "Name is required"

@pytest.mark.integration
def test_create_teacher_with_invalid_email():
    """Test creating a teacher with an invalid email format."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "invalid-email"})
    
    assert response.status_code == 400  # Expecting 400 Bad Request
    error = response.json()
    assert error["error"]["code"] == "E002"
    assert error["error"]["message"] == "Invalid email format"

@pytest.mark.integration
def test_list_teachers():
    """Test retrieving a list of all teachers."""
    response = client.get("/teachers")
    
    assert response.status_code == 200  # Expecting 200 OK
    data = response.json()
    assert isinstance(data, list)  # Expecting a list
    # Further validation can be done depending on the state of the database
```