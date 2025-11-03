import pytest
from src.api.student_api import app  # Import the FastAPI app
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Here you would setup the database, e.g., create tables or seed initial data
    # This is a placeholder for database setup logic
    yield
    # Here you would tear down the database, e.g., drop tables if needed


def test_retrieve_all_students_empty(setup_database):
    """Test retrieving all students when no student exists should return an empty array."""
    response = client.get("/students")
    
    assert response.status_code == 200
    assert response.json() == []  # An empty array is expected


def test_create_student(setup_database):
    """Test creating a student should succeed and return the student object."""
    response = client.post("/students", json={"name": "John Doe"})
    
    assert response.status_code == 201
    assert response.json() == {"id": response.json()["id"], "name": "John Doe"}  # Expect the response to include an ID


def test_retrieve_all_students_with_data(setup_database):
    """Test retrieving all students should return the student just created."""
    # Create a student to ensure data exists
    client.post("/students", json={"name": "John Doe"})
    
    response = client.get("/students")
    
    assert response.status_code == 200
    assert len(response.json()) == 1  # Expecting one student
    assert response.json()[0]["name"] == "John Doe"  # The name should match


def test_fail_to_create_student_without_name(setup_database):
    """Test should return an error when attempting to create a student without a name."""
    response = client.post("/students", json={})  # Name is required, so we send an empty body
    
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name field is required.",
            "details": {}
        }
    }  # Expect an error response indicating the name is required