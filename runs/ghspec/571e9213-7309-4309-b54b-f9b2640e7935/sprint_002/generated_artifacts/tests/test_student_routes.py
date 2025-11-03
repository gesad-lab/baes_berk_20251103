```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Adjust the import based on your project structure

# Create a test client for the FastAPI application
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up and tear down the database for integration tests.
    This should create a fresh database before tests and drop it after.
    """
    # Code to set up the database should go here
    # e.g., creating tables or any required initial data ...
    yield  # Code after yield will run as teardown

def test_create_student_with_valid_data(setup_database):
    """
    Test creating a student with valid name and email.
    Expect a success response with student ID, name, and email.
    """
    response = client.post("/students", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 201  # 201 Created
    data = response.json()
    assert "id" in data
    assert data["name"] == "Jane Doe"
    assert data["email"] == "jane@example.com"

def test_retrieve_student_with_email(setup_database):
    """
    Test retrieving a student by existing ID.
    Expect a valid student record in response including the email field.
    """
    response = client.post("/students", json={"name": "Alice Smith", "email": "alice@example.com"})
    student_id = response.json()["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200  # 200 OK
    data = response.json()
    assert data["id"] == student_id
    assert data["email"] == "alice@example.com"

def test_create_student_with_invalid_email(setup_database):
    """
    Test creating a student with an invalid email format.
    Expect an error response indicating the email format is invalid.
    """
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalid-email-format"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Invalid email format",
            "details": {}
        }
    }

def test_create_student_with_missing_email(setup_database):
    """
    Test creating a student without providing an email.
    Expect an error response indicating the email field is required.
    """
    response = client.post("/students", json={"name": "Missing Email"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email field is required",
            "details": {}
        }
    }
```