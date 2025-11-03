```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in src/main.py
from src.db import init_db, shutdown_db  # Database management functions
from src.models import Teacher  # Assuming you have a Teacher model

# Mock data for testing
valid_teacher_data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Set up the database for testing."""
    init_db()
    yield
    shutdown_db()

@pytest.fixture
def client():
    """Create a TestClient for FastAPI app."""
    return TestClient(app)

def test_create_teacher_success(client):
    """Test creating a Teacher successfully."""
    response = client.post("/teachers", json=valid_teacher_data)
    assert response.status_code == 200
    assert response.json() == {
        "message": "Teacher created successfully",
        "teacher": {
            "id": 1,  # Assuming this will be auto-generated
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }

def test_create_teacher_missing_fields(client):
    """Test creating a Teacher with missing fields."""
    response = client.post("/teachers", json={})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required fields: name, email"
        }
    }

def test_create_teacher_duplicate_email(client):
    """Test creating a Teacher with a duplicate email."""
    client.post("/teachers", json=valid_teacher_data)  # Create first teacher
    response = client.post("/teachers", json=valid_teacher_data)  # Create second teacher
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email address already in use"
        }
    }

def test_retrieve_teacher_details(client):
    """Test retrieving Teacher details."""
    response = client.get("/teachers/1")  # Assuming 1 is the created teacher's ID
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
```