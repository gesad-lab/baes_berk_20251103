```python
import pytest
from unittest.mock import MagicMock
from src.services.enrollment_service import enroll_student_in_course, get_courses_for_student
from src.models import Enrollment, Student, Course
from your_app import db  # Ensure to update with actual import paths

@pytest.fixture
def mock_student():
    """Create a mock student data for testing."""
    return Student(id=1)  # Assuming Student model has an ID

@pytest.fixture
def mock_course():
    """Create a mock course data for testing."""
    return Course(id=1)  # Assuming Course model has an ID

@pytest.fixture
def enrolled_student_course(mock_student, mock_course):
    """Create an Enrollment instance for testing."""
    enrollment = Enrollment(student_id=mock_student.id, course_id=mock_course.id)
    db.session.add(enrollment)
    db.session.commit()
    return enrollment

def test_enroll_student_in_course_success(mock_student, mock_course):
    """Test enrolling a student in a course successfully."""
    response = enroll_student_in_course(mock_student.id, mock_course.id)
    assert response['status'] == 'success'
    assert response['student_id'] == mock_student.id
    assert response['course_id'] == mock_course.id

def test_get_courses_for_student_success(enrolled_student_course, mock_student):
    """Test retrieving courses for a student successfully."""
    response = get_courses_for_student(mock_student.id)
    assert len(response) == 1
    assert response[0]['course_id'] == enrolled_student_course.course_id

def test_enroll_student_in_invalid_course():
    """Test error handling when enrolling a student in a non-existent course."""
    invalid_course_id = 999  # Assuming this course does not exist
    response = enroll_student_in_course(1, invalid_course_id)
    assert response['status'] == 'error'
    assert response['message'] == 'Invalid course ID provided'

def test_enroll_student_in_invalid_student():
    """Test error handling when enrolling with a non-existent student."""
    invalid_student_id = 999  # Assuming this student does not exist
    response = enroll_student_in_course(invalid_student_id, 1)
    assert response['status'] == 'error'
    assert response['message'] == 'Invalid student ID provided'
```