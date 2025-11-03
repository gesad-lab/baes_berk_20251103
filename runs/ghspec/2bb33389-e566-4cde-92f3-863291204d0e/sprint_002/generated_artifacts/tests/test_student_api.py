```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from src.models import Base, Student  # Assuming the Student model is in src/models
from src.api import app  # Assuming the FastAPI app is defined in src/api

DATABASE_URL = "sqlite:///./test.db"

# Create a new database engine
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a new FastAPI app instance for testing
app = FastAPI()

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope='module', autouse=True)
def setup_database():
    # Create the database and the schema
    Base.metadata.create_all(bind=engine)
    yield  # This is where the testing happens
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

def test_create_student_with_email(test_client):
    """Test successful creation of a student with name and email."""
    response = test_client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}

def test_create_student_without_email(test_client):
    """Test validation error when email is missing."""
    response = test_client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email is required.", "details": {}}}

def test_get_students(test_client):
    """Test retrieving all students including emails."""
    test_client.post("/students", json={"name": "Alice Smith", "email": "alice@example.com"})
    test_client.post("/students", json={"name": "Bob Johnson", "email": "bob@example.com"})
    
    response = test_client.get("/students")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2  # Ensure two students are returned
    assert {"name": "Alice Smith", "email": "alice@example.com"} in data
    assert {"name": "Bob Johnson", "email": "bob@example.com"} in data
```