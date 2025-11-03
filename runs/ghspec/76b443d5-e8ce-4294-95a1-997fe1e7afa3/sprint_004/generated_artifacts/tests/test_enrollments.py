```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Course  # Ensure proper import of course model
from sqlalchemy.orm import Session
from src.database import get_db  # Dependency for database session

@pytest.fixture
def client():
    """Fixture for the test client."""
    with TestClient(app) as client:
        yield client

@pytest.fixture
def course_data():
    """Fixture for a sample course data."""
    return {
        "id": "some_course_id",
        "title": "Sample Course",
        "description": "A course for testing purposes."
    }

def test_get_courses(client):
    """Test retrieving all courses."""
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expect a list of courses

def test_get_course(client, course_data):
    """Test retrieving a single course by ID."""
    # First, we need to assume the course exists in our test DB.
    client.post("/courses", json=course_data)  # Create a course for testing

    response = client.get(f"/courses/{course_data['id']}")
    assert response.status_code == 200
    assert response.json() == {
        "id": course_data["id"],
        "title": course_data["title"],
        "description": course_data["description"]
    }

def test_get_course_not_found(client):
    """Test retrieving a course that does not exist."""
    response = client.get("/courses/invalid_course_id")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Course not found."}}

def test_get_courses_empty(client):
    """Test retrieving courses when none exist."""
    response = client.get("/courses")
    assert response.status_code == 200
    assert response.json() == []  # Expect an empty list if no courses are created
```