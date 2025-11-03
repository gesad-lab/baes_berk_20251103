```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import init_db, Base, SessionLocal
from src.models import Course, Student, Teacher  # Assuming Teacher model is defined in src/models.py
from src.api import app  # Assuming the FastAPI app is defined in src/api

DATABASE_URL = "sqlite:///./test.db"

# Create a new database engine for testing
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Set up the testing database
@pytest.fixture(scope="module")
def testing_db():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client(testing_db):
    with TestClient(app) as client:
        yield client

def test_create_teacher_success(client):
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"message": "Teacher created successfully."}

def test_create_teacher_missing_name(client):
    response = client.post("/teachers", json={"email": "jane.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name field is required."}}

def test_create_teacher_missing_email(client):
    response = client.post("/teachers", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email field is required."}}

def test_create_teacher_invalid_email_format(client):
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@invalid"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E003", "message": "Invalid email format."}}

def test_database_migration_verification(testing_db):
    # This test could be more elaborate if migration checks were implemented
    response = client.get("/migratestatus")
    assert response.status_code == 200
    # Ensure the Teacher table exists (pseudo db checking)
    # This part depends on your actual implementation of the migration check
```