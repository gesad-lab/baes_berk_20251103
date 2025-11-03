```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_application.models import Base, Student  # Replace with your actual import
from your_application.main import app  # Replace with your actual import

DATABASE_URL = "sqlite:///./test.db"  # Use an in-memory database for tests
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    """Set up the database for testing."""
    Base.metadata.create_all(bind=engine)  # Create the tables
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)  # Clean up the database

@pytest.fixture(scope="module")
def client():
    """Fixture for the test client."""
    with TestClient(app) as client:
        yield client

def test_create_student_with_email(client, db):
    """Test creating a Student with a valid email."""
    response = client.post("/students/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "john@example.com"

def test_retrieve_student_details(client, db):
    """Test retrieving a Student's details including email."""
    response = client.post("/students/", json={"name": "Jane Doe", "email": "jane@example.com"})
    student_id = response.json()["id"]
    
    response = client.get(f"/students/{student_id}/")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane@example.com"

def test_create_student_without_email(client, db):
    """Test creating a Student without an email."""
    response = client.post("/students/", json={"name": "Missing Email"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email is required"}

def test_create_student_with_invalid_email_format(client, db):
    """Test creating a Student with an invalid email format."""
    response = client.post("/students/", json={"name": "Invalid Email", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email format is invalid"}
```