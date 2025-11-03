import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.database import initialize_database, Student
from sqlalchemy.orm import Session
from src.database import get_db


@pytest.fixture(scope="module")
def test_client():
    """Fixture for creating a test client."""
    initialize_database()  # Ensure the database is initialized before tests
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def db_session():
    """Fixture for creating a database session."""
    db: Session = next(get_db())
    yield db
    db.close()


def test_create_student_success(test_client):
    """Testing successful creation of a student."""
    response = test_client.post("/students/", json={"name": "John Doe", "age": 22})
    assert response.status_code == 201
    assert response.json() == {"message": "Student created successfully", "student": response.json()["student"]}


def test_create_student_missing_name(test_client):
    """Testing student creation with missing name."""
    response = test_client.post("/students/", json={"age": 22})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name field is required.", "details": {}}}


def test_retrieve_students_success(test_client):
    """Testing retrieval of all students."""
    response = test_client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of students


def test_database_initialized(db_session):
    """Testing if the database and Student table are created correctly."""
    assert db_session.query(Student).count() == 0  # Initially, there should be no students
