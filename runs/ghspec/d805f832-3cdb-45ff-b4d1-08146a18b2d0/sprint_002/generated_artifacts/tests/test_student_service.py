```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student  # Assuming a models.py defines the Student model and Base for SQLAlchemy
from main import app, get_db  # Assume the FastAPI app is in main.py with a dependency for db session

# Setting up the test database and FastAPI client
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database and the tables
Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_student_with_email():
    # Test creating a student with valid data
    response = client.post(
        "/students",
        json={"name": "John Doe", "email": "john.doe@example.com"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_create_student_without_email():
    # Test creating a student without an email
    response = client.post(
        "/students",
        json={"name": "Jane Doe"}
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()

def test_create_student_with_invalid_email():
    # Test creating a student with an invalid email
    response = client.post(
        "/students",
        json={"name": "Invalid Email", "email": "invalid_email_format"}
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()

def test_retrieve_student_by_id():
    # First, create a student to retrieve
    creation_response = client.post(
        "/students",
        json={"name": "Alice", "email": "alice@example.com"}
    )
    student_id = creation_response.json()["id"]

    # Now retrieve the student using the ID
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert data["id"] == student_id

# Note: This testing structure ensures that each function test observes isolation with a clean state.
# Additional tests could be added for further coverage based on functional requirements.
```