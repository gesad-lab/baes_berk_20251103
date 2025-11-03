```python
# tests/test_api.py
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

def test_create_teacher(client):
    """Test the creation of a Teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Check for successful creation
    assert "teacher" in response.json()  # Ensure the teacher object is in the response
    assert response.json()["teacher"]["name"] == "John Doe"
    assert response.json()["teacher"]["email"] == "john.doe@example.com"

def test_get_teacher_details(client):
    """Test retrieving Teacher details."""
    # First create a teacher
    create_response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    teacher_id = create_response.json()["teacher"]["id"]

    # Now retrieve the teacher details
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200  # Ensure the request is successful
    assert response.json()["id"] == teacher_id
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane.doe@example.com"

def test_get_teacher_details_not_found(client):
    """Test getting details of a non-existent Teacher."""
    response = client.get("/teachers/999")  # Assuming 999 is a non-existent ID
    assert response.status_code == 404  # Ensure we get a not found response
    assert response.json() == {"error": {"code": "E003", "message": "Teacher not found"}}  # Response schema when not found
```