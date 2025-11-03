```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Teacher  # Ensure proper import of teacher model

@pytest.fixture
def client():
    """Fixture for the test client."""
    with TestClient(app) as client:
        yield client

def test_create_teacher(client):
    """Test creating a new Teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_teacher_missing_name(client):
    """Test creating a Teacher without providing a name."""
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name field is required."}}

def test_create_teacher_invalid_email(client):
    """Test creating a Teacher with an invalid email format."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email format is invalid."}}

def test_get_teacher_details(client):
    """Test retrieving Teacher details by ID."""
    # Assume we have created a Teacher with ID 1 for this test
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_teacher_not_found(client):
    """Test retrieving a Teacher that does not exist."""
    response = client.get("/teachers/9999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Teacher not found."}}
```