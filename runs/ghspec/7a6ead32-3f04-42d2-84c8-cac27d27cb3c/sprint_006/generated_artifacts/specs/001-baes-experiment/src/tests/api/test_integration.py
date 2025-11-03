```python
import json
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Teacher, Course

@pytest.fixture
def client():
    """Fixture to create a test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

@pytest.fixture
def setup_teachers(client):
    """Create test data for teachers."""
    teacher_response = client.post("/api/v1/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    assert teacher_response.status_code == 201
    return teacher_response.json()

@pytest.fixture
def setup_courses(client, setup_teachers):
    """Create test data for courses."""
    course_response = client.post("/api/v1/courses", json={"title": "Math 101"})
    assert course_response.status_code == 201
    return course_response.json()

def test_assign_teacher_to_course(client, setup_courses, setup_teachers):
    """Test assigning a teacher to a course with valid inputs."""
    course_id = setup_courses['id']
    teacher_id = setup_teachers['id']
    
    response = client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Teacher assigned successfully",
        "course_id": course_id,
        "teacher_id": teacher_id
    }

def test_assign_teacher_with_invalid_id(client, setup_courses):
    """Test assigning a teacher to a course with an invalid teacher ID."""
    course_id = setup_courses['id']
    invalid_teacher_id = 9999  # Assuming this ID does not exist
    
    response = client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": invalid_teacher_id})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Invalid Teacher ID provided",
            "details": {}
        }
    }

def test_assign_teacher_to_already_assigned_course(client, setup_courses, setup_teachers):
    """Test assigning a new teacher to a course that already has an assigned teacher."""
    course_id = setup_courses['id']
    teacher_id = setup_teachers['id']
    
    # First assignment
    client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})
    
    new_teacher_response = client.post("/api/v1/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    new_teacher_id = new_teacher_response.json()['id']

    # Attempting to assign a second teacher
    response = client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": new_teacher_id})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Course already has an assigned teacher",
            "details": {}
        }
    }

def test_get_course_with_teacher(client, setup_courses, setup_teachers):
    """Test retrieving course details including assigned teacher information."""
    course_id = setup_courses['id']
    teacher_id = setup_teachers['id']
    client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})

    response = client.get(f"/api/v1/courses/{course_id}")
    assert response.status_code == 200
    course_info = response.json()
    
    assert course_info['id'] == course_id
    assert course_info['teacher'] == {
        "id": teacher_id,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
```