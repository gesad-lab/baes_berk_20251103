```python
import pytest
from flask import json
from app import create_app, db
from src.models.student import Student  # Importing Student model
from src.models.course import Course  # Importing Course model
from src.services.student_service import enroll_student, disassociate_student, get_courses_for_student  # Importing service functions

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup the database before tests
            # Pre-populate some test data if needed
            yield client
            db.drop_all()  # Clean up after tests

@pytest.fixture
def sample_student(client):
    """Create a sample student for testing."""
    student = Student(name='Test Student', email='test@student.com')
    db.session.add(student)
    db.session.commit()
    return student

@pytest.fixture
def sample_course(client):
    """Create a sample course for testing."""
    course = Course(title='Test Course', description='A course for testing.')
    db.session.add(course)
    db.session.commit()
    return course

def test_enroll_student(sample_student, sample_course):
    """Test enrolling a student in a course."""
    result = enroll_student(sample_student.id, sample_course.id)
    assert result is True  # Check that the enrollment succeeded

    # Optionally, query the database to verify the enrollment was recorded correctly

def test_enroll_student_invalid_course(sample_student):
    """Test enrolling a student with an invalid course ID."""
    invalid_course_id = 9999  # Assuming this ID does not exist
    with pytest.raises(ValueError) as excinfo:
        enroll_student(sample_student.id, invalid_course_id)
    assert str(excinfo.value) == "Invalid course ID"

def test_disassociate_student(sample_student, sample_course):
    """Test disassociating a student from a course."""
    enroll_student(sample_student.id, sample_course.id)  # Enroll first
    result = disassociate_student(sample_student.id, sample_course.id)
    assert result is True  # Check that disassociation succeeded

    # Verify that the association is removed if necessary

def test_get_courses_for_student(sample_student, sample_course):
    """Test getting courses for a student."""
    enroll_student(sample_student.id, sample_course.id)  # Enroll first
    courses = get_courses_for_student(sample_student.id)
    assert sample_course in courses  # Check that the right course is returned
```