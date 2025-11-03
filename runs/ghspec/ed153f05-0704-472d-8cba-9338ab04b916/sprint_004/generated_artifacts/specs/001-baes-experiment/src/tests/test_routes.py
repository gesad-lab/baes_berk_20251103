```python
import pytest
from flask import json
from src.database import get_db, init_db
from src.models import Student, Course, StudentCourse
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

@pytest.fixture(scope='module')
def test_client(db):
    """Create a test client for making API requests."""
    from src.app import create_app  # Import the application factory
    app = create_app()  # Create a new instance of the application
    with app.test_client() as client:
        yield client  # Provide the client to the test

def test_enroll_student_in_course(test_client, db):
    """Test enrolling a student in a course."""
    # Create a test student and course
    student = Student(name="John Doe")
    course = Course(name="Mathematics", level="Beginner")
    db.session.add(student)
    db.session.add(course)
    db.session.commit()

    # Enroll the student in the course
    response = test_client.post(f'/students/{student.id}/courses', 
                                 json={"course_id": course.id})
    
    assert response.status_code == 201
    assert response.get_json() == {"message": "Enrollment successful."}

    # Verify that the enrollment was recorded in the database
    assert db.session.query(StudentCourse).filter_by(student_id=student.id, course_id=course.id).count() == 1

def test_get_student_courses(test_client, db):
    """Test retrieving the list of courses for a specific student."""
    # Create a test student and two courses
    student = Student(name="Jane Smith")
    course1 = Course(name="Science", level="Intermediate")
    course2 = Course(name="Literature", level="Advanced")
    db.session.add(student)
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    # Enroll the student in both courses
    db.session.add(StudentCourse(student_id=student.id, course_id=course1.id))
    db.session.add(StudentCourse(student_id=student.id, course_id=course2.id))
    db.session.commit()

    # Retrieve the list of courses for the student
    response = test_client.get(f'/students/{student.id}/courses')

    assert response.status_code == 200
    courses = response.get_json()
    assert len(courses) == 2
    assert set(course['name'] for course in courses) == {"Science", "Literature"}
```