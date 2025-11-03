```python
import pytest
from fastapi.testclient import TestClient
from myapp.main import app  # Assuming your FastAPI app is instantiated in main.py

client = TestClient(app)

def test_create_course_with_valid_data():
    """Test creating a course with valid name and level."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201  # Expecting 201 Created
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_create_course_without_name():
    """Test creating a course without a name."""
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400  # Expecting 400 Bad Request
    assert response.json()["error"]["code"] == "E001"  # Assuming E001 for missing name

def test_create_course_without_level():
    """Test creating a course without a level."""
    response = client.post("/courses", json={"name": "Science"})
    assert response.status_code == 400  # Expecting 400 Bad Request
    assert response.json()["error"]["code"] == "E002"  # Assuming E002 for missing level

def test_get_courses_empty():
    """Test getting courses when no courses exist."""
    response = client.get("/courses")
    assert response.status_code == 200  # Expecting 200 OK
    assert response.json() == []  # Expecting an empty list

def test_get_courses_with_course():
    """Test getting courses when there are existing courses."""
    client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    response = client.get("/courses")
    assert response.status_code == 200  # Expecting 200 OK
    assert len(response.json()) == 1  # Expecting only one course
    assert response.json()[0]["name"] == "Mathematics"
    assert response.json()[0]["level"] == "Beginner"
```