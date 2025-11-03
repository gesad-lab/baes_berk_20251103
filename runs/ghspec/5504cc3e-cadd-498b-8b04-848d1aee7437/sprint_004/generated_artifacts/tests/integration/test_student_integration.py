```python
import pytest
from flask import json
from app import create_app, db
from src.models.student import Student  # Import the Student model
from src.models.course import Course  # Import the Course model

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup the database before tests
            # Create initial student and course data for testing
            course = Course(name="Mathematics")
            student = Student(name="John Doe")
            db.session.add(course)
            db.session.add(student)
            db.session.commit()
        yield client
        db.drop_all()  # Clean up after tests

def test_enroll_student_in_course(client):
    """Test enrolling a student in a course."""
    # Assuming the endpoint for enrollment is POST /api/v1/enroll
    response = client.post('/api/v1/enroll', json={
        'student_id': 1,
        'course_id': 1
    })

    assert response.status_code == 201  # Check for successful enrollment
    assert response.json['message'] == 'Student enrolled successfully'

def test_get_courses_for_student(client):
    """Test retrieving courses for a specific student."""
    # Enroll the student first using the previous test or setup
    client.post('/api/v1/enroll', json={
        'student_id': 1,
        'course_id': 1
    })

    # Assuming the endpoint to get courses is GET /api/v1/students/<student_id>/courses
    response = client.get('/api/v1/students/1/courses')

    assert response.status_code == 200  # Check for successful retrieval
    assert isinstance(response.json['courses'], list)  # Ensure the response is a list
    assert len(response.json['courses']) > 0  # Check that the student has enrolled courses

def test_enrollment_with_invalid_student_id(client):
    """Test enrolling a student with an invalid student ID."""
    response = client.post('/api/v1/enroll', json={
        'student_id': 999,  # Non-existent student
        'course_id': 1
    })

    assert response.status_code == 404  # Check for not found error
    assert response.json['error']['code'] == 'E404'  # Check for correct error code
    assert response.json['error']['message'] == 'Student not found'

def test_enrollment_with_invalid_course_id(client):
    """Test enrolling a student with an invalid course ID."""
    response = client.post('/api/v1/enroll', json={
        'student_id': 1,
        'course_id': 999  # Non-existent course
    })

    assert response.status_code == 404  # Check for not found error
    assert response.json['error']['code'] == 'E404'  # Check for correct error code
    assert response.json['error']['message'] == 'Course not found'
```