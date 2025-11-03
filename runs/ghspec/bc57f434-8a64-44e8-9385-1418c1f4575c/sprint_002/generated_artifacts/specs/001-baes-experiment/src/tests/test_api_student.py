```python
import pytest
from fastapi.testclient import TestClient
from your_application.database import get_db, SessionLocal
from your_application.models import Student  # Adjust based on your project's structure
from your_application.api import app  # The FastAPI application instance

# Fixture to create a test client
@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

# Helper function to create a student for testing
def create_student(client, name="Test Student", email="test@student.com"):
    response = client.post("/students", json={"name": name, "email": email})
    return response.json()

# Integration test for updating a student's email
def test_update_student_email(test_client):
    # Create a student to update
    student_data = create_student(test_client)
    student_id = student_data["id"]  # Assuming the response contains the student ID

    # New email to update
    new_email = "updated@student.com"
    
    # Update the student's email
    response = test_client.put(f"/students/{student_id}", json={"email": new_email})
    
    # Assert that the response is successful
    assert response.status_code == 200
    updated_student = response.json()
    
    # Verify that the email has been updated
    assert updated_student["email"] == new_email

def test_update_student_email_with_invalid_format(test_client):
    # Create a student to update
    student_data = create_student(test_client)
    student_id = student_data["id"]  # Assuming the response contains the student ID

    # Invalid email format
    invalid_email = "invalid_email_format"
    
    # Attempt to update the student's email
    response = test_client.put(f"/students/{student_id}", json={"email": invalid_email})
    
    # Assert that the response indicates a client error
    assert response.status_code == 400
    response_data = response.json()
    
    # Check if the error message is as expected
    assert response_data == {
        "error": {
            "code": "E002",
            "message": "Invalid email format",
            "details": {}
        }
    }

def test_update_student_email_missing(test_client):
    # Create a student to attempt to update
    student_data = create_student(test_client)
    student_id = student_data["id"]  # Assuming the response contains the student ID

    # Attempt to update the student's email without providing an email
    response = test_client.put(f"/students/{student_id}", json={})
    
    # Assert that the response indicates a client error
    assert response.status_code == 400
    response_data = response.json()
    
    # Check if the error message indicates the missing email
    assert response_data == {
        "error": {
            "code": "E001",
            "message": "Missing email field",
            "details": {}
        }
    }
```