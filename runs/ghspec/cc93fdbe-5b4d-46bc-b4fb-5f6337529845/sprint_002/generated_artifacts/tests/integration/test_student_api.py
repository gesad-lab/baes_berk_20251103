```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student  # Assuming existing Student model is in models.py

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_db():
    """Setup the database for integration tests."""
    # Create the database schema
    Base.metadata.create_all(bind=engine)
    yield
    # Tear down the database
    Base.metadata.drop_all(bind=engine)

def test_create_student_success(setup_db):
    """Test successful creation of a student."""
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

def test_create_student_missing_email(setup_db):
    """Test creating a student without an email returns a validation error."""
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 422  # Unprocessable Entity

def test_create_student_invalid_email(setup_db):
    """Test creating a student with an invalid email format returns a validation error."""
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalidemail"})
    assert response.status_code == 422  # Unprocessable Entity

def test_get_student_success(setup_db):
    """Test fetching a student by ID."""
    # First create a student
    create_response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    student_id = create_response.json()["id"]

    # Now fetch the student
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

def test_get_student_not_found(setup_db):
    """Test fetching a student that does not exist returns 404."""
    response = client.get("/students/9999")  # Assuming 9999 does not exist
    assert response.status_code == 404  # Not Found
```