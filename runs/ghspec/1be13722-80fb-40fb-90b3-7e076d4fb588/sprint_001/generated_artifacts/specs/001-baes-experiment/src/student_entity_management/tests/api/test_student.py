import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.database.db import init_db, get_db
from src.api.student import router as student_router
from src.models.student import Base, Student

# Create FastAPI instance and include the student router
app = FastAPI()
app.include_router(student_router)

# Setup Test Database - use an in-memory SQLite database for testing
@pytest.fixture(scope="module")
def test_app():
    # Create the database tables
    Base.metadata.create_all(bind=get_db())
    yield TestClient(app)
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=get_db())

# Integration tests for the student API
def test_create_student(test_app):
    # Test creating a new student
    response = test_app.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}

def test_get_students(test_app):
    # First, we create a student to test retrieving
    test_app.post("/students", json={"name": "Jane Doe"})
    
    # Now, we test the get operation
    response = test_app.get("/students")
    assert response.status_code == 200
    students = response.json()
    assert len(students) == 1
    assert students[0]["name"] == "Jane Doe"

def test_create_student_with_invalid_data(test_app):
    # Test creating a student with invalid data (missing name)
    response = test_app.post("/students", json={})
    assert response.status_code == 422  # Unprocessable Entity

def test_get_non_existent_student(test_app):
    # Test retrieving a non-existent student (empty DB scenario)
    response = test_app.get("/students")
    assert response.status_code == 200
    assert response.json() == []  # Expecting empty list if no students exist

def test_create_multiple_students(test_app):
    # Test creating multiple students
    student_names = ["Alice", "Bob", "Charlie"]
    for name in student_names:
        response = test_app.post("/students", json={"name": name})
        assert response.status_code == 201
    # Validate that the students were created
    response = test_app.get("/students")
    assert len(response.json()) == len(student_names)

def test_student_retrieval_after_multiple_creations(test_app):
    # After multiple creations, check retrieval again
    response = test_app.get("/students")
    student_names = ["John Doe", "Jane Doe", "Alice", "Bob", "Charlie"]
    response_students = [student["name"] for student in response.json()]
    
    # Check if all created students exist in the response
    for name in student_names:
        assert name in response_students
```