```python
import pytest
from fastapi.testclient import TestClient
from myapp.main import app  # Importing the FastAPI app
from myapp.models import Teacher  # Assuming Teacher model is defined

# Create a TestClient for making requests to the FastAPI app
client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Fixture to set up the database schema before running tests."""
    # Here you would typically create your database schema and any necessary initial data
    pass

def test_create_teacher_success():
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()  # Check that the ID of the newly created teacher is returned

def test_create_teacher_missing_name():
    """Test creating a teacher without a name."""
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400  # Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required field: name",
            "details": {}
        }
    }

def test_create_teacher_missing_email():
    """Test creating a teacher without an email."""
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 400  # Bad Request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Missing required field: email",
            "details": {}
        }
    }

def test_get_teacher_success():
    """Test retrieving a teacher's details successfully."""
    # First, create a teacher to ensure we have one to retrieve.
    create_response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    teacher_id = create_response.json()["id"]

    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": teacher_id,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

def test_get_teacher_not_found():
    """Test retrieving a teacher that does not exist."""
    response = client.get("/teachers/999")  # Assuming 999 does not exist in the database
    assert response.status_code == 404  # Not Found
    assert response.json() == {
        "error": {
            "code": "E003",
            "message": "Teacher not found",
            "details": {}
        }
    }
```