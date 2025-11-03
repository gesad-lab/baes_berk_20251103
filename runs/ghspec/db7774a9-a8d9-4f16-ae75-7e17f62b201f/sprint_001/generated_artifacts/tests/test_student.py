import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture()
def create_student():
    """Fixture to create a student for testing."""
    response = client.post("/students", json={"name": "John Doe"})
    return response.json()

def test_create_student():
    """Test creating a student with a valid name."""
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Jane Doe"

def test_create_student_with_empty_name():
    """Test creating a student with an empty name."""
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name field is required.", "details": {}}}

def test_list_students(create_student):
    """Test listing all students."""
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list
    assert any(student['name'] == "John Doe" for student in response.json())  # Check if the created student is in the list

def test_retrieve_student(create_student):
    """Test retrieving a student by ID."""
    student_id = create_student['id']
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert response.json()["name"] == "John Doe"

def test_retrieve_student_not_found():
    """Test retrieving a student that does not exist."""
    response = client.get("/students/999")  # Assuming 999 does not exist
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not found.", "details": {}}}