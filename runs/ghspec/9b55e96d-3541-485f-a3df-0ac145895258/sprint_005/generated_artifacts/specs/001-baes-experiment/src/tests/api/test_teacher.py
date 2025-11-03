from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base
from models import Teacher

# Create a new FastAPI instance
app = FastAPI()

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Use an in-memory database for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency
@app.dependency_overrides[get_db]
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include the router
from app.api.teacher import router as teacher_router
app.include_router(teacher_router)

# Create the database tables for testing
Base.metadata.create_all(bind=engine)

# Set up the test client
client = TestClient(app)

# Test cases for Teacher functionality
def test_create_teacher_success():
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"message": "Teacher created successfully", "teacher_id": 1}

def test_create_teacher_missing_fields():
    response = client.post("/teachers", json={"name": "", "email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name and email are required fields."}}

def test_create_teacher_duplicate_email():
    client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})  # Create the teacher first
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "john.doe@example.com"})
    assert response.status_code == 409
    assert response.json() == {"error": {"code": "E002", "message": "Email already exists."}}

def test_get_teacher_success():
    client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})  # Create the teacher first
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_get_teacher_not_found():
    response = client.get("/teachers/999")  # Teacher ID that doesn't exist
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Teacher not found."}}