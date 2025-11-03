import pytest
from fastapi.testclient import TestClient
from myapp.main import app  # Assuming your FastAPI app is instantiated in main.py

client = TestClient(app)

def test_add_student_with_valid_email():
    """Test adding a student with valid name and email."""
    response = client.post("/students", json={"name": "Valid Student", "email": "valid.student@example.com"})
    assert response.status_code == 201  # Assuming 201 Created is the expected response
    assert response.json()["name"] == "Valid Student"
    assert response.json()["email"] == "valid.student@example.com"

def test_add_student_without_email():
    """Test that adding a student without an email returns an error."""
    response = client.post("/students", json={"name": "Student Without Email"})
    assert response.status_code == 400  # Bad Request
    assert response.json()["error"]["code"] == "E001"  # Assuming E001 for missing email error

def test_add_student_with_invalid_email_format():
    """Test that adding a student with an invalid email format returns an error."""
    response = client.post("/students", json={"name": "Invalid Email Student", "email": "not-an-email"})
    assert response.status_code == 400  # Bad Request
    assert response.json()["error"]["code"] == "E002"  # Assuming E002 for invalid email format error

def test_add_student_with_duplicate_email():
    """Test adding a student with a duplicate email returns an error."""
    # First, add a student with a valid email
    client.post("/students", json={"name": "Duplicate Email Student", "email": "duplicate@example.com"})
    
    # Now attempt to add another student with the same email
    response = client.post("/students", json={"name": "Another Student", "email": "duplicate@example.com"})
    assert response.status_code == 400  # Bad Request
    assert response.json()["error"]["code"] == "E003"  # Assuming E003 for duplicate email error