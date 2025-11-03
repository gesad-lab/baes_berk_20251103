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
def setup_students_and_courses(client):
    """Create test data for students and courses."""
    # Create a test course
    course_response = client.post("/api/v1/courses", json={"name": "Biology 101", "level": "Beginner"})
    assert course_response.status_code == 201
    course_id = course_response.json().get('id')
    
    # Create a test student
    student_response = client.post("/api/v1/students", json={"name": "John Doe"})
    assert student_response.status_code == 201
    student_id = student_response.json().get('id')

    return student_id, course_id

def test_assign_course_to_student(setup_students_and_courses, client):
    """Test assigning a course to a student."""
    student_id, course_id = setup_students_and_courses
    response = client.post(f"/api/v1/students/{student_id}/courses", json={"course_ids": [course_id]})
    
    assert response.status_code == 200
    assert response.json() == {
        "student_id": student_id,
        "courses": [{"course_id": course_id, "name": "Biology 101"}]
    }

def test_remove_course_from_student(setup_students_and_courses, client):
    """Test removing a course from a student."""
    student_id, course_id = setup_students_and_courses
    client.post(f"/api/v1/students/{student_id}/courses", json={"course_ids": [course_id]})  # Assign first
    
    response = client.delete(f"/api/v1/students/{student_id}/courses/{course_id}")
    assert response.status_code == 200
    assert response.json() == {
        "student_id": student_id,
        "removed_course_id": course_id
    }

def test_invalid_course_assignment(client):
    """Test assigning a non-existent course to a student."""
    student_id = 1  # Assume this student exists
    invalid_course_id = 999  # Assuming this course does not exist

    response = client.post(f"/api/v1/students/{student_id}/courses", json={"course_ids": [invalid_course_id]})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}

def test_student_courses_retrieval(setup_students_and_courses, client):
    """Test retrieving a student's courses."""
    student_id, course_id = setup_students_and_courses
    client.post(f"/api/v1/students/{student_id}/courses", json={"course_ids": [course_id]})  # Assign first
    
    response = client.get(f"/api/v1/students/{student_id}/courses")
    assert response.status_code == 200
    assert response.json() == {
        "student_id": student_id,
        "courses": [{"course_id": course_id, "name": "Biology 101"}]
    }
```