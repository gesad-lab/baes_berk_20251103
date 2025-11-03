```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def student_data():
    return {
        "name": "John Doe",
        "age": 20,
        "email": "johndoe@example.com"  # New required email field
    }

def test_create_student_success(student_data):
    response = client.post("/students/", json=student_data)
    assert response.status_code == 201  # Check for successful creation
    assert "id" in response.json()  # Ensure the response contains an ID
    assert response.json()["email"] == student_data["email"]  # Verify email is stored correctly

def test_create_student_missing_email():
    response = client.post("/students/", json={"name": "Jane Doe", "age": 22})
    assert response.status_code == 422  # Check for validation error (missing email)
    assert response.json() == {"error": {"code": "E002", "message": "Email is required."}}  # Ensure the error message is appropriate

def test_create_student_invalid_email():
    invalid_email_data = {
        "name": "John Smith",
        "age": 21,
        "email": "invalid_email"  # Invalid email format
    }
    response = client.post("/students/", json=invalid_email_data)
    assert response.status_code == 422  # Check for validation error (invalid email)
    assert response.json() == {"error": {"code": "E003", "message": "Invalid email format."}}  # Ensure the error message is appropriate

def test_get_student_success():
    response = client.get("/students/1")  # Assuming student with ID 1 exists
    assert response.status_code == 200  # Check for success
    assert "email" in response.json()  # Ensure email is included in the response

def test_update_student_success():
    update_data = {
        "name": "John Doe",
        "age": 20,
        "email": "johnupdated@example.com"  # New email to update
    }
    response = client.put("/students/1", json=update_data)  # Assuming student with ID 1 exists
    assert response.status_code == 200  # Check for successful update
    assert response.json()["email"] == update_data["email"]  # Verify the email is updated correctly

def test_update_student_invalid_email():
    invalid_email_data = {
        "name": "John Smith",
        "age": 21,
        "email": "invalid_email"  # Invalid email format
    }
    response = client.put("/students/1", json=invalid_email_data)  # Assuming student with ID 1 exists
    assert response.status_code == 422  # Check for validation error (invalid email)
    assert response.json() == {"error": {"code": "E003", "message": "Invalid email format."}}  # Ensure the error message is appropriate
```