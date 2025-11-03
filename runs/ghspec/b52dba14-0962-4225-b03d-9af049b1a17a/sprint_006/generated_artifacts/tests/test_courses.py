```python
import pytest
from flask import json
from src.api.course_routes import assign_teacher_to_course
from src.models.course_model import Course
from src.models.teacher_model import Teacher
from src.services.course_service import CourseService
from src.services.teacher_service import TeacherService

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture
def create_teacher(client):
    """Helper fixture to create a teacher for testing."""
    teacher_data = {"name": "Jane Smith", "email": "jane.smith@example.com"}
    response = client.post('/teachers', json=teacher_data)
    assert response.status_code == 201
    return response.get_json()

@pytest.fixture
def create_course(client):
    """Helper fixture to create a course for testing."""
    course_data = {"title": "Mathematics 101", "description": "Introduction to Mathematics"}
    response = client.post('/courses', json=course_data)
    assert response.status_code == 201
    return response.get_json()

def test_assign_teacher_to_course(client, create_teacher, create_course):
    """Test assigning a teacher to a course successfully."""
    teacher_id = create_teacher['id']
    course_id = create_course['id']
    
    response = client.post(f'/courses/{course_id}/assign-teacher', json={"teacher_id": teacher_id})
    
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['message'] == "Teacher assigned to course successfully."
    
    # Fetch the course to verify the assignment
    updated_course = client.get(f'/courses/{course_id}')
    assert updated_course.status_code == 200
    assert updated_course.get_json()['teacher_id'] == teacher_id

def test_assign_teacher_to_non_existent_course(client, create_teacher):
    """Test assigning a teacher to a non-existent course."""
    teacher_id = create_teacher['id']
    non_existent_course_id = 99999  # Arbitrary non-existent course ID
    
    response = client.post(f'/courses/{non_existent_course_id}/assign-teacher', json={"teacher_id": teacher_id})
    
    assert response.status_code == 404
    response_data = response.get_json()
    assert response_data['error'] == {"code": "E404", "message": "Course not found."}

def test_assign_non_existent_teacher_to_course(client, create_course):
    """Test assigning a non-existent teacher to a course."""
    course_id = create_course['id']
    non_existent_teacher_id = 99999  # Arbitrary non-existent teacher ID
    
    response = client.post(f'/courses/{course_id}/assign-teacher', json={"teacher_id": non_existent_teacher_id})
    
    assert response.status_code == 404
    response_data = response.get_json()
    assert response_data['error'] == {"code": "E404", "message": "Teacher not found."}
```