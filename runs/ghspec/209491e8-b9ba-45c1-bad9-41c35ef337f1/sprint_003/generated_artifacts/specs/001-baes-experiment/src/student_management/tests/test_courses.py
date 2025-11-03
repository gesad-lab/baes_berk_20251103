import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming app is imported from main.py
from src.models import Course  # Import the Course model
from src.database import get_db  # Import the database session

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture
def setup_database():
    # Setup code for database goes here, e.g., creating test records
    # Ensure the test database is clean before each test or ...
    pass

def test_create_course(client, setup_database):
    """Test creating a course with valid input."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert "id" in response.json()  # Assuming the response includes the course ID
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_retrieve_courses(client, setup_database):
    """Test retrieving all courses."""
    client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    client.post("/courses", json={"name": "Science", "level": "Intermediate"})
    
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of courses
    assert len(response.json()) == 2  # Expecting two courses created in the previous step

def test_create_course_missing_name(client, setup_database):
    """Test creating a course without a name."""
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400  # Bad request expected
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing fields: name",
            "details": {}
        }
    }

def test_create_course_missing_level(client, setup_database):
    """Test creating a course without a level."""
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400  # Bad request expected
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Missing fields: level",
            "details": {}
        }
    }