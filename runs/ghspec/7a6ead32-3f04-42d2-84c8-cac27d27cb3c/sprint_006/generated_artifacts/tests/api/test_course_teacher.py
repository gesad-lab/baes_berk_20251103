```python
import json
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Course, Teacher

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
    course_response = client.post("/api/v1/courses", json={"title": "Physics 101"})
    assert course_response.status_code == 201
    return course_response.json()

def test_assign_teacher_to_course(client, setup_courses, setup_teachers):
    """Test assigning a teacher to a course."""
    course_id = setup_courses['id']
    teacher_id = setup_teachers['id']

    response = client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully."}

def test_view_course_with_teacher(client, setup_courses, setup_teachers):
    """Test retrieving a course and its associated teacher."""
    course_id = setup_courses['id']
    teacher_id = setup_teachers['id']
    
    # Assign teacher to course first
    client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})

    response = client.get(f"/api/v1/courses/{course_id}")
    
    assert response.status_code == 200
    course_data = response.json()
    assert course_data['teacher_id'] == teacher_id
    assert course_data['teacher']['name'] == "Jane Smith"
    assert course_data['teacher']['email'] == "jane.smith@example.com"

def test_assign_teacher_to_course_already_assigned(client, setup_courses, setup_teachers):
    """Test attempting to assign a teacher when one is already assigned."""
    course_id = setup_courses['id']
    teacher_id_1 = setup_teachers['id']
    
    # Assign first teacher to course
    client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id_1})

    # Create a different teacher for additional validation
    teacher_response_2 = client.post("/api/v1/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    teacher_id_2 = teacher_response_2.json()['id']
    
    response = client.put(f"/api/v1/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id_2})
    
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "A teacher is already assigned to this course."}}  

def test_assign_teacher_to_nonexistent_course(client):
    """Test assigning a teacher to a non-existent course."""
    response = client.put("/api/v1/courses/99999/assign_teacher", json={"teacher_id": 1})
    
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Course not found."}}

def test_view_nonexistent_course(client):
    """Test viewing a non-existent course."""
    response = client.get("/api/v1/courses/99999")
    
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Course not found."}}
```