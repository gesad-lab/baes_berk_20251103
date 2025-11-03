import pytest
from fastapi.testclient import TestClient
from main import app  # Adjust the import based on your project structure

# Create a test client for the FastAPI application
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up and tear down the database for integration tests.
    This should create a fresh database before tests and drop it after.
    """
    # Code to set up the database
    # e.g., creating tables or any required initial data
    yield  # Tests will be run here
    # Code to tear down the database
    # e.g., dropping tables or cleaning up data


def test_create_student_success(setup_database):
    """
    Test creating a student successfully with valid input.
    """
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # HTTP 201 Created
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"

def test_create_student_missing_name(setup_database):
    """
    Test creating a student with missing 'name' field.
    """
    response = client.post("/students", json={})
    assert response.status_code == 400  # HTTP 400 Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}

def test_get_student_success(setup_database):
    """
    Test retrieving a student by ID.
    """
    # First create a student
    create_response = client.post("/students", json={"name": "Jane Doe"})
    student_id = create_response.json()["id"]
    
    # Now retrieve the student
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200  # HTTP 200 OK
    data = response.json()
    assert data["id"] == student_id
    assert data["name"] == "Jane Doe"

def test_get_student_not_found(setup_database):
    """
    Test retrieving a student that does not exist.
    """
    response = client.get("/students/999")  # Assuming this ID does not exist
    assert response.status_code == 404  # HTTP 404 Not Found
    assert response.json() == {"error": {"code": "E002", "message": "Student not found."}}