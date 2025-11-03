```python
# /tests/services/test_teacher_service.py

from fastapi.testclient import TestClient
import pytest
from src.api.teacher import app  # Assuming this is where the FastAPI app instance is defined
from models.teacher import Teacher  # Assuming Teacher is defined in models
from sqlalchemy.orm import Session
from database import get_db  # Assuming this is how we get a database session

client = TestClient(app)

# Mock database session fixture (setup and teardown as needed)
@pytest.fixture(scope="module")
def db_session():
    # Logic to create a temporary database session for testing goes here
    # Yield the session and ensure cleanup after tests
    pass

def test_create_teacher_success(db_session):
    """Test case for successfully creating a new teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Check for successful creation
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_retrieve_teacher_success(db_session):
    """Test case for retrieving teacher information by ID."""
    # Assuming a teacher with ID 1 exists from previous test
    response = client.get("/teachers/1")
    assert response.status_code == 200  # Check for successful retrieval
    data = response.json()
    assert data["id"] == 1  # Assuming the ID of the created teacher is 1
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_create_teacher_missing_fields(db_session):
    """Test case for handling errors when creating a teacher with missing fields."""
    response = client.post("/teachers", json={"name": "", "email": ""})
    assert response.status_code == 422  # Check for unprocessable entity
    assert response.json() == {
        "detail": [
            {"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"},
            {"loc": ["body", "email"], "msg": "field required", "type": "value_error.missing"}
        ]
    }
```