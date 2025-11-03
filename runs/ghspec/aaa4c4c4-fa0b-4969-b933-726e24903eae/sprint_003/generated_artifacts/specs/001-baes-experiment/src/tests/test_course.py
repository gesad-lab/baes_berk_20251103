```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is created in main.py

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """This fixture would typically configure and initialize the database.
    Implementation depends on your specific setup and testing requirements.
    """
    pass

def test_create_course_success(setup_database):
    """Test creating a course successfully."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Intermediate"})
    assert response.status_code == 201
    course = response.json()
    assert "id" in course
    assert course["name"] == "Mathematics"
    assert course["level"] == "Intermediate"

def test_create_course_missing_name(setup_database):
    """Test creating a course without a name should return a 400 error."""
    response = client.post("/courses", json={"level": "Intermediate"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Missing required field: name"}}

def test_create_course_missing_level(setup_database):
    """Test creating a course without a level should return a 400 error."""
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Missing required field: level"}}

def test_get_all_courses_empty(setup_database):
    """Test retrieving all courses when none exist should return an empty list."""
    response = client.get("/courses")
    assert response.status_code == 200
    assert response.json() == []  # Expecting an empty list

def test_get_all_courses_with_data(setup_database):
    """Test retrieving all courses after adding some courses."""
    client.post("/courses", json={"name": "Mathematics", "level": "Intermediate"})
    client.post("/courses", json={"name": "Physics", "level": "Advanced"})

    response = client.get("/courses")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) == 2
    assert courses[0]["name"] == "Mathematics"
    assert courses[1]["name"] == "Physics"
```