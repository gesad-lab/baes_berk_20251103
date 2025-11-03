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
    """Test creating a new course with valid data."""
    response = client.post("/api/v1/courses", json={"name": "Data Science 101", "level": "Beginner"})
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_course(client):
    """Test retrieving an existing course by ID."""
    # Assuming a course with ID 1 has been created in the database for testing purposes
    response = client.get("/api/v1/courses/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Data Science 101"


def test_get_non_existent_course(client):
    """Test retrieving a non-existent course by ID returns 404."""
    response = client.get("/api/v1/courses/999")  # Assuming 999 is invalid
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}


def test_create_course_with_invalid_data(client):
    """Test that creating a course with invalid data returns a validation error."""
    response = client.post("/api/v1/courses", json={"name": "", "level": "Beginner"})  # Invalid name
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"error": {"code": "E422", "message": "Invalid input data", "details": {"name": ["field required"]}}}

```