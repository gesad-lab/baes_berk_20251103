import pytest
from fastapi.testclient import TestClient
from src.api.student import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database(db_session):
    """
    Run before each test to ensure a clean database state.
    You can implement this fixture to initialize the DB if needed.
    """
    pass  # This could be used to add seed data if necessary


def test_create_student_success():
    """
    Test whether a student can be successfully created.
    """
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # Expecting 201 Created
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"

def test_retrieve_students_success():
    """
    Test if all students can be retrieved successfully.
    """
    client.post("/students", json={"name": "John Doe"})
    client.post("/students", json={"name": "Jane Doe"})
    
    response = client.get("/students")
    assert response.status_code == 200  # Expecting 200 OK
    students = response.json()
    assert len(students) == 2  # Ensure we have two students
    assert any(student["name"] == "John Doe" for student in students)
    assert any(student["name"] == "Jane Doe" for student in students)

def test_create_student_empty_name():
    """
    Test whether trying to create a student with an empty name returns a proper error response.
    """
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400  # Expecting 400 Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name cannot be empty.",
            "details": {}
        }
    }
