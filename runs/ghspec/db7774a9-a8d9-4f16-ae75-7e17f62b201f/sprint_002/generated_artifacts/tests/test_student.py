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

def test_create_student_with_email():
    """Test creating a student with a valid name and email."""
    response = client.post("/students", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "jane@example.com"

def test_retrieve_student_email():
    """Test retrieving a student's details by ID."""
    student = create_student()  # Create a student using the fixture
    response = client.get(f"/students/{student['id']}")
    assert response.status_code == 200
    assert response.json() == {
        "id": student["id"],
        "name": "John Doe",
        "email": "john@example.com"
    }

def test_list_all_students():
    """Test listing all students with names and emails."""
    create_student()  # Create a student for the list
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Ensure that the list is not empty

def test_create_student_with_invalid_email():
    """Test creating a student with an invalid email format."""
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Invalid email format.",
            "details": {}
        }
    }

def test_create_student_without_email():
    """Test creating a student without providing an email."""
    response = client.post("/students", json={"name": "No Email"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email is required.",
            "details": {}
        }
    }
```