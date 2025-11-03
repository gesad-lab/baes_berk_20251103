```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Setup the test database and create test data
    with TestClient(app) as client:
        yield client  # Provide the client to the tests

def test_create_student_with_email(setup_database):
    """Test creating a student with valid email"""
    response = setup_database.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # 201 Created
    assert "student_id" in response.json()  # Assert that the response contains the student_id

def test_create_student_with_invalid_email(setup_database):
    """Test creating a student with invalid email format"""
    response = setup_database.post("/students", json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format", "details": {}}}

def test_create_student_without_email(setup_database):
    """Test creating a student without providing an email"""
    response = setup_database.post("/students", json={"name": "John Smith"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {"error": {"code": "E002", "message": "Email is required", "details": {}}}

def test_get_student_by_email(setup_database):
    """Test retrieving a student by email"""
    # First, create a student
    create_response = setup_database.post("/students", json={"name": "Alice", "email": "alice@example.com"})
    student_id = create_response.json()["student_id"]

    # Now, get the student by email
    response = setup_database.get(f"/students/email/{create_response.json()['email']}")
    assert response.status_code == 200  # 200 OK
    assert response.json()["student_id"] == student_id  # Assert that we fetched the correct student

def test_get_nonexistent_student_by_email(setup_database):
    """Test handling get request for a nonexistent student by email"""
    response = setup_database.get("/students/email/nonexistent@example.com")
    assert response.status_code == 404  # 404 Not Found
    assert response.json() == {"error": {"code": "E003", "message": "Student not found", "details": {}}}
```