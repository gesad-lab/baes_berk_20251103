```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the main FastAPI application is in src/main.py
from src.database import get_database  # Assuming there is a function to get the database

client = TestClient(app)

# Integration tests for the student API endpoints
@pytest.mark.integration
def test_create_student_with_email():
    """Test creating a new student with email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json() == {"name": "John Doe", "email": "john@example.com"}

def test_create_student_without_email():
    """Test creating a new student without an email."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Field 'email' is required."}

def test_create_student_with_invalid_email():
    """Test creating a new student with an invalid email format."""
    response = client.post("/students", json={"name": "John Doe", "email": "not-an-email"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Field 'email' is not a valid email address."}

@pytest.mark.integration
def test_list_students():
    """Test retrieving the list of students with email."""
    # First create a student to ensure we have data to retrieve
    client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert response.json()[0] == {"name": "John Doe", "email": "john@example.com"}
```