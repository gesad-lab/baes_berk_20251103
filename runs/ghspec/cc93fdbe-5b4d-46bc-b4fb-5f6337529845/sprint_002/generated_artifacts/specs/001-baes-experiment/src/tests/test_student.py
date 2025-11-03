```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    # Code for creating the test database schema can be added here.
    yield
    # Code for tearing down the database can be added here.

def test_create_student_success(setup_db):
    """Test successful creation of a student."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Expecting a 201 Created response
    assert response.json() == {"name": "John Doe", "email": "john.doe@example.com"}

def test_get_student_success(setup_db):
    """Test retrieval of student information including email."""
    response = client.get("/students/1")  # Assuming student with ID 1 exists
    assert response.status_code == 200  # Expecting a 200 OK response
    assert response.json() == {"name": "John Doe", "email": "john.doe@example.com"}

def test_create_student_missing_email(setup_db):
    """Test creation of a student with missing email."""
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 400  # Expecting a 400 Bad Request response
    assert response.json() == {"error": {"code": "E001", "message": "Email field is required."}}

def test_create_student_invalid_email(setup_db):
    """Test creation of a student with invalid email format."""
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalid-email"})
    assert response.status_code == 400  # Expecting a 400 Bad Request response
    assert response.json() == {"error": {"code": "E002", "message": "Invalid email format."}}
```