```python
import pytest
from flask import json, Flask
from src.api.enrollment_routes import enrollment_blueprint
from src.models.student_model import Student
from src.models.course_model import Course
from src.models.enrollment_model import Enrollment  # Assuming this model exists for linking students and courses

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(enrollment_blueprint)
    
    # Setup database schema and seed data for tests
    with app.app_context():
        # Create tables and initial data here
        pass  

    yield app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_add_course_to_student(client):
    """Test adding a course to a student."""
    # Assuming a student and course already exist in the database
    student_id = 1
    course_id = 1
    
    response = client.post(f'/students/{student_id}/courses', 
                           data=json.dumps({"course_id": course_id}), 
                           content_type='application/json')
    
    assert response.status_code == 201
    assert response.json == {"message": f"Successfully enrolled student {student_id} in course {course_id}."}

def test_add_course_to_nonexistent_student(client):
    """Test adding a course to a non-existent student."""
    course_id = 1
    
    response = client.post('/students/999/courses',  # assuming 999 does not exist
                           data=json.dumps({"course_id": course_id}), 
                           content_type='application/json')

    assert response.status_code == 404
    assert response.json == {"error": {"code": "E404", "message": "Student not found."}}

def test_get_student_courses(client):
    """Test retrieving courses for a student."""
    student_id = 1
    
    response = client.get(f'/students/{student_id}/courses')

    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check the response is a list

def test_get_courses_for_nonexistent_student(client):
    """Test retrieving courses for a non-existent student."""
    response = client.get('/students/999/courses')  # assuming 999 does not exist
    
    assert response.status_code == 404
    assert response.json == {"error": {"code": "E404", "message": "Student not found."}}

def test_remove_course_from_student(client):
    """Test removing a course from a student."""
    student_id = 1
    course_id = 1  # Assuming this course is enrolled for the student

    response = client.delete(f'/students/{student_id}/courses/{course_id}')

    assert response.status_code == 204

def test_remove_course_from_nonexistent_student(client):
    """Test removing a course from a non-existent student."""
    response = client.delete('/students/999/courses/1')  # assuming 999 does not exist

    assert response.status_code == 404
    assert response.json == {"error": {"code": "E404", "message": "Student not found."}}

def test_remove_nonexistent_course_from_student(client):
    """Test removing a non-existent course from a student."""
    student_id = 1
    response = client.delete('/students/1/courses/999')  # assuming 999 does not exist in the course table

    assert response.status_code == 404
    assert response.json == {"error": {"code": "E404", "message": "Course not found."}}
```