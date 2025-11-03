import pytest
from fastapi.testclient import TestClient
from src.services.student_service import StudentService
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the in-memory database for testing."""
    # This fixture is set up for in-memory testing and cleanup if needed
    yield

def test_create_student_success(setup_database):
    """Test creating a student with valid data, including email."""
    response = client.post(
        "/students/",
        json={"name": "John Doe", "email": "john.doe@example.com"}
    )
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_student_missing_email(setup_database):
    """Test creating a student without an email should return an error."""
    response = client.post(
        "/students/",
        json={"name": "Jane Doe"}
    )
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Email field is required.",
            "details": {}
        }
    }

def test_retrieve_student_with_email(setup_database):
    """Test retrieving a student by ID returns the correct details including email."""
    # First, we need to create a student to retrieve
    creation_response = client.post(
        "/students/",
        json={"name": "Alice", "email": "alice@example.com"}
    )
    student_id = creation_response.json()["id"]

    # Now we retrieve that student
    retrieval_response = client.get(f"/students/{student_id}")
    assert retrieval_response.status_code == 200
    assert retrieval_response.json()["id"] == student_id
    assert retrieval_response.json()["name"] == "Alice"
    assert retrieval_response.json()["email"] == "alice@example.com"