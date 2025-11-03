```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in src/main.py
from src.db import init_db, shutdown_db  # Database management functions
from src.models import Teacher  # Assuming you have a Teacher model

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
    """Test the successful creation of a teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Teacher created successfully"
    assert "teacher" in data
    assert data["teacher"]["name"] == "John Doe"
    assert data["teacher"]["email"] == "john.doe@example.com"
    assert "id" in data["teacher"]

def test_create_teacher_missing_fields(client):
    """Test creating a teacher with missing fields."""
    response = client.post("/teachers", json={"name": ""})  # Missing email
    assert response.status_code == 400
    error_data = response.json()
    assert error_data == {
        "error": {
            "code": "E001",
            "message": "Missing required fields: name, email"
        }
    }

def test_create_teacher_duplicate_email(client):
    """Test creating a teacher with a duplicate email."""
    # First create the teacher
    client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})

    # Now try to create another teacher with the same email
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "john.doe@example.com"})
    assert response.status_code == 400
    error_data = response.json()
    assert error_data == {
        "error": {
            "code": "E002",
            "message": "Email address already in use"
        }
    }
```
