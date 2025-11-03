import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust the import based on your actual project structure
from src.models import StudentCreate, StudentResponse  # Import your data models

client = TestClient(app)

# Test the creation of a student
def test_create_student_success():
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

# Test creating a student without a name
def test_create_student_missing_name():
    response = client.post("/students", json={"email": "john.doe@example.com"})
    assert response.status_code == 422  # Unprocessable Entity
    error_details = response.json()
    assert error_details["detail"][0]["msg"] == "field required"

# Test creating a student without an email
def test_create_student_missing_email():
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 422  # Unprocessable Entity
    error_details = response.json()
    assert error_details["detail"][0]["msg"] == "field required"

# Test retrieving a student by ID
def test_get_student_by_id():
    # First create a student to obtain an ID
    create_response = client.post("/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    student_id = create_response.json()["id"]

    # Now retrieve the student by ID
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == student_id
    assert data["name"] == "Jane Doe"
    assert data["email"] == "jane.doe@example.com"

# Test updating a student's email
def test_update_student_email():
    # First create a student to update
    create_response = client.post("/students", json={"name": "Alice Smith", "email": "alice.smith@example.com"})
    student_id = create_response.json()["id"]

    # Now update the student's email
    update_response = client.put(f"/students/{student_id}", json={"email": "alice.newemail@example.com"})
    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data["id"] == student_id
    assert updated_data["name"] == "Alice Smith"
    assert updated_data["email"] == "alice.newemail@example.com"

    # Verify the update was successful by retrieving the student again
    verify_response = client.get(f"/students/{student_id}")
    assert verify_response.status_code == 200
    verify_data = verify_response.json()
    assert verify_data["email"] == "alice.newemail@example.com"