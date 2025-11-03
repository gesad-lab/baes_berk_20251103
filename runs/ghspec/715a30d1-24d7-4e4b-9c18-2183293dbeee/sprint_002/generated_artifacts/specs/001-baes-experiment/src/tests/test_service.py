```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is initialized in `main.py`
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from models import Student

# Initialize the test client
client = TestClient(app)

# Setup a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database structure before tests
def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    # Clean up database after tests
    Base.metadata.drop_all(bind=engine)

# Dependency override
app.dependency_overrides[get_db] = lambda: SessionLocal()

def test_create_student_with_email():
    """Test that creating a student with valid name and email works."""
    response = client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"name": "John Doe", "email": "john.doe@example.com"}

def test_create_student_without_email():
    """Test that creating a student without an email returns an error."""
    response = client.post("/students/", json={"name": "Jane Doe"})
    assert response.status_code == 422  # Expecting validation error
    assert response.json() == {
        "detail": [{"loc": ["body", "email"], "msg": "field required", "type": "value_error.missing"}]}

def test_retrieve_student_email():
    """Test that retrieving a student's details by ID returns the correct email."""
    # First, create a student to retrieve
    client.post("/students/", json={"name": "Alice Smith", "email": "alice.smith@example.com"})
    
    # Assuming the id of the newly created student is 1
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Alice Smith", "email": "alice.smith@example.com"}
```