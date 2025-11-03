import pytest
from fastapi.testclient import TestClient
from src.services.student_service import StudentService
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the in-memory database for testing."""
    # If using a separate test database, configure it here
    yield
    # Any cleanup can be done here if needed

def test_create_student_success(setup_database):
    """Test creating a student with valid data."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"

def test_create_student_missing_name(setup_database):
    """Test creating a student without providing a name."""
    response = client.post("/students", json={})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required.",
            "details": {}
        }
    }

def test_get_student_success(setup_database):
    """Test retrieving an existing student by ID."""
    create_response = client.post("/students", json={"name": "Jane Doe"})
    student_id = create_response.json()["id"]
    
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == student_id
    assert data["name"] == "Jane Doe"

def test_get_student_not_found(setup_database):
    """Test retrieving a non-existing student."""
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Student not found.",
            "details": {}
        }
    }