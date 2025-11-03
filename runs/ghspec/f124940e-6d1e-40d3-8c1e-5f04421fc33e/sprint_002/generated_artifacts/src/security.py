```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is instantiated in src/main.py

client = TestClient(app)

def test_create_student_with_email():
    """
    Test creating a student with a valid email.
    The student should be created successfully and return the correct email.
    """
    response = client.post("/students/", json={"name": "Test Student", "email": "test@student.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "test@student.com"

def test_create_student_with_invalid_email():
    """
    Test creating a student with an invalid email format.
    The application should return a 400 Bad Request with an error message.
    """
    response = client.post("/students/", json={"name": "Test Student", "email": "invalidemail"})
    assert response.status_code == 400
    assert "Invalid email format" in response.json()["detail"]

def test_retrieve_students():
    """
    Test retrieving a list of all students.
    The response should include all students with their email fields.
    """
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Check if response is a list
    assert all("email" in student for student in response.json())  # Check if each student has an email field

def test_update_student_email():
    """
    Test updating a student's email.
    The student's email should be updated successfully and reflect the new email in the response.
    """
    create_response = client.post("/students/", json={"name": "Test Student", "email": "test@student.com"})
    student_id = create_response.json()["id"]  # Extract the student's ID
    
    # Update the student's email
    updated_response = client.put(f"/students/{student_id}", json={"name": "Test Student", "email": "updated@student.com"})
    assert updated_response.status_code == 200
    assert updated_response.json()["email"] == "updated@student.com"

def test_error_handling_for_email():
    """
    Test error handling for creating a student with an invalid email.
    The application should return a clear error message indicating that the email format is invalid.
    """
    response = client.post("/students/", json={"name": "Test Student", "email": "invalidemail"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid email format"
```