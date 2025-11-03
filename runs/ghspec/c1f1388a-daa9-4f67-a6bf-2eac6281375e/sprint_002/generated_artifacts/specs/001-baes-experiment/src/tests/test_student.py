```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.database import init_db  # Assuming there's a function to initialize the database
from src.models.student import Student
from sqlalchemy.orm import Session
from src.db.database import get_db


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def db_session():
    # Initialize the database and create tables
    db = init_db()  # Hypothetical function to initialize the database
    yield db
    # Cleanup logic could go here if needed


def test_create_student_with_email(test_client):
    """Test creating a student with a valid email."""
    response = test_client.post(
        "/students",
        json={"name": "John Doe", "email": "john.doe@example.com"}
    )
    assert response.status_code == 201  # Created
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"


def test_create_student_with_missing_email(test_client):
    """Test error handling when email is missing."""
    response = test_client.post(
        "/students",
        json={"name": "Jane Doe"}  # Omitting email
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Email field is required.",
            "details": {}
        }
    }


def test_retrieve_student_with_email(test_client):
    """Test retrieving a student includes email in the response."""
    # First, create a student to ensure there’s one to retrieve
    create_response = test_client.post(
        "/students",
        json={"name": "Alice", "email": "alice@example.com"}
    )
    student_id = create_response.json()["id"]

    response = test_client.get(f"/students/{student_id}")
    assert response.status_code == 200  # OK
    data = response.json()
    assert data["id"] == student_id
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"


def test_retrieve_all_students_with_email(test_client):
    """Test retrieving all students includes emails in the response."""
    # Create a couple of students for retrieval
    test_client.post("/students", json={"name": "Bob", "email": "bob@example.com"})
    test_client.post("/students", json={"name": "Charlie", "email": "charlie@example.com"})

    response = test_client.get("/students")
    assert response.status_code == 200  # OK
    data = response.json()
    assert isinstance(data, list)  # Response should be a list
    assert all("email" in student for student in data)  # All students should have an email field
```