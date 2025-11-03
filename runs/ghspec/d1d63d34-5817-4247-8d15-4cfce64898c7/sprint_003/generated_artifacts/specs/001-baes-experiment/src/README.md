import pytest
from fastapi.testclient import TestClient
from src.services.course_service import app, create_course, get_course, update_course, list_courses

client = TestClient(app)

@pytest.fixture
def sample_course():
    """Fixture for a sample course."""
    return {
        "name": "Mathematics 101",
        "level": "Beginner"
    }

def test_create_course(sample_course):
    """Test successful course creation with valid data."""
    response = client.post("/courses/", json=sample_course)
    assert response.status_code == 201
    assert response.json()["name"] == sample_course["name"]
    assert response.json()["level"] == sample_course["level"]

def test_get_course():
    """Test retrieving a course by ID."""
    # First, create a course to retrieve
    create_response = client.post("/courses/", json={"name": "Science 101", "level": "Intermediate"})
    course_id = create_response.json()["id"]

    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["id"] == course_id
    assert response.json()["name"] == "Science 101"
    assert response.json()["level"] == "Intermediate"

def test_update_course():
    """Test updating a course's details."""
    # First, create a course to update
    create_response = client.post("/courses/", json={"name": "History 101", "level": "Beginner"})
    course_id = create_response.json()["id"]

    # Now, update the course
    update_response = client.put(f"/courses/{course_id}", json={"name": "Advanced History", "level": "Advanced"})
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Advanced History"
    assert update_response.json()["level"] == "Advanced"

def test_list_courses():
    """Test listing all courses."""
    client.post("/courses/", json={"name": "Art 101", "level": "Beginner"})
    client.post("/courses/", json={"name": "Biology 101", "level": "Beginner"})

    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 2  # At least 2 courses should be listed
    assert all("name" in course for course in response.json())
    assert all("level" in course for course in response.json())