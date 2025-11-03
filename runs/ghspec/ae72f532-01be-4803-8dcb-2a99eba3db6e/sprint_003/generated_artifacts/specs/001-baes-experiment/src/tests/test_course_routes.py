```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.mark.parametrize("course_name, course_level, expected_status, expected_response", [
    ("Mathematics", "Beginner", 201, {"id": 1, "name": "Mathematics", "level": "Beginner"}),
    ("History", "Intermediate", 201, {"id": 2, "name": "History", "level": "Intermediate"}),
])
def test_create_course(course_name, course_level, expected_status, expected_response):
    """Test creating a new course."""
    response = client.post("/courses/", json={"name": course_name, "level": course_level})
    assert response.status_code == expected_status
    assert response.json() == expected_response

def test_retrieve_courses():
    """Test retrieving all courses."""
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Validate response type
    # Verify if at least one course exists in the response
    assert len(response.json()) > 0

@pytest.mark.parametrize("course_data, expected_status, expected_error", [
    ({}, 400, {"error": {"code": "E001", "message": "Name is required"}}),  # Missing name
    ({"name": "Science"}, 400, {"error": {"code": "E002", "message": "Level is required"}}),  # Missing level
])
def test_create_course_missing_fields(course_data, expected_status, expected_error):
    """Test creating a course with missing fields."""
    response = client.post("/courses/", json=course_data)
    assert response.status_code == expected_status
    assert response.json() == expected_error

def test_course_data_persistence():
    """Test course data persistence after application restart."""
    initial_response = client.post("/courses/", json={"name": "Art", "level": "Advanced"})
    assert initial_response.status_code == 201
    created_course_id = initial_response.json()["id"]

    # Simulate application restart by creating a new TestClient
    client = TestClient(app)
    courses_response = client.get("/courses/")
    assert any(course["id"] == created_course_id for course in courses_response.json()), \
        "Created course was not found after restart"
```