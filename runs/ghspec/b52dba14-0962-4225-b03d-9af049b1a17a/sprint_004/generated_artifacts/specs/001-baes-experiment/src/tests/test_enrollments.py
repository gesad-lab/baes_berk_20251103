```python
import pytest
from flask import json
from src.api.enrollment_routes import add_course_to_student, get_student_courses, remove_course_from_student
from src.models.enrollment_model import Enrollment
from src.models.student_model import Student
from src.models.course_model import Course

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_add_course_to_student_with_valid_ids(client):
    """Test linking a valid course to a student successfully."""
    response = client.post('/students/1/courses', 
                           data=json.dumps({"course_id": 1}), 
                           content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == 'Course added to student successfully.'

def test_get_student_courses_with_valid_student_id(client):
    """Test retrieving courses for a valid student."""
    response = client.get('/students/1/courses')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Expecting a list of courses

def test_remove_course_from_student_with_valid_ids(client):
    """Test unlinking a valid course from a student successfully."""
    response = client.delete('/students/1/courses/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Course removed from student successfully.'

def test_add_course_to_student_with_invalid_student_id(client):
    """Test error handling when using an invalid student ID."""
    response = client.post('/students/999/courses', 
                           data=json.dumps({"course_id": 1}), 
                           content_type='application/json')
    assert response.status_code == 404
    assert response.json['error']['message'] == 'Invalid student ID.'

def test_add_course_to_student_with_invalid_course_id(client):
    """Test error handling when using an invalid course ID."""
    response = client.post('/students/1/courses', 
                           data=json.dumps({"course_id": 999}), 
                           content_type='application/json')
    assert response.status_code == 404
    assert response.json['error']['message'] == 'Invalid course ID.'
```