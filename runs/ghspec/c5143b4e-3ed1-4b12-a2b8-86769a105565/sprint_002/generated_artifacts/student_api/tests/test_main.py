import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import get_db, Base
from src.main import app, Student

# Create an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency override for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Set up the test client
client = TestClient(app)

# Test case for creating a student with valid name and email
def test_create_student_with_email():
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Expect created status
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

# Test case for retrieving students
def test_retrieve_students():
    response = client.get("/students")
    assert response.status_code == 200  # Expect success status
    data = response.json()
    assert isinstance(data, list)  # Expect a list of students

# Test case for creating a student without email
def test_create_student_without_email():
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 422  # Expect unprocessable entity
    error_response = response.json()
    assert "detail" in error_response  # Check for validation error details
    assert len(error_response["detail"]) > 0  # Ensure there's at least one validation error

# Test case for creating a student with invalid email format
def test_create_student_with_invalid_email():
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalid-email"})
    assert response.status_code == 422  # Expect unprocessable entity
    error_response = response.json()
    assert "detail" in error_response  # Check for validation error details
    assert len(error_response["detail"]) > 0  # Ensure there's at least one validation error

# Test case for creating a student without a name (assuming name is also required)
def test_create_student_without_name():
    response = client.post("/students", json={"email": "valid.email@example.com"})
    assert response.status_code == 422  # Expect unprocessable entity
    error_response = response.json()
    assert "detail" in error_response  # Check for validation error details
    assert len(error_response["detail"]) > 0  # Ensure there's at least one validation error