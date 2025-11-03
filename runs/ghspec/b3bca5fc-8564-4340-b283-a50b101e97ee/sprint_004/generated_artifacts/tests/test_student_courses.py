```python
import pytest
from unittest.mock import patch
from src.models import Student, Course, StudentCourse  # Assuming models are in src/models
from src.database import SessionLocal  # Import your database session
from src.services import enroll_student_in_course, get_student_courses  # Assuming service functions are defined here

@pytest.fixture
def new_student():
    """Fixture to create a new student."""
    student = Student(name="Test Student")
    yield student
    # Here would be logic to clean up the student from the database if needed

@pytest.fixture
def new_course():
    """Fixture to create a new course."""
    course = Course(name="Test Course")
    yield course
    # Here would be logic to clean up the course from the database if needed

@pytest.fixture
def db_session():
    """Fixture for database session."""
    db = SessionLocal()
    yield db
    db.rollback()
    db.close()

def test_enroll_student_in_course(db_session, new_student, new_course):
    """Test enrolling a student in a course successfully."""
    # Arrange
    db_session.add(new_student)
    db_session.add(new_course)
    db_session.commit()

    # Act
    result = enroll_student_in_course(new_student.id, new_course.id)

    # Assert
    assert result is True
    enrolled = db_session.query(StudentCourse).filter_by(student_id=new_student.id, course_id=new_course.id).first()
    assert enrolled is not None

def test_get_student_courses(db_session, new_student, new_course):
    """Test retrieving a list of courses a student is enrolled in."""
    # Arrange
    db_session.add(new_student)
    db_session.add(new_course)
    db_session.commit()

    # Enroll student in course
    enroll_student_in_course(new_student.id, new_course.id)

    # Act
    courses = get_student_courses(new_student.id)

    # Assert
    assert len(courses) == 1
    assert courses[0].id == new_course.id

def test_enroll_student_in_nonexistent_course(db_session, new_student):
    """Test error handling for enrolling in a non-existent course."""
    # Arrange
    db_session.add(new_student)
    db_session.commit()

    # Act & Assert
    with pytest.raises(ValueError, match="Course does not exist"):
        enroll_student_in_course(new_student.id, 999)  # Assuming 999 is a non-existent course ID
```