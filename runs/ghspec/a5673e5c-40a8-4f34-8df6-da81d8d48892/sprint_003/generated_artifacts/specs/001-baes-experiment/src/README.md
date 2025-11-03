```
# File: tests/test_api.py

import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.schemas import CourseCreate, CourseUpdate
from src.models import Course  # Assuming a Course model is defined in models.py

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Sets up the database for testing."""
    # Setup code to initialize the database goes here.
    # This could involve creating tables, seeding initial data, etc.
    yield
    # Code to teardown the database goes here.

def test_create_course():
    """Test the creation of a course."""
    response = client.post("/api/courses", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json() == {"name": "Math 101", "level": "Beginner"}

def test_create_course_missing_name():
    """Test creating a course with missing name."""
    response = client.post("/api/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required.", "details": {}}}

def test_create_course_missing_level():
    """Test creating a course with missing level."""
    response = client.post("/api/courses", json={"name": "Math 101"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Level is required.", "details": {}}}

def test_retrieve_course():
    """Test retrieving a course by ID."""
    # First, create a course to retrieve
    course_response = client.post("/api/courses", json={"name": "Science 101", "level": "Intermediate"})
    course_id = course_response.json().get("id")

    response = client.get(f"/api/courses/{course_id}")
    assert response.status_code == 200
    assert response.json() == {"id": course_id, "name": "Science 101", "level": "Intermediate"}

def test_update_course_level():
    """Test updating a course's level."""
    # First, create a course to update
    course_response = client.post("/api/courses", json={"name": "History 101", "level": "Basic"})
    course_id = course_response.json().get("id")

    response = client.put(f"/api/courses/{course_id}", json={"level": "Advanced"})
    assert response.status_code == 200
    updated_course = response.json()
    assert updated_course["level"] == "Advanced"

    # Verify the course was updated correctly
    retrieve_response = client.get(f"/api/courses/{course_id}")
    assert retrieve_response.json()["level"] == "Advanced"
```