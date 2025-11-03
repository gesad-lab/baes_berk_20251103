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
    # Test that the List Students endpoint returns an empty list when no students exist
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == []

def test_create_student(db):
    # Test creating a new student
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert "id" in response.json()  # Expecting the response to contain an ID
    assert response.json()["name"] == "John Doe"

def test_list_students_after_creation(db):
    # Ensure that after creating a student we can retrieve them in the list
    client.post("/students", json={"name": "John Doe"})
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "John Doe"

def test_create_student_empty_name(db):
    # Test creating a student with empty name should fail
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 422  # Unprocessable Entity

def test_list_students_multiple(db):
    # Test creating multiple students and retrieving them
    client.post("/students", json={"name": "Alice"})
    client.post("/students", json={"name": "Bob"})
    
    response = client.get("/students")
    assert response.status_code == 200
    students = response.json()
    assert len(students) == 3  # Including John Doe, Alice, and Bob
    names = {student["name"] for student in students}
    assert "John Doe" in names
    assert "Alice" in names
    assert "Bob" in names

# Test retrieval of specific student (for future implementation)
def test_retrieve_student(db):
    response = client.post("/students", json={"name": "Charlie"})
    student_id = response.json()["id"]
    
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Charlie"

def test_retrieve_student_not_found(db):
    # Test retrieving a non-existing student
    response = client.get("/students/9999")
    assert response.status_code == 404  # Not Found
    assert response.json() == {"detail": "Student not found"}  # Adjust based on actual API error response structure