```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_create_course_with_valid_data(client):
    """
    Test creating a new course with valid data.
    """
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201  # 201 Created
    assert "id" in response.json()  # Verify that the response includes the course ID
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_create_course_with_missing_name(client):
    """
    Test creating a course without a name should return an error.
    """
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 422  # 422 Unprocessable Entity
    assert response.json()["detail"]  # Validation error details should be provided

def test_create_course_with_missing_level(client):
    """
    Test creating a course without a level should return an error.
    """
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 422  # 422 Unprocessable Entity
    assert response.json()["detail"]  # Validation error details should be provided

def test_get_course_by_id(client):
    """
    Test retrieving a course by ID.
    """
    # First, create a course to retrieve
    create_response = client.post("/courses", json={"name": "Science", "level": "Intermediate"})
    course_id = create_response.json()["id"]

    # Now retrieve the course
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200  # 200 OK
    assert response.json()["name"] == "Science"
    assert response.json()["level"] == "Intermediate"

def test_get_course_by_invalid_id(client):
    """
    Test retrieving a course with a non-existent ID should return a 404 error.
    """
    response = client.get("/courses/9999")  # Assuming this ID does not exist
    assert response.status_code == 404  # 404 Not Found
    assert response.json()["detail"] == "Course not found"  # Custom message from your API
```