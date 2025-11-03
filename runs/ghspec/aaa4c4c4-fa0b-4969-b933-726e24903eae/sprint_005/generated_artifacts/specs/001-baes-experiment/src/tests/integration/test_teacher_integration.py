import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py

# Initialize the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to set up the database state before tests and clean up afterwards."""
    # Assume setup logic is handled here, e.g., creating tables and seeding data
    pass

@pytest.fixture(scope="module")
def create_teacher():
    """Fixture to create a teacher for testing purposes."""
    response = client.post("/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    assert response.status_code == 201
    return response.json()  # Return the created teacher's details

def test_create_teacher_success():
    """Test successful creation of a teacher."""
    response = client.post("/teachers", json={"name": "Emily Johnson", "email": "emily.johnson@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Emily Johnson"
    assert data["email"] == "emily.johnson@example.com"

def test_create_teacher_missing_fields():
    """Test creation of a teacher with missing required fields."""
    response = client.post("/teachers", json={"name": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Missing required fields: email"}}

def test_get_teacher_details(create_teacher):
    """Test retrieval of a teacher's details."""
    teacher_id = create_teacher['id']
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == teacher_id
    assert data["name"] == create_teacher["name"]
    assert data["email"] == create_teacher["email"]

def test_get_non_existent_teacher():
    """Test retrieval of a non-existent teacher."""
    response = client.get("/teachers/99999")  # Assuming this ID does not exist
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Teacher not found"}}