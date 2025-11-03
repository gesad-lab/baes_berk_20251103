```python
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.models import Teacher

client = TestClient(app)

@pytest.fixture(scope="module")
def test_teachers():
    """Setup test teachers in the database before any tests run."""
    clear_and_seed_database_with_teachers()
    yield
    # Tear down test database cleanup
    clear_test_database()

def test_create_teacher_success(test_teachers):
    """Test successful creation of a teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_teacher_missing_fields(test_teachers):
    """Test error when trying to create a teacher with missing fields."""
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 400
    assert "error" in response.json()  # Check if error key exists
    assert response.json()["error"]["message"] == "Email is required."

def test_fetch_teacher_success(test_teachers):
    """Test fetching a teacher's information."""
    # Assuming the teacher created in the previous test now has an ID of 1
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_fetch_non_existent_teacher(test_teachers):
    """Test error response for fetching a non-existent teacher."""
    response = client.get("/teachers/999999")  # Arbitrary large ID that doesn't exist
    assert response.status_code == 404
    assert "error" in response.json()  # Check if error key exists
    assert response.json()["error"]["message"] == "Teacher not found."
```