```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.services import create_teacher, get_teacher, update_teacher, delete_teacher
from src.models import Teacher
from pydantic import BaseModel

@pytest.fixture(scope="module")
def test_client():
    """Create a test client for the FastAPI application."""
    client = TestClient(app)
    yield client

class TeacherCreate(BaseModel):
    name: str  # The name of the teacher
    email: str  # The email of the teacher

def test_create_teacher(test_client):
    """Test creating a teacher."""
    response = test_client.post("/teachers", json={"name": "Bob Brown", "email": "bob@school.com"})
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == "Bob Brown"
    assert data['email'] == "bob@school.com"

def test_get_teacher(test_client):
    """Test retrieving an existing teacher."""
    response = test_client.get("/teachers/1")  # Assuming teacher with ID 1 exists
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data['name'] == "Bob Brown"

def test_update_teacher(test_client):
    """Test updating a teacher's information."""
    response = test_client.put("/teachers/1", json={"email": "bob.brown@school.com"})
    assert response.status_code == 200
    data = response.json()
    assert data['email'] == "bob.brown@school.com"

def test_delete_teacher(test_client):
    """Test deleting a teacher."""
    response = test_client.delete("/teachers/1")
    assert response.status_code == 204  # No content on successful delete
   
def test_create_teacher_with_invalid_data(test_client):
    """Test creating a teacher with missing data."""
    response = test_client.post("/teachers", json={"name": ""})  # Missing email
    assert response.status_code == 400
    assert "error" in response.json()  # Check for error in response

def test_update_teacher_with_invalid_data(test_client):
    """Test updating a teacher with invalid data."""
    response = test_client.put("/teachers/1", json={"email": ""})  # Invalid email
    assert response.status_code == 400
    assert "error" in response.json()  # Check for error in response
```