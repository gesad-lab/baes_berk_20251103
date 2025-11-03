import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    # Code for creating the test database schema can be added here.
    yield
    # Code for tearing down the database can be added here.

def test_create_student_success(setup_db):
    """Test successful creation of a student."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # Check for a successful creation
    assert response.json() == {"message": "Student created successfully", "student": {"name": "John Doe"}} 

def test_create_student_missing_name(setup_db):
    """Test creation of a student with missing name."""
    response = client.post("/students", json={})
    assert response.status_code == 400  # Bad request error
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required",
            "details": {}
        }
    }

def test_get_student_info(setup_db):
    """Test retrieval of a student's information."""
    create_response = client.post("/students", json={"name": "Jane Doe"})
    student_id = create_response.json().get("student").get("id")  # Extracting the student ID

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200  # Check for successful retrieval
    assert response.json() == {"id": student_id, "name": "Jane Doe"}

def test_invalid_student_id(setup_db):
    """Test retrieval of a student's information with an invalid ID."""
    response = client.get("/students/99999")  # Assuming 99999 is an invalid ID
    assert response.status_code == 404  # Not found error
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Student not found",
            "details": {}
        }
    }