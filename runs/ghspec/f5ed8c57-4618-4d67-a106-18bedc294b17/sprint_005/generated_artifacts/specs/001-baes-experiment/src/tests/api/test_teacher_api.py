```python
import pytest
from fastapi.testclient import TestClient
from src.api.teacher_api import app  # Assuming the FastAPI instance for teacher management is in this module
from src.models import Teacher  # Import the Teacher model

client = TestClient(app)

# Test data setup for teacher testing
@pytest.fixture()
def create_teacher():
    response = client.post("/teachers", json={"name": "John Doe", "email": "johndoe@example.com"})
    return response.json()

def test_create_teacher():
    """Test ability to create a new teacher."""
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "janedoe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "janedoe@example.com"

def test_retrieve_teacher(create_teacher):
    """Test ability to retrieve a teacher by ID."""
    teacher_id = create_teacher["id"]
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "johndoe@example.com"

def test_update_teacher(create_teacher):
    """Test ability to update a teacher's information."""
    teacher_id = create_teacher["id"]
    response = client.put(f"/teachers/{teacher_id}", json={"name": "John Smith"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Smith"
    assert response.json()["email"] == "johndoe@example.com"  # Ensure email remains unchanged

def test_delete_teacher(create_teacher):
    """Test ability to delete a teacher."""
    teacher_id = create_teacher["id"]
    response = client.delete(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher deleted successfully."

    # Verify that the teacher no longer exists
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 404  # Not Found
```