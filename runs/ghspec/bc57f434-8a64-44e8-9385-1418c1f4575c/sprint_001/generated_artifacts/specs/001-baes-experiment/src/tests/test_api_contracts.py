import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Setup the test database and create test data
    with TestClient(app) as client:
        yield client  # Provide the client to the tests


def test_create_student(setup_database):
    response = setup_database.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}


def test_create_student_missing_name(setup_database):
    response = setup_database.post("/students", json={})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required field: name",
            "details": {}
        }
    }


def test_get_student(setup_database):
    # First create a student
    create_response = setup_database.post("/students", json={"name": "Jane Doe"})
    student_id = create_response.json()["id"]

    # Now retrieve the student
    response = setup_database.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == {"id": student_id, "name": "Jane Doe"}


def test_get_nonexistent_student(setup_database):
    response = setup_database.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Student not found",
            "details": {}
        }
    }


def test_update_student(setup_database):
    # First create a student
    create_response = setup_database.post("/students", json={"name": "Alice Smith"})
    student_id = create_response.json()["id"]

    # Now update their name
    response = setup_database.put(f"/students/{student_id}", json={"name": "Alice Johnson"})
    assert response.status_code == 200
    assert response.json() == {"id": student_id, "name": "Alice Johnson"}


def test_delete_student(setup_database):
    # First create a student
    create_response = setup_database.post("/students", json={"name": "Bob Brown"})
    student_id = create_response.json()["id"]

    # Now delete the student
    response = setup_database.delete(f"/students/{student_id}")
    assert response.status_code == 204  # No Content


def test_delete_nonexistent_student(setup_database):
    response = setup_database.delete("/students/999")
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Student not found",
            "details": {}
        }
    }