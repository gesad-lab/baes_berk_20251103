```python
import pytest
from flask import json
from your_application import create_app  # import your app factory function
from your_application.models import db, Course, Student, StudentCourse  # import Course, Student and StudentCourse models
from your_application.database import init_db  # import your database initialization function

@pytest.fixture
def app():
    """Create a Flask application for testing."""
    app = create_app('TEST')  # Use the testing configuration
    with app.app_context():
        init_db()  # Initialize the database
        # Create initial data for testing
        student = Student(name='Test Student')
        course = Course(name='Test Course')
        db.session.add(student)
        db.session.add(course)
        db.session.commit()
        yield app

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

def test_associate_course_with_student(client):
    """Test associating a course with a student."""
    student = Student.query.first()
    course = Course.query.first()

    # Perform POST request to associate the course
    response = client.post(f'/students/{student.id}/courses', json={'course_id': course.id})

    assert response.status_code == 201  # Check for created status
    assert b'Course associated successfully' in response.data  # Check response message

    # Validate that the association is created in the database
    association = StudentCourse.query.filter_by(student_id=student.id, course_id=course.id).first()
    assert association is not None  # Ensure the association exists

def test_get_courses_for_student(client):
    """Test retrieving all courses associated with a student."""
    student = Student.query.first()
    course = Course.query.first()
    
    # First, associate a course with student
    client.post(f'/students/{student.id}/courses', json={'course_id': course.id})

    # Perform GET request to retrieve courses
    response = client.get(f'/students/{student.id}/courses')

    assert response.status_code == 200  # Check for OK status
    data = json.loads(response.data)
    assert len(data['courses']) == 1  # Expect one course associated
    assert data['courses'][0]['id'] == course.id  # Check course ID matches

def test_associate_invalid_course(client):
    """Test associating an invalid course with a student returns an error."""
    student = Student.query.first()

    # Perform POST request with invalid course ID
    response = client.post(f'/students/{student.id}/courses', json={'course_id': 999})

    assert response.status_code == 400  # Check for bad request status
    assert b'Invalid course ID' in response.data  # Check error message

def test_get_courses_for_nonexistent_student(client):
    """Test retrieving courses for a nonexistent student returns an error."""
    # Perform GET request for a nonexistent student ID
    response = client.get('/students/999/courses')
    
    assert response.status_code == 404  # Check for not found status
    assert b'Student not found' in response.data  # Check error message
```