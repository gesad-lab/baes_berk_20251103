import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the main FastAPI application is in src/main.py
from src.database import get_database  # Assuming there is a function to get the database

client = TestClient(app)

# Integration tests for the student API endpoints
@pytest.mark.integration
def test_create_student():
    """Test creating a new student"""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # HTTP 201 Created
    student_data = response.json()
    assert "id" in student_data  # Check if the student ID is returned
    assert student_data["name"] == "John Doe"  # Verify the student name


@pytest.mark.integration
def test_retrieve_student_list():
    """Test retrieving all students"""
    response = client.get("/students")
    assert response.status_code == 200  # HTTP 200 OK
    students = response.json()
    assert isinstance(students, list)  # Check if the response is a list


@pytest.mark.integration
def test_create_student_without_name():
    """Test creating a new student without a name"""
    response = client.post("/students", json={})
    assert response.status_code == 400  # HTTP 400 Bad Request
    error_response = response.json()
    assert error_response == {
        "error": {
            "code": "E001",
            "message": "Name field is required",
            "details": {}
        }
    }  # Ensure the correct error format and message

# Add more tests as necessary to meet coverage requirements