```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is initialized in `main.py`
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from models import Course, Student, StudentCourse, Teacher  # Import the Teacher model
import json

# Initialize the test client
client = TestClient(app)

# Setup a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database and tables
def init_db():
    Base.metadata.create_all(bind=engine)

def drop_db():
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def test_app():
    init_db()
    yield client  # This is where the testing happens
    drop_db()

def test_create_teacher(test_app):
    # Example payload for creating a teacher
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = test_app.post("/teachers/", json=payload)
    assert response.status_code == 201  # Check for creation success
    assert response.json()["name"] == payload["name"]
    assert response.json()["email"] == payload["email"]

def test_create_teacher_missing_fields(test_app):
    # Example payload with missing fields
    payload = {
        "name": ""
    }
    response = test_app.post("/teachers/", json=payload)
    assert response.status_code == 422  # Check for validation error

def test_get_teacher(test_app):
    # First, create a teacher to test retrieval
    create_payload = {
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
    create_response = test_app.post("/teachers/", json=create_payload)
    teacher_id = create_response.json()["id"]

    # Now retrieve the created teacher
    response = test_app.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json()["name"] == create_payload["name"]
    assert response.json()["email"] == create_payload["email"]

def test_get_teacher_not_found(test_app):
    # Test retrieving a non-existing teacher
    response = test_app.get("/teachers/999")
    assert response.status_code == 404  # Check for not found error
    assert response.json()["detail"] == "Teacher not found"
```