```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  

@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

def test_create_student_with_valid_email(client):
    """Test creating a new student with a valid email."""
    response = client.post("/api/v1/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()  # Check if response includes the new student ID

def test_create_student_with_invalid_email(client):
    """Test creating a new student with an invalid email."""
    response = client.post("/api/v1/students", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}

def test_update_student_email(client):
    """Test updating an existing student's email."""
    # First, create a new student
    create_response = client.post("/api/v1/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    student_id = create_response.json()["id"]

    # Now, update that student's email
    update_response = client.put(f"/api/v1/students/{student_id}", json={"email": "jane.updated@example.com"})
    assert update_response.status_code == 200
    assert update_response.json()["email"] == "jane.updated@example.com"

def test_update_student_email_with_invalid_email(client):
    """Test updating a student's email with an invalid email format."""
    # First, create a new student
    create_response = client.post("/api/v1/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    student_id = create_response.json()["id"]

    # Now, try updating with an invalid email
    update_response = client.put(f"/api/v1/students/{student_id}", json={"email": "invalid-email"})
    assert update_response.status_code == 400
    assert update_response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}

def test_retrieve_student(client):
    """Test retrieving a student's details, including email, by student ID."""
    # Create a new student
    create_response = client.post("/api/v1/students", json={"name": "Jake Doe", "email": "jake.doe@example.com"})
    student_id = create_response.json()["id"]

    # Retrieve the student
    retrieve_response = client.get(f"/api/v1/students/{student_id}")
    assert retrieve_response.status_code == 200
    assert retrieve_response.json()["email"] == "jake.doe@example.com"
```