import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py
from src.models import Student  # Assuming a Student model exists in src/models.py
from src.database import get_db, SessionLocal  # Adjust imports based on your project structure

# Fixture to create a test client
@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

# Fixture to create a student instance for testing
@pytest.fixture
def new_student():
    return {
        "name": "John Doe",
        "age": 20,
        "email": "john.doe@example.com"
    }

# Test Create Student
def test_create_student(test_client, new_student):
    response = test_client.post("/students/", json=new_student)  # Assuming POST /students/ creates a student
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == new_student["name"]
    assert data["age"] == new_student["age"]
    assert data["email"] == new_student["email"]

# Test Read Student
def test_read_student(test_client):
    student_id = 1  # Assuming we have a student with ID 1
    response = test_client.get(f"/students/{student_id}")  # Assuming GET /students/{id} retrieves a student
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == student_id

# Test Update Student
def test_update_student(test_client):
    student_id = 1  # Assuming we're updating student with ID 1
    updated_student = {
        "name": "Jane Doe",
        "age": 21,
        "email": "jane.doe@example.com"
    }
    response = test_client.put(f"/students/{student_id}", json=updated_student)  # Assuming PUT /students/{id} updates a student
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_student["name"]
    assert data["age"] == updated_student["age"]
    assert data["email"] == updated_student["email"]

# Test Delete Student
def test_delete_student(test_client):
    student_id = 1  # Assuming we're deleting student with ID 1
    response = test_client.delete(f"/students/{student_id}")  # Assuming DELETE /students/{id} deletes a student
    assert response.status_code == 204  # No content expected on successful deletion

    # Attempt to read the deleted student
    response = test_client.get(f"/students/{student_id}")
    assert response.status_code == 404  # Expect not found error for deleted student

# Run this file with pytest to validate the CRUD operations.