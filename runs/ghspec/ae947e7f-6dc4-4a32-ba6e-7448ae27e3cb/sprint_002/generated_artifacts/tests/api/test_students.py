```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_create_student_with_email(client):
    """
    Test creating a new student with valid data including email.
    """
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201  # 201 Created
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}


def test_create_student_missing_email(client):
    """
    Test creating a new student without an email.
    Expect a 400 Bad Request response.
    """
    response = client.post("/students", json={"name": "Jane Doe", "email": ""})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Email is required.",
            "details": {}
        }
    }


def test_create_student_duplicate_email(client):
    """
    Test creating a new student with a duplicate email.
    Expect a 400 Bad Request response.
    """
    client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    response = client.post("/students", json={"name": "John Smith", "email": "john@example.com"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Email already exists.",
            "details": {}
        }
    }


def test_get_student_by_id(client):
    """
    Test retrieving a created student by ID.
    Expect a successful response with the student's details.
    """
    create_response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    student_id = create_response.json()["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200  # 200 OK
    assert response.json() == {"id": student_id, "name": "John Doe", "email": "john@example.com"}


def test_get_student_not_found(client):
    """
    Test retrieving a student with a non-existing ID.
    Expect a 404 Not Found response.
    """
    response = client.get("/students/999")  # Assuming 999 does not exist
    assert response.status_code == 404  # 404 Not Found
    assert response.json() == {
        "error": {
            "code": "E003",
            "message": "Student not found.",
            "details": {}
        }
    }
```