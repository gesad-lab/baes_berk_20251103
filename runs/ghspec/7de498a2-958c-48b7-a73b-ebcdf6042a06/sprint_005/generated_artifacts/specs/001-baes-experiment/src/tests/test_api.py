```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Set up any necessary database state before tests
    yield
    # Clean up database state after tests

def test_create_teacher_success(setup_database):
    """Test that creating a teacher successfully returns the created object."""
    response = client.post("/teachers", json={"name": "Alice Smith", "email": "alice@school.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Alice Smith"
    assert response.json()["email"] == "alice@school.com"

def test_get_teacher_success(setup_database):
    """Test that retrieving a teacher by ID returns the correct details."""
    response = client.get("/teachers/1")  # Assuming teacher with ID 1 exists
    assert response.status_code == 200
    assert "name" in response.json()
    assert "email" in response.json()

def test_create_teacher_invalid_data(setup_database):
    """Test that providing invalid data when creating a teacher returns an error."""
    response = client.post("/teachers", json={"name": "", "email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"]
    assert any("value should not be blank" in error["msg"] for error in response.json()["detail"])
```