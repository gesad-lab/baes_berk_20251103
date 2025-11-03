```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app, get_db
from src.models import Base, Student  # Ensure the Student model is imported

# Setup the test database and client
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the test database
Base.metadata.create_all(bind=engine)

# Dependency override for the test database session
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the in-memory database for testing."""
    # Create a student to test retrieval
    student_data = {"name": "John Doe", "email": "john@example.com"}
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    yield  # Test using the set state
    # Any cleanup can be done here if needed

def test_retrieve_student_success(setup_database):
    """Test retrieving a student by ID."""
    # Assuming the first student created has an ID of 1
    response = client.get("/students/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"

def test_retrieve_non_existing_student():
    """Test retrieving a student that does not exist."""
    response = client.get("/students/999")  # Assuming 999 does not exist
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found."}  # Assuming this is the error message
```