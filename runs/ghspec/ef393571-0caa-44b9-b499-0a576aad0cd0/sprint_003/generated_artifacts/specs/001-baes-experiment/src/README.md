```python
import pytest
from fastapi.testclient import TestClient
from myapp.main import app  # Assuming your FastAPI app is defined in main.py

client = TestClient(app)

def test_add_course_with_valid_data():
    """Test adding a course with valid name and level."""
    response = client.post("/courses", json={"name": "Biology 101", "level": "Beginner"})
    assert response.status_code == 201  # Assuming 201 Created is expected
    assert response.json()["name"] == "Biology 101"
    assert response.json()["level"] == "Beginner"

def test_add_course_without_name():
    """Test adding a course without a name."""
    response = client.post("/courses", json={"level": "Basic"})
    assert response.status_code == 400  # Expecting Bad Request
    assert response.json()["error"]["code"] == "E001"  # Code for missing name
    assert response.json()["error"]["message"] == "Course name is required."  # Expected error message

def test_add_course_without_level():
    """Test adding a course without a level."""
    response = client.post("/courses", json={"name": "Physics 101"})
    assert response.status_code == 400  # Expecting Bad Request
    assert response.json()["error"]["code"] == "E002"  # Code for missing level
    assert response.json()["error"]["message"] == "Course level is required."  # Expected error message

def test_retrieve_courses():
    """Test retrieving all courses."""
    response = client.get("/courses")
    assert response.status_code == 200  # Expecting success
    assert isinstance(response.json(), list)  # Expecting a list of courses
    # Additional asserts can check for expected structure of course objects
```