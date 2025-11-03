```python
import pytest
from fastapi.testclient import TestClient
from main import app, get_database_connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student

# Set up the test database
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database schema
Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    """Provides an instance of the FastAPI test client."""
    with TestClient(app) as client:
        yield client

@pytest.fixture
def create_student(client):
    """Helper function to create a student for tests."""
    response = client.post(
        "/students/",
        json={"name": "John Doe", "email": "john.doe@example.com"}
    )
    return response.json()

def test_create_student_with_valid_email(client):
    """Test that creating a student with a valid email returns the expected JSON response."""
    response = client.post(
        "/students/",
        json={"name": "Jane Doe", "email": "jane.doe@example.com"}
    )
    assert response.status_code == 201
    assert "email" in response.json()
    assert response.json()["email"] == "jane.doe@example.com"

def test_create_student_with_invalid_email(client):
    """Test that creating a student with an invalid email returns a 400 status code."""
    response = client.post(
        "/students/",
        json={"name": "Invalid Email", "email": "invalid-email"}
    )
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}

def test_update_student_email(client, create_student):
    """Test updating a student's email to a valid one."""
    student_id = create_student["id"]
    response = client.put(
        f"/students/{student_id}",
        json={"name": "John Updated", "email": "john.updated@example.com"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "john.updated@example.com"

def test_update_student_with_invalid_email(client, create_student):
    """Test updating a student's email to an invalid one."""
    student_id = create_student["id"]
    response = client.put(
        f"/students/{student_id}",
        json={"name": "John Updated", "email": "invalid-email"}
    )
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}

def test_retrieve_student_with_email(client, create_student):
    """Test that retrieving a student returns the expected JSON response including email."""
    student_id = create_student["id"]
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert "email" in response.json()
    assert response.json()["email"] == create_student["email"]
```