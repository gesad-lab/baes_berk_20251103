```python
import pytest
from fastapi.testclient import TestClient
from main import app  # assuming your FastAPI app is defined in main.py
from models import Student  # assuming your Student model is defined here
from sqlalchemy.exc import IntegrityError

client = TestClient(app)

@pytest.fixture
def create_student():
    """
    Fixture to create a student for testing. The created student must have
    valid attributes including email.
    """
    valid_student_data = {"name": "John Doe", "age": 20, "email": "john.doe@example.com"}
    response = client.post("/students/", json=valid_student_data)
    yield response.json()  
    # Clean up code can be added here if needed


def test_create_student_with_valid_email(create_student):
    """
    Test creating a student with a valid email. 
    The student should be created successfully.
    """
    assert create_student["email"] == "john.doe@example.com"
    assert create_student["name"] == "John Doe"
    assert create_student["age"] == 20


def test_create_student_without_email():
    """
    Test creating a student without providing an email.
    Should return a validation error indicating the email is required.
    """
    response = client.post("/students/", json={"name": "Jane Doe", "age": 21})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email is required.", "details": {}}}


def test_create_student_with_invalid_email_format():
    """
    Test creating a student with an invalid email format.
    Should return a validation error indicating the email format is invalid.
    """
    response = client.post("/students/", json={"name": "Jane Doe", "age": 21, "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid email format.", "details": {}}}
```