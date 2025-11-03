import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.database import init_db  # Assuming there's a function to initialize the database
from src.models.student import Student
from sqlalchemy.orm import Session
from src.db.database import get_db


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def db_session():
    # Initialize the database and create tables
    db = next(get_db())
    init_db(db)  # Assuming this function sets up the database schema
    yield db
    # Cleanup code can go here if necessary


def test_retrieve_all_students_empty(db_session, test_client):
    """Test case for retrieving all students when no students exist"""
    response = test_client.get("/students")
    assert response.status_code == 200
    assert response.json() == []


def test_create_student(db_session, test_client):
    """Test case for creating a student"""
    response = test_client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"


def test_retrieve_all_students_with_data(db_session, test_client):
    """Test case for retrieving all students after creation"""
    # Create a couple of students
    test_client.post("/students", json={"name": "Alice"})
    test_client.post("/students", json={"name": "Bob"})
    
    response = test_client.get("/students")
    assert response.status_code == 200
    students = response.json()
    assert len(students) == 2
    assert any(student['name'] == "Alice" for student in students)
    assert any(student['name'] == "Bob" for student in students)


def test_retrieve_student_by_id(db_session, test_client):
    """Test case for retrieving a specific student by ID"""
    response = test_client.post("/students", json={"name": "Charlie"})
    student_id = response.json()["id"]
    
    response = test_client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert response.json()["name"] == "Charlie"


def test_retrieve_student_not_found(db_session, test_client):
    """Test case for handling retrieval of a non-existent student"""
    response = test_client.get("/students/9999")  # Assuming this ID does not exist
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}