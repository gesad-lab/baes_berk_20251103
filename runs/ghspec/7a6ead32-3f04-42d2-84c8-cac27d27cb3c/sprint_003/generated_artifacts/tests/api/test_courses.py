```python
import json
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Course

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_create_course_with_valid_data(client):
    """Test creating a course with valid data."""
    response = client.post("/api/v1/courses", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json() == {"name": "Math 101", "level": "Beginner"}

def test_create_course_with_missing_fields(client):
    """Test creating a course with missing fields."""
    response = client.post("/api/v1/courses", json={"name": "", "level": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Both name and level must be provided"}}

def test_get_course(client):
    """Test retrieving a course by ID."""
    response_create = client.post("/api/v1/courses", json={"name": "Science 101", "level": "Intermediate"})
    course_id = response_create.json()["id"]
    
    response_get = client.get(f"/api/v1/courses/{course_id}")
    assert response_get.status_code == 200
    assert response_get.json() == {"id": course_id, "name": "Science 101", "level": "Intermediate"}

def test_update_course_with_valid_data(client):
    """Test updating a course with valid data."""
    response_create = client.post("/api/v1/courses", json={"name": "History 101", "level": "Advanced"})
    course_id = response_create.json()["id"]
    
    response_update = client.put(f"/api/v1/courses/{course_id}", json={"name": "History 102", "level": "Advanced"})
    assert response_update.status_code == 200
    assert response_update.json() == {"id": course_id, "name": "History 102", "level": "Advanced"}

def test_update_course_with_missing_fields(client):
    """Test updating a course with missing fields."""
    response_create = client.post("/api/v1/courses", json={"name": "English 101", "level": "Beginner"})
    course_id = response_create.json()["id"]

    response_update = client.put(f"/api/v1/courses/{course_id}", json={"name": "", "level": ""})
    assert response_update.status_code == 400
    assert response_update.json() == {"error": {"code": "E001", "message": "Both name and level must be provided"}}

def test_course_functionality_does_not_affect_students(client):
    """Test that existing student functionality remains unaffected by course endpoints."""
    # Create a student (Assumed functionality from existing tests)
    response_create_student = client.post("/api/v1/students", json={"email": "student@example.com"})
    assert response_create_student.status_code == 201
    
    # Verify that student was created successfully
    response_get_student = client.get("/api/v1/students")
    assert response_get_student.status_code == 200
    assert len(response_get_student.json()) == 1  # Ensure student count is 1
```