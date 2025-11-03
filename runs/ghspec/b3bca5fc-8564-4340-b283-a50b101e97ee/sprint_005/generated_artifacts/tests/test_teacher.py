```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Teacher  # Import the Teacher model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base  # Assuming there's a database module for the database setup

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    with TestClient(app) as c:
        yield c

@pytest.fixture(autouse=True)
def db_session():
    """Create a new database session for each test."""
    # Mock the database session
    db = TestingSessionLocal()
    yield db
    db.close()

def test_create_teacher(client):
    """Test successful creation of a teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    
    assert response.status_code == 201  # Check for 201 Created
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_create_teacher_missing_name(client):
    """Test error response for missing name when creating a teacher."""
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    
    assert response.status_code == 400  # Check for Bad Request
    error_data = response.json()
    assert error_data["error"]["code"] == "E001"
    assert "name" in error_data["error"]["message"]

def test_create_teacher_missing_email(client):
    """Test error response for missing email when creating a teacher."""
    response = client.post("/teachers", json={"name": "John Doe"})
    
    assert response.status_code == 400  # Check for Bad Request
    error_data = response.json()
    assert error_data["error"]["code"] == "E001"
    assert "email" in error_data["error"]["message"]

def test_retrieve_teacher(client):
    """Test retrieving a teacher by ID."""
    create_response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    teacher_id = create_response.json()["id"]
    
    retrieve_response = client.get(f"/teachers/{teacher_id}")
    assert retrieve_response.status_code == 200  # Check for OK
    teacher_data = retrieve_response.json()
    assert teacher_data["id"] == teacher_id
    assert teacher_data["name"] == "John Doe"
    assert teacher_data["email"] == "john.doe@example.com"
```
