```python
import pytest
from fastapi.testclient import TestClient
from src.services.course_service import app, create_course, update_course
from pydantic import ValidationError

client = TestClient(app)

@pytest.fixture
def sample_course():
    return {
        "name": "Introduction to Python",
        "level": "Beginner"
    }

def test_create_course(sample_course):
    """Test successful course creation with valid data."""
    response = client.post("/courses/", json=sample_course)
    assert response.status_code == 201
    assert response.json()["name"] == sample_course["name"]
    assert response.json()["level"] == sample_course["level"]

def test_create_course_missing_name():
    """Test course creation fails when name is missing."""
    response = client.post("/courses/", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Missing required field: name", "details": {}}}

def test_create_course_missing_level():
    """Test course creation fails when level is missing."""
    response = client.post("/courses/", json={"name": "Introduction to Python"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Missing required field: level", "details": {}}}

def test_update_course(sample_course):
    """Test successful course update with valid data."""
    created_response = client.post("/courses/", json=sample_course)
    course_id = created_response.json()["id"]
    
    update_data = {"name": "Advanced Python"}
    response = client.put(f"/courses/{course_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == update_data["name"]
    assert response.json()["level"] == sample_course["level"]  # Level remains unchanged

def test_update_course_invalid_id():
    """Test course update fails with a non-existent course ID."""
    response = client.put("/courses/999", json={"name": "Advanced Python"})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Course not found", "details": {}}}

def test_update_course_missing_fields():
    """Test course update fails when no fields are provided."""
    created_response = client.post("/courses/", json=sample_course)
    course_id = created_response.json()["id"]
    
    response = client.put(f"/courses/{course_id}", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E004", "message": "No fields to update passed", "details": {}}}
```