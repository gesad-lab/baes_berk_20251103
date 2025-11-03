```python
import pytest
from flask import json
from src.routes import app, db
from src.models import Course, Student, StudentCourse

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables for the test
            # Seed the database with initial data if necessary
            course = Course(name='Biology 101', level='Undergraduate')
            student = Student(name='John Doe')
            db.session.add(course)
            db.session.add(student)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after the test

def test_enroll_student_in_course_success(client):
    """Test successfully enrolling a student in a course."""
    response = client.post('/enroll', data=json.dumps({
        'student_id': 1,
        'course_id': 1
    }), content_type='application/json')

    assert response.status_code == 201  # Expecting a success status
    assert response.json == {"message": "Successfully enrolled in course"}
    
    # Verify the enrollment is recorded in the StudentCourse model
    enrollment = StudentCourse.query.filter_by(student_id=1, course_id=1).first()
    assert enrollment is not None

def test_retrieve_student_courses_success(client):
    """Test successfully retrieving courses for a student."""
    client.post('/enroll', data=json.dumps({
        'student_id': 1,
        'course_id': 1
    }), content_type='application/json')  # Enroll student in a course

    response = client.get('/student_courses/1')  # Get courses for student with ID 1
    assert response.status_code == 200
    assert len(response.json['courses']) == 1
    assert response.json['courses'][0]['course_id'] == 1
    assert response.json['courses'][0]['course_name'] == 'Biology 101'

def test_enroll_student_in_course_invalid_student(client):
    """Test enrolling student with a non-existent ID fails."""
    response = client.post('/enroll', data=json.dumps({
        'student_id': 9999,  # Invalid student ID
        'course_id': 1
    }), content_type='application/json')

    assert response.status_code == 400  # Expecting client error
    assert response.json == {"error": {"code": "E001", "message": "Invalid student ID"}}

def test_enroll_student_in_course_invalid_course(client):
    """Test enrolling a student with a non-existent course fails."""
    response = client.post('/enroll', data=json.dumps({
        'student_id': 1,
        'course_id': 9999  # Invalid course ID
    }), content_type='application/json')

    assert response.status_code == 400  # Expecting client error
    assert response.json == {"error": {"code": "E002", "message": "Invalid course ID"}}
```