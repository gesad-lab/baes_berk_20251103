```python
# tests/test_teacher.py
import pytest
from fastapi.testclient import TestClient
from pydantic import BaseModel
from src.main import app  # Assuming FastAPI app is created in main.py
from src.services.teacher_service import TeacherService  # Assuming this service is implemented
from src.models.teacher import Teacher  # Assuming Teacher model is correctly implemented

client = TestClient(app)

class CreateTeacherRequest(BaseModel):
    name: str
    email: str

class CreateTeacherResponse(BaseModel):
    id: int
    name: str
    email: str

@pytest.fixture
def setup_db():
    # Placeholder for setting up test database state
    # This will typically include creating a temporary database and tables
    yield
    # Clean up database state after tests

def test_create_teacher(setup_db):
    """Test creating a new teacher with valid name and email."""
    response = client.post(
        "/teachers",
        json={"name": "John Doe", "email": "johndoe@example.com"}
    )
    
    assert response.status_code == 201
    teacher = CreateTeacherResponse(**response.json())
    assert teacher.name == "John Doe"
    assert teacher.email == "johndoe@example.com"

def test_create_teacher_missing_fields(setup_db):
    """Test creating a new teacher with missing fields."""
    response = client.post(
        "/teachers",
        json={"name": "John Doe"}  # Missing email
    )
    
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert any(field in response.json()["detail"][0]["msg"] for field in ["email"])


def test_create_teacher_invalid_email(setup_db):
    """Test creating a new teacher with invalid email format."""
    response = client.post(
        "/teachers",
        json={"name": "John Doe", "email": "invalid-email"}
    )
    
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert "value is not a valid email address" in response.json()["detail"][0]["msg"]

def test_retrieve_teacher_details(setup_db):
    """Test retrieving details of a teacher by ID."""
    # First create a teacher to retrieve
    create_response = client.post(
        "/teachers",
        json={"name": "John Doe", "email": "johndoe@example.com"}
    )
    teacher_id = create_response.json()["id"]

    # Now retrieve the teacher details
    response = client.get(f"/teachers/{teacher_id}")

    assert response.status_code == 200
    teacher = response.json()
    assert teacher["id"] == teacher_id
    assert teacher["name"] == "John Doe"
    assert teacher["email"] == "johndoe@example.com"
```