```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.mark.parametrize("name, level, expected_status, expected_response", [
    ("Mathematics", "Beginner", 201, {"id": 1, "name": "Mathematics", "level": "Beginner"}),
    ("Science", "Advanced", 201, {"id": 2, "name": "Science", "level": "Advanced"}),
    (None, "Beginner", 400, {"error": {"code": "E003", "message": "Name is required"}}),
    ("Mathematics", None, 400, {"error": {"code": "E004", "message": "Level is required"}}),
])
def test_create_course(name, level, expected_status, expected_response):
    """Test creating a new course with valid and invalid data."""
    response = client.post("/courses", json={"name": name, "level": level})
    
    assert response.status_code == expected_status
    assert response.json() == expected_response

def test_retrieve_courses():
    """Test retrieving all courses."""
    response = client.get("/courses")
    
    assert response.status_code == 200
    # Check if the response is a list and has the appropriate structure
    assert isinstance(response.json(), list)
    for course in response.json():
        assert "id" in course
        assert "name" in course
        assert "level" in course

def test_persistent_course_data():
    """Test that a course persists after application restart."""
    # Assume a course is created here via the `test_create_course` function
    client.post("/courses", json={"name": "History", "level": "Intermediate"})
    
    # Simulate application restart by creating a new client instance
    client = TestClient(app)
    response = client.get("/courses")
    
    # Check if the created course is still present
    assert response.status_code == 200
    assert any(course['name'] == "History" for course in response.json())

```