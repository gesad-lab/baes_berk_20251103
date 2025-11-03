```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is instantiated in src/main.py
from src.models import Course  # Import the Course model for testing

client = TestClient(app)

@pytest.fixture(scope="module")
def create_course():
    # Setup: Create a course in the database for testing
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    yield response.json()
    # Teardown: Cleanup created course after tests
    if response.status_code == 201:
        course_id = response.json().get("id")
        client.delete(f"/courses/{course_id}")  # Assuming the DELETE endpoint exists

def test_create_course():
    # Test creating a course successfully
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json()["name"] == "Math 101"
    assert response.json()["level"] == "Beginner"

def test_create_course_missing_fields():
    # Test creating a course without level
    response = client.post("/courses", json={"name": "Math 101"})
    assert response.status_code == 400
    assert "level" in response.json()["detail"][0]["loc"]

    # Test creating a course without name
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert "name" in response.json()["detail"][0]["loc"]

def test_retrieve_courses():
    # Test retrieving all courses
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of courses

def test_update_course(create_course):
    # Test updating the created course
    course_id = create_course['id']
    updated_data = {"name": "Advanced Math 101", "level": "Intermediate"}
    response = client.put(f"/courses/{course_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Advanced Math 101"
    assert response.json()["level"] == "Intermediate"
```