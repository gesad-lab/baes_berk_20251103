```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py

@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client


def test_create_course(client):
    """Test creating a new course with valid name and level."""
    response = client.post("/api/v1/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201  # Expect created status
    assert "id" in response.json()  # Ensure there is a returned course ID
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"


def test_retrieve_course(client):
    """Test retrieving an existing course by its ID."""
    # First, create a course to retrieve
    create_response = client.post("/api/v1/courses", json={"name": "Physics", "level": "Intermediate"})
    course_id = create_response.json()["id"]

    response = client.get(f"/api/v1/courses/{course_id}")
    assert response.status_code == 200  # Expect OK status
    assert response.json()["name"] == "Physics"
    assert response.json()["level"] == "Intermediate"


def test_update_course(client):
    """Test updating an existing course's name and level."""
    # Create a course to update
    create_response = client.post("/api/v1/courses", json={"name": "Chemistry", "level": "Advanced"})
    course_id = create_response.json()["id"]

    response = client.put(f"/api/v1/courses/{course_id}", json={"name": "Advanced Chemistry", "level": "Expert"})
    assert response.status_code == 200  # Expect OK status
    assert response.json()["name"] == "Advanced Chemistry"
    assert response.json()["level"] == "Expert"


def test_create_course_without_fields(client):
    """Test error handling when required fields are missing."""
    response = client.post("/api/v1/courses", json={})
    assert response.status_code == 400  # Expect bad request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Missing required fields: name, level",
            "details": {}
        }
    }


def test_retrieve_nonexistent_course(client):
    """Test retrieving a course that does not exist."""
    response = client.get("/api/v1/courses/999")  # Assuming 999 does not exist
    assert response.status_code == 404  # Expect not found
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Course not found",
            "details": {}
        }
    }
```