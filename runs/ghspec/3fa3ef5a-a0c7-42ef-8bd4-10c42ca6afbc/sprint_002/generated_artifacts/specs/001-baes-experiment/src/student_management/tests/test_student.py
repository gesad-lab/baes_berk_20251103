import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.database.db import SessionLocal

@pytest.fixture(scope="module")
def test_client():
    """Fixture for FastAPI test client."""
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def db_session():
    """Fixture to provide a database session for testing."""
    db = SessionLocal()
    yield db
    db.close()

def test_create_student_with_valid_data(test_client):
    """Test student creation with valid name and email."""
    response = test_client.post("/students/", json={"name": "Test Student", "email": "test@student.com"})
    assert response.status_code == 201
    assert response.json() == {"message": "Student created successfully", "student": {"name": "Test Student", "email": "test@student.com"}}

def test_create_student_with_missing_email(test_client):
    """Test student creation with missing email."""
    response = test_client.post("/students/", json={"name": "Test Student"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email is required", "details": {}}}

def test_create_student_with_invalid_email(test_client):
    """Test student creation with invalid email format."""
    response = test_client.post("/students/", json={"name": "Test Student", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid email format", "details": {}}}

def test_get_student_with_email(test_client):
    """Test retrieval of student data including email."""
    response = test_client.get("/students/1")  # Assuming the student ID is 1
    assert response.status_code == 200
    assert "email" in response.json()
    assert response.json()["email"] == "test@student.com"  # Match the email of the created student

def test_create_student_duplicate_email(test_client):
    """Test creating a student with a duplicate email address."""
    response = test_client.post("/students/", json={"name": "Another Student", "email": "test@student.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E003", "message": "Email already exists", "details": {}}}