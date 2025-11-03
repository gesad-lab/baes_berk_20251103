```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Ensure this imports your FastAPI application

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    # Here you would set up your database for testing.
    # This can involve creating tables and seeding data if necessary.
    pass  # Implement database setup and teardown as needed

def test_create_student_success():
    """Test creating a student successfully."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_create_student_missing_email():
    """Test creating a student fails when email is missing."""
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email is required.", "details": {}}}

def test_create_student_invalid_email():
    """Test creating a student fails when email format is invalid."""
    response = client.post("/students", json={"name": "Alice Smith", "email": "alice.smith@invalid"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid email format.", "details": {}}}

def test_create_student_email_already_exists():
    """Test creating a student fails when email already exists."""
    # First create a student with this email
    client.post("/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    
    # Attempt to create another student with the same email
    response = client.post("/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 409
    assert response.json() == {"error": {"code": "E003", "message": "Email already exists.", "details": {}}}
```