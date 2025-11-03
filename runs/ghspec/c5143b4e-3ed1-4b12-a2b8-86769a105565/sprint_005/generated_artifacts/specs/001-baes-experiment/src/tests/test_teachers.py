```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.schemas import TeacherCreate
from sqlalchemy.exc import IntegrityError
from src.database import get_db
from src.models import Teacher

client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    yield client

@pytest.fixture(scope="module")
def db_session():
    # Setup code for creating a test database session or use test DB functionalities
    pass  # Ensure to implement session management if needed

def test_create_teacher_success(test_client, db_session):
    """Test successful creation of a Teacher."""
    teacher_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    response = test_client.post("/teachers", json=teacher_data)
    
    assert response.status_code == 201
    assert response.json()["name"] == teacher_data["name"]
    assert response.json()["email"] == teacher_data["email"]
    assert "id" in response.json()  # Expect an ID to be present
    assert "created_at" in response.json()  # Check for timestamp field

def test_create_teacher_missing_name(test_client):
    """Test creation fails when name is missing."""
    teacher_data = {
        "email": "john.doe@example.com"
    }

    response = test_client.post("/teachers", json=teacher_data)
    
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing field: name",
            "details": {}
        }
    }

def test_create_teacher_missing_email(test_client):
    """Test creation fails when email is missing."""
    teacher_data = {
        "name": "John Doe"
    }

    response = test_client.post("/teachers", json=teacher_data)
    
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing field: email",
            "details": {}
        }
    }

def test_create_teacher_invalid_email(test_client):
    """Test creation fails when email format is invalid."""
    teacher_data = {
        "name": "John Doe",
        "email": "not-an-email"
    }

    response = test_client.post("/teachers", json=teacher_data)

    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Invalid email format",
            "details": {}
        }
    }

def test_create_teacher_email_already_exists(test_client, db_session):
    """Test creation fails when email already exists."""
    # First, create a teacher with the same email
    teacher_data = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

    test_client.post("/teachers", json=teacher_data)

    # Try creating another teacher with the same email
    duplicate_teacher_data = {
        "name": "John Smith",
        "email": "jane.doe@example.com"
    }

    response = test_client.post("/teachers", json=duplicate_teacher_data)

    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E003",
            "message": "Email already exists",
            "details": {}
        }
    }
```