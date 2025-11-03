```python
# tests/test_integration.py

import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your main app is in a file called main.py
from models import Course, Student, StudentCourses, Teacher  # Import required models

client = TestClient(app)

# Test case for creating a new teacher
def test_create_teacher():
    teacher_data = {"name": "Mr. Smith", "email": "smith@example.com"}
    response = client.post("/teachers", json=teacher_data)
    assert response.status_code == 201  # Expect status OK on creation
    assert response.json()["name"] == teacher_data["name"]
    assert response.json()["email"] == teacher_data["email"]

# Test case for retrieving teachers
def test_get_teachers():
    response = client.get("/teachers")
    assert response.status_code == 200  # Expect status OK on retrieval
    assert isinstance(response.json(), list)  # Should return a list
    assert len(response.json()) > 0  # Ensure that we have at least one teacher

# Test case for validating teacher creation with missing fields
def test_create_teacher_missing_fields():
    # Missing the email field
    teacher_data = {"name": "Mrs. Johnson"}
    response = client.post("/teachers", json=teacher_data)
    assert response.status_code == 400  # Expect client error
    assert response.json()["error"]["code"] == "E001"  # Check for specific error code
    assert "email" in response.json()["error"]["message"]  # Message should indicate missing email

# Test case for validating teacher creation with invalid email
def test_create_teacher_invalid_email():
    teacher_data = {"name": "Mrs. Doe", "email": "invalid-email"}
    response = client.post("/teachers", json=teacher_data)
    assert response.status_code == 400  # Expect client error
    assert response.json()["error"]["code"] == "E002"  # Check for specific error code
    assert "email" in response.json()["error"]["message"]  # Message should indicate invalid email
```