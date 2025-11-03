```python
import pytest
from fastapi.testclient import TestClient
from src.api import app
from src.course_service import create_course, get_course, update_course 

client = TestClient(app)

@pytest.fixture
def setup_course():
    """Fixture to create a sample course for tests."""
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    course_data = response.json()
    yield course_data["id"]  # Return course ID for tests
    client.delete(f"/courses/{course_data['id']}")  # Clean up after tests

def test_create_course(setup_course):
    """Test creating a new course."""
    course_id = setup_course
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Math 101"

def test_update_course(setup_course):
    """Test updating an existing course."""
    course_id = setup_course
    response = client.put(f"/courses/{course_id}", json={"name": "Math 201", "level": "Intermediate"})
    assert response.status_code == 200
    assert response.json()["name"] == "Math 201"

def test_create_course_invalid_input():
    """Test creating a course with invalid input."""
    response = client.post("/courses", json={"name": "", "level": ""})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"
    assert "Course name and level are required." in response.json()["error"]["message"]

def test_get_course():
    """Test retrieving a specific course by ID."""
    response = client.post("/courses", json={"name": "Science 101", "level": "Beginner"})
    course_data = response.json()
    course_id = course_data["id"]

    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Science 101"

    # Clean up after test
    client.delete(f"/courses/{course_id}")
```