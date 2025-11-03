```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture()
def create_student():
    """Fixture to create a student for testing."""
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    return response.json()

def test_create_student():
    """Test creating a student with a valid name and email."""
    response = client.post("/students", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "jane@example.com"

def test_retrieve_student_email():
    """Test retrieval of a student's email by ID."""
    student = create_student
    response = client.get(f"/students/{student['id']}")
    assert response.status_code == 200
    assert response.json()["email"] == student["email"]

def test_list_all_students_with_emails():
    """Test listing all students includes names and emails."""
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    # Check if the created student is listed and has an email
    assert any(student for student in response.json() if student["email"] == "john@example.com")

def test_create_student_with_invalid_email():
    """Test creating a student returns error for invalid email."""
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format."}}
```