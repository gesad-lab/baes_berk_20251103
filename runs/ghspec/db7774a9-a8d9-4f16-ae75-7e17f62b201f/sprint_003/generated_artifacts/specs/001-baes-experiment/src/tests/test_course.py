```python
# tests/test_course.py

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_course():
    """Test creating a course with valid name and level."""
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Math 101"
    assert response.json()["level"] == "Beginner"

def test_create_course_missing_name():
    """Test creating a course without a name should fail."""
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"

def test_create_course_missing_level():
    """Test creating a course without a level should fail."""
    response = client.post("/courses", json={"name": "Math 101"})
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"

def test_retrieve_course():
    """Test retrieving a course by ID after creating one."""
    # First create a course to retrieve it
    create_response = client.post("/courses", json={"name": "Science 101", "level": "Intermediate"})
    course_id = create_response.json()["id"]

    # Now retrieve the created course
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["id"] == course_id
    assert response.json()["name"] == "Science 101"
    assert response.json()["level"] == "Intermediate"

def test_retrieve_nonexistent_course():
    """Test retrieving a course with a nonexistent ID should return 404."""
    response = client.get("/courses/99999")
    assert response.status_code == 404

def test_list_courses():
    """Test listing all courses."""
    # Creating some courses for the list
    client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    client.post("/courses", json={"name": "History 101", "level": "Advanced"})

    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 2  # Expect at least two courses
```