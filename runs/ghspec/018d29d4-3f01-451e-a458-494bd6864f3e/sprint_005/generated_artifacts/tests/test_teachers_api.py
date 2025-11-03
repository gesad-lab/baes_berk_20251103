import pytest
from fastapi.testclient import TestClient
from main import app  # Assume FastAPI app is instantiated in a file named main.py
from models import Teacher  # Import the Teacher model

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    """Setup the database before each test case."""
    # Normally you would set up the database, handle migrations, etc.
    # This may include creating the necessary tables and a clean state for every test
    pass  # Replace with actual setup code

def test_create_teacher_with_valid_data():
    """Test creating a new teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_get_teacher_details():
    """Test retrieving details of a specific teacher."""
    # First, create a teacher to retrieve
    create_response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    teacher_id = create_response.json()["id"]

    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert "name" in response.json() and "email" in response.json()
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane.doe@example.com"

def test_create_teacher_with_invalid_email():
    """Test creating a teacher with an invalid email format."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "not-an-email"})
    assert response.status_code == 400
    assert "error" in response.json()
    assert response.json()["error"]["message"] == "Invalid email format"

def test_retrieve_nonexisting_teacher():
    """Test retrieving a non-existing teacher by ID."""
    response = client.get("/teachers/9999")  # Assuming 9999 does not exist
    assert response.status_code == 404
    assert "error" in response.json()
    assert response.json()["error"]["message"] == "Teacher not found"