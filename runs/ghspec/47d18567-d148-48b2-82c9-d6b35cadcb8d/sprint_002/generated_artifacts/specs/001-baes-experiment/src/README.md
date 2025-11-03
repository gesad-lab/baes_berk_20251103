```python
import json
import pytest
from fastapi.testclient import TestClient
from src.api.student import app  # Assuming 'app' is the FastAPI instance

client = TestClient(app)

@pytest.fixture
def sample_student():
    """Fixture to return a sample student data"""
    return {"name": "John Doe", "email": "john.doe@example.com"}

def test_add_student_success(sample_student):
    """Test adding a new student successfully."""
    response = client.post("/students/", json=sample_student)
    assert response.status_code == 201
    assert response.json() == {"name": "John Doe", "email": "john.doe@example.com"}

def test_add_student_without_email():
    """Test adding a student without an email returns an error."""
    student_data = {"name": "Jane Doe"}
    response = client.post("/students/", json=student_data)
    assert response.status_code == 400  # Bad Request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email is required.",
            "details": {}
        }
    }

def test_add_student_with_invalid_email():
    """Test adding a student with an invalid email returns an error."""
    student_data = {"name": "Jake Doe", "email": "jake.doe@invalid"}
    response = client.post("/students/", json=student_data)
    assert response.status_code == 400  # Bad Request
    assert response.json() == {
        "error": {
            "code": "E003",
            "message": "Invalid email format.",
            "details": {}
        }
    }

def test_retrieve_students():
    """Test retrieving students returns correct data format including emails."""
    response = client.get("/students/")
    assert response.status_code == 200
    # Assuming the response contains a list of students with names and emails
    assert isinstance(response.json(), list)
    for student in response.json():
        assert "name" in student
        assert "email" in student
```