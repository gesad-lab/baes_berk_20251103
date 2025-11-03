import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in src/main.py
from src.models import Student  # Assuming your SQLAlchemy model is defined in src/models.py
from sqlalchemy.orm import Session
from src.database import get_db  # Assuming you have a dependency that provides a database session

@pytest.fixture
def client():
    """Fixture for the test client."""
    with TestClient(app) as client:
        yield client

@pytest.fixture
def sample_student():
    """Fixture to create a sample student for testing."""
    return {"name": "John Doe", "email": "john.doe@example.com"}

def test_create_student_with_email(client, sample_student):
    """Test creating a new student with an email."""
    response = client.post("/students/", json=sample_student)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == sample_student["name"]
    assert data["email"] == sample_student["email"]

def test_retrieve_student_details(client, sample_student):
    """Test retrieving a student's details including email."""
    # First, create a student
    response = client.post("/students/", json=sample_student)
    student_id = response.json()["id"]

    # Retrieve the student details
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == sample_student["name"]
    assert data["email"] == sample_student["email"]

def test_create_student_without_email(client):
    """Test creating a student without providing an email."""
    student_data = {"name": "Jane Doe"}
    response = client.post("/students/", json=student_data)
    
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "email"], "msg": "field required", "type": "value_error.missing"}]}

def test_create_student_with_invalid_email(client):
    """Test creating a student with an invalid email format."""
    student_data = {"name": "Invalid Email", "email": "invalid-email"}
    response = client.post("/students/", json=student_data)
    
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "email"], "msg": "value is not a valid email address", "type": "value_error.email"}]}