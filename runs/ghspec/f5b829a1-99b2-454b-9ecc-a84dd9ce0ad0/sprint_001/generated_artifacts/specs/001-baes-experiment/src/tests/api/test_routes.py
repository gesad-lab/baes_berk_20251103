```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app, get_db
from src.models import Base

# Setup the test database and client
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the test database
Base.metadata.create_all(bind=engine)

# Dependency override for the test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Use the FastAPI TestClient for sending requests
app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Integration tests for the API endpoints
def test_create_student_with_valid_name():
    response = client.post("/students/", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}

def test_create_student_missing_name():
    response = client.post("/students/", json={})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required.",
            "details": {}
        }
    }

def test_retrieve_student_by_id():
    # First, create a student
    response = client.post("/students/", json={"name": "Jane Doe"})
    student_id = response.json()["id"]
    
    # Now retrieve the student by ID
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == {"id": student_id, "name": "Jane Doe"}

def test_retrieve_student_with_non_existing_id():
    response = client.get("/students/9999")  # Assuming this ID does not exist
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Student not found.",
            "details": {}
        }
    }
```