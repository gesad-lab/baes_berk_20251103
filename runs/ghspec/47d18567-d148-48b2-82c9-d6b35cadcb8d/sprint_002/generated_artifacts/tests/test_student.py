```python
import json
import pytest
from fastapi.testclient import TestClient
from src.api.student import app  # Assuming 'app' is the FastAPI instance
from src.db.models import Student   # Import the Student model

client = TestClient(app)

@pytest.fixture
def sample_student():
    """Fixture to return a sample student data"""
    return {"name": "John Doe", "email": "john.doe@example.com"}

@pytest.fixture
def invalid_email_student():
    """Fixture to return a sample student data with an invalid email"""
    return {"name": "Jane Doe", "email": "not_an_email"}

def test_add_student_success(sample_student):
    """Test adding a new student successfully."""
    response = client.post("/students/", json=sample_student)
    assert response.status_code == 201  # Check if the response is created
    response_data = response.json()
    assert response_data["name"] == sample_student["name"]
    assert response_data["email"] == sample_student["email"]

def test_add_student_missing_email(sample_student):
    """Test adding a new student without an email."""
    student_data = sample_student.copy()
    del student_data["email"]
    response = client.post("/students/", json=student_data)
    assert response.status_code == 400  # Expect a Bad Request
    assert "email" in response.json()["error"]["message"]

def test_add_student_invalid_email(invalid_email_student):
    """Test adding a new student with an invalid email."""
    response = client.post("/students/", json=invalid_email_student)
    assert response.status_code == 400  # Expect a Bad Request
    assert "email" in response.json()["error"]["message"]

def test_get_students():
    """Test retrieving the list of students."""
    response = client.get("/students/")
    assert response.status_code == 200  # Check if the response is OK
    students = response.json()
    assert isinstance(students, list)  # Expect a list
    # Assuming at least one student exists, adjust as necessary for test environment
    assert all("id" in student for student in students)
    assert all("name" in student for student in students)
    assert all("email" in student for student in students)
```