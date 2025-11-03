import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is created in main.py
from src.models import Student  # Importing the Student model

client = TestClient(app)

# Test cases for email validation related to the Student model

def test_create_student_with_valid_email():
    """Test creating a student with a valid email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    student = response.json()
    assert "id" in student
    assert student["name"] == "John Doe"
    assert student["email"] == "john.doe@example.com"

def test_create_student_with_invalid_email():
    """Test creating a student with an invalid email format."""
    response = client.post("/students", json={"name": "Jane Doe", "email": "not-an-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}

def test_retrieve_students_includes_email():
    """Test retrieving all students includes email."""
    response = client.get("/students")
    assert response.status_code == 200
    students = response.json()
    for student in students:
        assert "email" in student  # Ensure each student has an email field

def test_update_student_email():
    """Test updating a student's email."""
    # First create a student
    create_response = client.post("/students", json={"name": "Jake White", "email": "jake.white@example.com"})
    student_id = create_response.json()["id"]
    
    # Now update the student's email
    update_response = client.put(f"/students/{student_id}", json={"email": "jake.updated@example.com"})
    assert update_response.status_code == 200
    updated_student = update_response.json()
    assert updated_student["email"] == "jake.updated@example.com"

def test_update_student_with_invalid_email():
    """Test updating a student's email with an invalid email format."""
    create_response = client.post("/students", json={"name": "Emily Black", "email": "emily.black@example.com"})
    student_id = create_response.json()["id"]
    
    response = client.put(f"/students/{student_id}", json={"email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}