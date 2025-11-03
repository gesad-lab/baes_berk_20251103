```python
import pytest
from src.api.student_api import app  # Import the FastAPI app
from fastapi.testclient import TestClient
from src.models.student import Student  # Import the Student model
from src.services.student_service import create_student  # Import the student creation service
from sqlalchemy.exc import IntegrityError

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Set up the database for testing."""
    # Setup logic (e.g. create tables)
    yield
    # Teardown logic (e.g. drop tables)

def test_create_student_with_valid_email(setup_database):
    """Test creating a student with a valid email."""
    response = client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_student_with_invalid_email_format(setup_database):
    """Test creating a student with an invalid email format."""
    response = client.post("/students/", json={"name": "Jane Doe", "email": "jane.doe@com"})
    assert response.status_code == 400  # Bad Request
    assert "email" in response.json()["errors"]  # Assuming the response contains errors

def test_create_student_with_missing_email(setup_database):
    """Test creating a student without providing an email."""
    response = client.post("/students/", json={"name": "No Email"})
    assert response.status_code == 400  # Bad Request
    assert "email" in response.json()["errors"]  # Check if error message relates to email

def test_create_student_with_duplicate_email(setup_database):
    """Test creating a student with a duplicate email."""
    create_student(name="John Doe", email="john.doe@example.com")  # Pre-create a student with the email
    response = client.post("/students/", json={"name": "Another John", "email": "john.doe@example.com"})
    assert response.status_code == 400  # Bad Request due to duplicate email
    assert "email" in response.json()["errors"]  # Assuming the response contains errors

def test_retrieve_student_by_email(setup_database):
    """Test retrieving a student by email."""
    client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    response = client.get("/students/?email=john.doe@example.com")
    assert response.status_code == 200
    assert response.json()["email"] == "john.doe@example.com"
    assert response.json()["name"] == "John Doe"
```