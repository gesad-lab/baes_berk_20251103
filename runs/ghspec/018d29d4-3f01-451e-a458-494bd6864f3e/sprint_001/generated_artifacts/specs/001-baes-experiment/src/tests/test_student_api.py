import pytest
from fastapi.testclient import TestClient
from main import app  # Assume the FastAPI app is instantiated in a file named main.py

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    # Setup the database: create tables as necessary before tests
    # This would normally include dropping any existing tables and re-creating them
    pass  # Replace with actual setup code

def test_create_student_missing_name():
    # Test creating a student without providing a name
    response = client.post("/students", json={})
    assert response.status_code == 400  # Expecting a Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required field: name",
            "details": {}
        }
    }

def test_create_student_missing_name_field():
    # Test creating a student with an empty name
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400  # Expecting a Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required field: name",
            "details": {}
        }
    }

def test_create_student_with_valid_name():
    # Test creating a student with a valid name
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # Expecting Created
    assert "id" in response.json()  # Ensure an ID is returned for the created student

def test_create_student_with_whitespace_name():
    # Test creating a student with a name that is only whitespace
    response = client.post("/students", json={"name": "   "})
    assert response.status_code == 400  # Expecting a Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required field: name",
            "details": {}
        }
    }