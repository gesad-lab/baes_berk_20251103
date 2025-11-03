```python
import pytest
from flask import json
from app import create_app, db
from models.student import Student  # Import the Student model
from models.course import Course  # Import the Course model
from models.student_courses import StudentCourses  # Import the new mapping model

@pytest.fixture
def client():
    app = create_app('testing')  # Use a separate testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create fresh database for each test
            # Set up initial data for Student and Course
            student = Student(name='Test Student')
            course = Course(name='Test Course')
            db.session.add(student)
            db.session.add(course)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()  # Clean up database after tests

def test_enroll_student_in_course(client):
    """Test enrolling a student in a course."""
    # Retrieve the test student and course
    student = Student.query.first()
    course = Course.query.first()

    # Make the enroll API request
    response = client.post(f'/api/v1/enrollments', 
                           data=json.dumps({'student_id': student.id, 'course_id': course.id}),
                           content_type='application/json')
    
    # Check response status and database state
    assert response.status_code == 201  # Expecting Created
    enrollment = StudentCourses.query.filter_by(student_id=student.id, course_id=course.id).first()
    assert enrollment is not None  # Enrollment should exist

def test_unenroll_student_from_course(client):
    """Test unenrolling a student from a course."""
    # Setting up the student-course relationship
    student = Student.query.first()
    course = Course.query.first()
    enrollment = StudentCourses(student_id=student.id, course_id=course.id)
    db.session.add(enrollment)
    db.session.commit()

    # Make the unenroll API request
    response = client.delete(f'/api/v1/enrollments',
                             data=json.dumps({'student_id': student.id, 'course_id': course.id}),
                             content_type='application/json')
    
    # Check response status and database state
    assert response.status_code == 204  # Expecting No Content
    enrollment_after = StudentCourses.query.filter_by(student_id=student.id, course_id=course.id).first()
    assert enrollment_after is None  # Enrollment should no longer exist

def test_get_courses_for_student(client):
    """Test retrieving courses for a student."""
    student = Student.query.first()
    course = Course.query.first()
    # Set up initial enrollment
    enrollment = StudentCourses(student_id=student.id, course_id=course.id)
    db.session.add(enrollment)
    db.session.commit()

    # Make the GET request for courses for this student
    response = client.get(f'/api/v1/students/{student.id}/courses')

    # Check response status and data
    assert response.status_code == 200  # Expecting OK
    data = json.loads(response.data)
    assert len(data) == 1  # Expecting 1 course for this student
    assert data[0]['id'] == course.id  # Ensure the correct course is returned
```