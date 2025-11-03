```python
import json
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.student import Student  # Assuming Student model is defined in models.student
from models.course import Course    # Assuming Course model is defined in models.course
from models.student_course import StudentCourse  # Importing the join table model

# Initialize the Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up the in-memory database with test data
@pytest.fixture
def setup_database():
    db.create_all()

    # Create sample courses
    course1 = Course(name="Mathematics")
    course2 = Course(name="Science")
    db.session.add(course1)
    db.session.add(course2)

    # Create a sample student
    student = Student(name="John Doe")
    db.session.add(student)
    db.session.commit()

    yield student, [course1, course2]  # Provide the student and courses for testing

    # Clean up after tests
    db.drop_all()

def test_associate_courses_with_students(setup_database):
    student, courses = setup_database

    # Associate courses with the student
    for course in courses:
        student_course = StudentCourse(student_id=student.id, course_id=course.id)
        db.session.add(student_course)
    db.session.commit()

    # Verify associations
    assert len(student.courses) == 2
    assert student.courses[0].name == "Mathematics"
    assert student.courses[1].name == "Science"

def test_retrieve_student_course_information(setup_database):
    student, courses = setup_database

    # Associate courses
    for course in courses:
        student_course = StudentCourse(student_id=student.id, course_id=course.id)
        db.session.add(student_course)
    db.session.commit()

    # Retrieve student's courses
    associated_courses = StudentCourse.query.filter_by(student_id=student.id).all()
    course_ids = [sc.course_id for sc in associated_courses]

    # Ensure the student has the correct associated courses
    assert set(course_ids) == {course.id for course in courses}

def test_associate_invalid_course_fails(setup_database):
    student, _ = setup_database

    # Attempt to associate an invalid course
    invalid_course_id = 999  # Assuming this course does not exist
    response = {
        'error': {
            'code': 'E001', 
            'message': 'Invalid course ID.'
        }
    }

    with pytest.raises(Exception) as excinfo:
        student_course = StudentCourse(student_id=student.id, course_id=invalid_course_id)
        db.session.add(student_course)
        db.session.commit()

    assert str(excinfo.value) == "Invalid course ID."
```