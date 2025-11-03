import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py

# Initialize the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to set up the database state before tests and clean up afterwards."""
    # Assume setup logic is handled here, e.g., creating tables and seeding teacher data
    pass

def test_create_teacher_success():
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    assert response.status_code == 201  # Check if the response status code is 201 Created
    data = response.json()
    assert "id" in data  # Ensure the response includes the teacher ID
    assert data["name"] == "Jane Smith"  # Check the teacher's name
    assert data["email"] == "jane.smith@example.com"  # Check the teacher's email

def test_create_teacher_missing_name():
    """Test creating a teacher with missing name."""
    response = client.post("/teachers", json={"email": "no.name@example.com"})
    assert response.status_code == 400  # Check if the response status code is 400 Bad Request
    data = response.json()
    assert data["message"] == "Missing required field: name"  # Validate the error message

def test_create_teacher_missing_email():
    """Test creating a teacher with missing email."""
    response = client.post("/teachers", json={"name": "No Email"})
    assert response.status_code == 400  # Check if the response status code is 400 Bad Request
    data = response.json()
    assert data["message"] == "Missing required field: email"  # Validate the error message

def test_get_teacher_success():
    """Test retrieving a teacher by ID."""
    # First, we create a teacher to retrieve
    create_response = client.post("/teachers", json={"name": "Mark Johnson", "email": "mark.johnson@example.com"})
    teacher_id = create_response.json()["id"]  # Get the created teacher's ID

    # Now retrieve the teacher using the ID
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200  # Ensure the request was successful
    data = response.json()
    assert data["id"] == teacher_id  # Validate the returned teacher ID
    assert data["name"] == "Mark Johnson"  # Validate the teacher's name
    assert data["email"] == "mark.johnson@example.com"  # Validate the teacher's email

def test_get_teacher_not_found():
    """Test retrieving a teacher that does not exist."""
    response = client.get("/teachers/999")  # Attempt to get a non-existent teacher
    assert response.status_code == 404  # Check if the response status code is 404 Not Found
    data = response.json()
    assert data["message"] == "Teacher not found"  # Validate the error message