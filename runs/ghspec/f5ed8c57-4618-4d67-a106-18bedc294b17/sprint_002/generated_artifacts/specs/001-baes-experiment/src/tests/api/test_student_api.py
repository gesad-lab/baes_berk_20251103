```python
import pytest
from fastapi.testclient import TestClient
from src.api.student_api import app  # Assuming the FastAPI instance is in this module
from src.database import get_db, Database  # Assuming there's a database module

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    # Create a new in-memory database or use a test database
    test_db = Database()
    test_db.create_tables()
    yield test_db
    test_db.drop_tables()

def test_list_students_empty(db):
    # Test that the list of students is empty initially
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == []

def test_create_student_with_email(db):
    # Test the creation of a student with a valid email
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

def test_create_student_with_invalid_email(db):
    # Test the creation of a student with an invalid email format
    response = client.post("/students", json={"name": "John Doe", "email": "invalidemail"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}

def test_retrieve_student_with_email(db):
    # Test retrieving the student by ID
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

def test_retrieve_nonexistent_student(db):
    # Test retrieving a student that does not exist
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not found"}}

def test_list_students_with_emails(db):
    # Test listing all students, expecting one student to be present
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }]
```