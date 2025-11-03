```python
import json
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Student, Course

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture
def student(client):
    """Create a test student for the API tests."""
    response = client.post("/api/v1/students", json={"name": "John Doe"})
    return response.json()

@pytest.fixture
def course(client):
    """Create a test course for the API tests."""
    response = client.post("/api/v1/courses", json={"name": "Math 101", "level": "Beginner"})
    return response.json()

def test_assign_courses_to_student(client, student, course):
    """Test assigning courses to a student successfully."""
    response = client.post(f"/api/v1/students/{student['id']}/courses", json={"course_ids": [course['id']]})
    assert response.status_code == 200
    assert response.json() == {
        "student_id": student['id'],
        "courses": [{"id": course['id'], "name": "Math 101", "level": "Beginner"}]
    }

def test_get_student_courses(client, student, course):
    """Test retrieving courses for a specific student."""
    client.post(f"/api/v1/students/{student['id']}/courses", json={"course_ids": [course['id']]})
    
    response = client.get(f"/api/v1/students/{student['id']}/courses")
    assert response.status_code == 200
    assert response.json() == {
        "student_id": student['id'],
        "courses": [{"id": course['id'], "name": "Math 101", "level": "Beginner"}]
    }

def test_remove_course_from_student(client, student, course):
    """Test removing a course from a student."""
    client.post(f"/api/v1/students/{student['id']}/courses", json={"course_ids": [course['id']]})
    
    response = client.delete(f"/api/v1/students/{student['id']}/courses/{course['id']}")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Course removed successfully."
    }

def test_assign_non_existing_course_to_student(client, student):
    """Test assigning a non-existing course to a student."""
    response = client.post(f"/api/v1/students/{student['id']}/courses", json={"course_ids": [999]})
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E404",
            "message": "Course not found."
        }
    }
```