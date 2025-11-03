import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Here, you would set up a fresh database state for the tests.
    # This includes potentially creating records necessary for testing.
    pass

def test_create_teacher_success():
    # Test successful creation of a Teacher
    response = client.post("/teachers", json={"name": "John Doe", "email": "johndoe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"name": "John Doe", "email": "johndoe@example.com"}

def test_create_teacher_duplicate_email():
    # Test creating a Teacher with a duplicate email
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "johndoe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email already exists.", "details": {}}}

def test_get_teacher_success():
    # Test retrieval of a Teacher by ID (assuming the ID of the created teacher is 1)
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "johndoe@example.com"}

def test_get_teacher_not_found():
    # Test retrieving a Teacher that does not exist
    response = client.get("/teachers/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Teacher not found.", "details": {}}}