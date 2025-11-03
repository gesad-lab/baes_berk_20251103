```python
import pytest
from src.services import enroll_student_in_course, get_student_courses
from src.models import Student, Course
from src.database import get_db_session

@pytest.fixture
def db_session():
    """Provides a transactional scope around a test, rolling back at the end."""
    session = get_db_session()
    yield session
    session.rollback()

@pytest.fixture
def sample_data(db_session):
    """Create sample data for testing."""
    # Create a sample student
    student = Student(name="John Doe", email="john.doe@example.com")
    db_session.add(student)
    
    # Create a sample course
    course = Course(name="Biology 101", level="Beginner")
    db_session.add(course)

    # Commit the transaction to persist the data
    db_session.commit()

    return student, course

def test_enroll_student_in_course_success(db_session, sample_data):
    """Test that enrolling a student in a course updates the student record."""
    student, course = sample_data

    enroll_response = enroll_student_in_course(student.id, course.id, db_session)

    # Confirm the enrollment was successful and check response
    assert enroll_response['status'] == 'success'
    assert course.id in [c.id for c in student.courses]

def test_get_student_courses_success(db_session, sample_data):
    """Test that retrieving a student's courses returns the correct list of courses."""
    student, course = sample_data
    enroll_student_in_course(student.id, course.id, db_session)

    courses = get_student_courses(student.id, db_session)

    # Check if the retrieved courses match the enrolled course
    assert len(courses) == 1
    assert courses[0].name == course.name

def test_get_student_courses_not_found(db_session):
    """Test that querying a student without course enrollments returns a not found response."""
    student = Student(name="Jane Doe", email="jane.doe@example.com")
    db_session.add(student)
    db_session.commit()

    courses = get_student_courses(student.id, db_session)

    # Check that no courses are found
    assert len(courses) == 0
```