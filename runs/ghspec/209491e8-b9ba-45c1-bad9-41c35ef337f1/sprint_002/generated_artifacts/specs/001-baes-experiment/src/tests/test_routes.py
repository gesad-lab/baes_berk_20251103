import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming app is imported from main.py
from src.models import Student  # Import the Student model
from src.database import get_db  # Import the database session

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture
def setup_database():
    # Setup code for database goes here, e.g., creating test records
    # Ensure the test database is clean before each test or use a fixture to handle that
    pass

def test_create_student_success(client, setup_database):
    """Test successful student creation with name and email."""
    response = client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_create_student_missing_email(client, setup_database):
    """Test student creation returns error for missing email."""
    response = client.post("/students/", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email is required.", "details": {}}}

def test_create_student_invalid_email(client, setup_database):
    """Test student creation returns error for invalid email format."""
    response = client.post("/students/", json={"name": "Jane Doe", "email": "not_an_email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid email format.", "details": {}}}

def test_get_students_success(client, setup_database):
    """Test retrieval of students returns list with names and emails."""
    # First, create a student
    client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    client.post("/students/", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    
    response = client.get("/students/")
    assert response.status_code == 200
    students = response.json()
    assert len(students) == 2
    assert any(student["name"] == "John Doe" and student["email"] == "john.doe@example.com" for student in students)
    assert any(student["name"] == "Jane Doe" and student["email"] == "jane.doe@example.com" for student in students)

# Ensure to handle cleanup of test database if needed
# If using a testing database, ensure proper teardown to not affect other tests
