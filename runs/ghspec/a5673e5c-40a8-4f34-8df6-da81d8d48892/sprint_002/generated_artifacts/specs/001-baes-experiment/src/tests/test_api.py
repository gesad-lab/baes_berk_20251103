# Assuming the file is empty as no existing content was provided. We will create unit tests for the FastAPI application in `test_api.py`.

import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.schemas import StudentCreate
from src.models import Student

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Sets up the database for testing."""
    # Assuming that you have a function to create the database schema.
    from src.models import Base, engine
    Base.metadata.create_all(engine)
    yield
    # Clean up: Drop all tables after tests are done
    Base.metadata.drop_all(engine)

def test_create_student_with_valid_email():
    """Test creating a student with a valid email."""
    response = client.post("/students/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "john@example.com"

def test_create_student_with_invalid_email():
    """Test that creating a student with an invalid email returns a validation error."""
    response = client.post("/students/", json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"

def test_retrieve_student():
    """Test retrieving a student by ID."""
    # Assuming the student with ID 1 exists
    response = client.get("/students/1")
    assert response.status_code == 200
    assert "email" in response.json()

def test_update_student_email():
    """Test updating an existing student's email."""
    response = client.put("/students/1", json={"email": "new_email@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "new_email@example.com"

def test_update_student_email_with_invalid_email():
    """Test that updating a student's email with an invalid format returns a validation error."""
    response = client.put("/students/1", json={"email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"