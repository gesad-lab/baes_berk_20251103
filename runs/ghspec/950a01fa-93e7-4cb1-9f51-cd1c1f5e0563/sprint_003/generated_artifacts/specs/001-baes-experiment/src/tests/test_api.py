```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in src/main.py
from src.db import init_db, shutdown_db  # Database management functions
from src.models import Course  # Assuming you have a Course model

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Set up the database for testing."""
    init_db()
    yield
    shutdown_db()

@pytest.fixture
def client():
    """Create a TestClient for the FastAPI app."""
    with TestClient(app) as client:
        yield client

def test_create_course(client):
    """Test creating a new course."""
    response = client.post("/api/v1/courses", json={"title": "Test Course", "description": "Test Description"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "title": "Test Course", "description": "Test Description"}  # Adjust based on actual response

def test_create_course_with_invalid_data(client):
    """Test creating a new course with invalid data."""
    response = client.post("/api/v1/courses", json={"title": "", "description": "Test Description"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Title cannot be empty", "details": {}}}  # Adjust based on actual error response

def test_get_course(client):
    """Test retrieving a course by ID."""
    # First create a course to get it by ID
    response = client.post("/api/v1/courses", json={"title": "Test Course", "description": "Test Description"})
    course_id = response.json()["id"]
    
    response = client.get(f"/api/v1/courses/{course_id}")
    assert response.status_code == 200
    assert response.json() == {"id": course_id, "title": "Test Course", "description": "Test Description"}  # Adjust based on actual response

def test_get_non_existent_course(client):
    """Test retrieving a course that does not exist."""
    response = client.get("/api/v1/courses/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Course not found", "details": {}}}  # Adjust based on actual error response
```