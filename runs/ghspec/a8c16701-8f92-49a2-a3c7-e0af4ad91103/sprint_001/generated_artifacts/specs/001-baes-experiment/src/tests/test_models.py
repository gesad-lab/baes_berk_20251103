import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Student
from src.api import app  # Assuming your FastAPI app is defined in api.py
from src.db import get_db

# Create a new SQLite database in memory for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
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

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Create a new database session for each test
    Base.metadata.create_all(bind=engine)  # Create tables before each test
    yield  # Run the tests
    # Teardown: Drop all tables after tests
    Base.metadata.drop_all(bind=engine)

def test_create_student():
    # Test POST /students
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}

def test_get_student():
    # Create a student to retrieve
    response = client.post("/students", json={"name": "Jane Doe"})
    student_id = response.json()["id"]
    
    # Test GET /students/{id}
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == {"id": student_id, "name": "Jane Doe"}

def test_get_non_existent_student():
    # Test GET /students/{id} for a non-existent student
    response = client.get("/students/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found."}

def test_create_student_without_name():
    # Test POST /students with missing name
    response = client.post("/students", json={})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"