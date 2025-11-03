import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.routes.students import app  # Assuming 'app' is defined in students.py for student routes

# Initialize the FastAPI test client
client = TestClient(app)

def test_create_student_missing_name():
    """
    Test creating a student without providing a name.
    The API should return a 400 error and a message indicating the name field is required.
    """

    # Attempt to create a student without the required 'name' field
    response = client.post("/students", json={})  # Missing 'name' field
    assert response.status_code == 400  # Check for Bad Request status
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "The name field is required.",
            "details": {}
        }
    }  # Verify the error message structure

def test_create_student_with_blank_name():
    """
    Test creating a student with an empty name string.
    The API should return a 400 error and a message indicating the name field is required.
    """

    # Attempt to create a student with an empty name
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400  # Check for Bad Request status
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "The name field is required.",
            "details": {}
        }
    }  # Verify the error message structure

def test_create_student_with_valid_data():
    """
    Test creating a student with valid data.
    The API should create the student and return a success message.
    """

    # Attempt to create a student with a valid name
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # Check for Created status
    assert response.json() == {"message": "Student created successfully."}  # Verify success message

# Additional tests for retrieving students can go here...
