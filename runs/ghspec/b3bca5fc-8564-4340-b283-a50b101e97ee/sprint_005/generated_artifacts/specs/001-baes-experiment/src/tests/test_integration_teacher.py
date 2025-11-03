```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Teacher  # Import the relevant Teacher model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base  # Assuming there's a database module for the database setup

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_integration_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_client():
    """Fixture to create a test client."""
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def db():
    """Fixture to setup and teardown the database for testing."""
    Base.metadata.create_all(bind=engine)  # Create the database schema
    yield TestingSessionLocal()  # Provide the database session
    Base.metadata.drop_all(bind=engine)  # Clean up the database after tests

def test_create_teacher(test_client, db):
    """Test successful creation of a Teacher."""
    response = test_client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()  # Check if Teacher ID is included
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_retrieve_teacher(test_client, db):
    """Test retrieval of Teacher information."""
    # First, create a teacher to test retrieval
    create_response = test_client.post("/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    teacher_id = create_response.json()["id"]

    response = test_client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json()["id"] == teacher_id
    assert response.json()["name"] == "Jane Smith"
    assert response.json()["email"] == "jane.smith@example.com"

def test_create_teacher_missing_fields(test_client):
    """Test error handling for missing required fields."""
    # Test missing name
    response = test_client.post("/teachers", json={"email": "invalid.email@example.com"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"

    # Test missing email
    response = test_client.post("/teachers", json={"name": "Missing Email"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"

def test_create_teacher_duplicate_email(test_client, db):
    """Test error handling for duplicate email."""
    test_client.post("/teachers", json={"name": "Alice", "email": "alice@example.com"})
    response = test_client.post("/teachers", json={"name": "Bob", "email": "alice@example.com"})  # Same email
    assert response.status_code == 400  # Bad Request
    assert response.json()["detail"] == "Email already exists."
```