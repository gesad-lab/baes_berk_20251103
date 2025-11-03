```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from pydantic import BaseModel, EmailStr

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Set up any necessary database state before tests
    yield
    # Clean up database state after tests

# Pydantic models for Course creation
class CourseCreate(BaseModel):
    name: str
    level: str  # Required field for course creation

def test_create_course_success(setup_database):
    """Test that creating a course successfully returns the expected course object."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_create_course_missing_fields(setup_database):
    """Test that creating a course without required fields returns a 400 error."""
    response = client.post("/courses", json={"name": ""})
    assert response.status_code == 400
    assert "error" in response.json()

def test_get_course_by_id_success(setup_database):
    """Test that retrieving a course by its ID returns the expected course object."""
    response = client.post("/courses", json={"name": "Science", "level": "Intermediate"})
    course_id = response.json().get("id")

    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["id"] == course_id
    assert response.json()["name"] == "Science"
    assert response.json()["level"] == "Intermediate"

def test_get_course_by_id_not_found(setup_database):
    """Test that retrieving a course by a nonexistent ID returns a 404 error."""
    response = client.get("/courses/9999")
    assert response.status_code == 404
    assert "error" in response.json()
```