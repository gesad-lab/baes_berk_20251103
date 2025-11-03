```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Set up necessary database state before tests."""
    # Set up database state here, such as creating necessary records
    yield
    # Clean up database state after tests

def test_create_teacher(setup_database):
    """Test creating a teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

def test_get_teacher(setup_database):
    """Test retrieving an existing teacher."""
    # Assuming teacher with ID 1 exists
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert "name" in response.json()
    assert response.json()["name"] == "John Doe"

def test_update_teacher(setup_database):
    """Test updating a teacher's information."""
    response = client.put("/teachers/1", json={"email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "john.doe@example.com"

def test_delete_teacher(setup_database):
    """Test deleting a teacher."""
    response = client.delete("/teachers/1")
    assert response.status_code == 204

def test_create_teacher_with_invalid_data(setup_database):
    """Test creating a teacher with invalid data."""
    response = client.post("/teachers", json={"name": "", "email": "invalid email"})
    assert response.status_code == 400
    assert "error" in response.json()
```