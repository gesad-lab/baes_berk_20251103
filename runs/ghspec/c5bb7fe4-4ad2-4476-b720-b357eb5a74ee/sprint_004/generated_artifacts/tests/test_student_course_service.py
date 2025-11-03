```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models import Student, Course  # Import Student and Course models
from src.services.student_course_service import enroll_student, unenroll_student  # Import service methods
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and db for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create all database tables for testing
with app.app_context():
    db.create_all()

@pytest.fixture
def test_student():
    """Fixture to create a test student."""
    student = Student(name="Test Student")
    db.session.add(student)
    db.session.commit()
    return student

@pytest.fixture
def test_course():
    """Fixture to create a test course."""
    course = Course(title="Test Course")
    db.session.add(course)
    db.session.commit()
    return course

def test_enroll_student(test_student, test_course):
    """Test enrolling a student in a course."""
    result, error = enroll_student(test_student.id, test_course.id)

    # Assert that the enrollment was successful
    assert error is None
    assert result is True  # Assuming enroll_student returns True on success

def test_unenroll_student(test_student, test_course):
    """Test unenrolling a student from a course."""
    # First, enroll the student
    enroll_student(test_student.id, test_course.id)

    # Now, unenroll the student
    result, error = unenroll_student(test_student.id, test_course.id)

    # Assert that the unenrollment was successful
    assert error is None
    assert result is True  # Assuming unenroll_student returns True on success

def test_enroll_student_invalid_course(test_student):
    """Test error handling when enrolling a student in a non-existent course."""
    invalid_course_id = 999  # Assuming this ID does not exist
    result, error = enroll_student(test_student.id, invalid_course_id)

    # Assert that an error is returned
    assert result is False
    assert error is not None  # Expecting an error for invalid course enrollment

def test_unenroll_student_not_enrolled(test_student, test_course):
    """Test unenrolling a student who is not enrolled in a course."""
    result, error = unenroll_student(test_student.id, test_course.id)

    # Assert that the unenrollment was considered unsuccessful
    assert result is False
    assert error is not None  # Expecting an error since student was not enrolled
```