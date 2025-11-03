```python
import pytest
from flask import json
from app import create_app, db
from app.models import Student, Course, StudentCourse

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Create the database tables
            # Add a sample student and course for testing
            sample_student = Student(name='Test Student')
            sample_course = Course(name='Sample Course', level='Beginner')
            db.session.add(sample_student)
            db.session.add(sample_course)
            db.session.commit()
            yield testing_client  # Provide the test client
            db.drop_all()  # Clean up after tests

def test_enroll_student_in_course(test_client):
    """Test enrolling a student in a course."""
    response = test_client.post('/students/1/courses', json={'course_id': 1})
    assert response.status_code == 201  # Check for 201 Created
    data = json.loads(response.data)
    assert data['student_id'] == 1
    assert data['course_id'] == 1

def test_list_students_courses(test_client):
    """Test listing a student's courses."""
    # First, enroll the student in the course
    test_client.post('/students/1/courses', json={'course_id': 1})
    
    response = test_client.get('/students/1/courses')
    assert response.status_code == 200  # Check for 200 OK
    data = json.loads(response.data)
    assert len(data) == 1  # Ensure one course is returned
    assert data[0]['course_id'] == 1  # Check course id

def test_unenroll_student_from_course(test_client):
    """Test unenrolling a student from a course."""
    # First, enroll the student in the course
    test_client.post('/students/1/courses', json={'course_id': 1})
    
    response = test_client.delete('/students/1/courses/1')
    assert response.status_code == 204  # Check for 204 No Content

    # Verify that the student's courses list is empty now
    response = test_client.get('/students/1/courses')
    assert response.status_code == 200  # Check for 200 OK
    data = json.loads(response.data)
    assert len(data) == 0  # Ensure no courses are returned
```