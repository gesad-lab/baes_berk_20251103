```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from pydantic import BaseModel, EmailStr

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Set up any necessary database state before tests
    yield
    # Clean up database state after tests

# Pydantic models for Student creation and updating
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Required field with email validation

class StudentUpdate(BaseModel):
    name: str = None  # Optional
    email: EmailStr = None  # Optional update

def test_create_student_with_email(setup_database):
    """Test that a new Student can be created with email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()['name'] == "John Doe"
    assert response.json()['email'] == "john.doe@example.com"

def test_create_student_without_email(setup_database):
    """Test that creating a Student without an email returns a validation error."""
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json()['detail'][0]['msg'] == "field required"

def test_create_student_with_invalid_email(setup_database):
    """Test that creating a Student with an invalid email format returns a validation error."""
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalid-email-format"})
    assert response.status_code == 400
    assert response.json()['detail'][0]['msg'] == "value is not a valid email address"

def test_update_student_email(setup_database):
    """Test that updating a Student's email works as expected."""
    # Assuming there's a student with ID 1
    response = client.put("/students/1", json={"email": "new.email@example.com"})
    assert response.status_code == 200
    assert response.json()['email'] == "new.email@example.com"

def test_retrieve_student_email(setup_database):
    """Test that retrieving a Student by ID returns the correct email."""
    response = client.get("/students/1")
    assert response.status_code == 200
    assert 'email' in response.json()
```