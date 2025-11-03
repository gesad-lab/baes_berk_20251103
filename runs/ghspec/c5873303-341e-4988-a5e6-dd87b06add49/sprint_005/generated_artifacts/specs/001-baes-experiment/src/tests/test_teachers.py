```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Teacher
from src.database import get_db
from sqlalchemy.orm import sessionmaker

# Test client for the FastAPI application
client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    """Fixture that sets up a database session for testing."""
    db = get_db()
    yield db
    db.rollback()
    db.close()

@pytest.fixture(scope="module")
def create_teacher(db_session):
    """Fixture to create a teacher for testing."""
    teacher_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = client.post("/teachers", json=teacher_data)
    assert response.status_code == 201
    return response.json()

def test_create_teacher(db_session):
    """Test the creation of a new teacher."""
    teacher_data = {
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
    response = client.post("/teachers", json=teacher_data)
    
    # Ensure that the teacher is successfully created
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == teacher_data["name"]
    assert response.json()["email"] == teacher_data["email"]

def test_retrieve_teachers(db_session, create_teacher):
    """Test retrieving the list of teachers."""
    response = client.get("/teachers")
    
    # Ensure that the list contains the created teacher
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(teacher["email"] == create_teacher["email"] for teacher in response.json())

def test_create_teacher_without_name(db_session):
    """Test creating a teacher without a name should return an error."""
    teacher_data = {
        "email": "missing.name@example.com"
    }
    response = client.post("/teachers", json=teacher_data)
    
    # Expecting a Bad Request response due to missing name
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required fields: name",
            "details": {}
        }
    }

def test_create_teacher_without_email(db_session):
    """Test creating a teacher without an email should return an error."""
    teacher_data = {
        "name": "Missing Email"
    }
    response = client.post("/teachers", json=teacher_data)
    
    # Expecting a Bad Request response due to missing email
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required fields: email",
            "details": {}
        }
    }

def test_create_teacher_with_duplicate_email(db_session, create_teacher):
    """Test creating a teacher with a duplicate email should return an error."""
    teacher_data = {
        "name": "Duplicate Email",
        "email": create_teacher["email"]  # Using existing email
    }
    response = client.post("/teachers", json=teacher_data)
    
    # Expecting a Conflict response due to duplicate email
    assert response.status_code == 409
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email already exists",
            "details": {}
        }
    }
```