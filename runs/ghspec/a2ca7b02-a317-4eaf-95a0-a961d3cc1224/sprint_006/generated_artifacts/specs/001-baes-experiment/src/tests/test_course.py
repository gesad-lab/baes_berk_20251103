# File: tests/test_course.py

import pytest
from fastapi import HTTPException
from services.course_service import CourseService
from db.database import Session, engine
from models.course import Course
from models.teacher import Teacher

@pytest.fixture(scope="module")
def setup_database():
    """Setup an in-memory SQLite database for testing."""
    # Create database tables
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    # Create a sample teacher and course data
    teacher = Teacher(id=1, name="John Doe", email="john.doe@example.com")
    course = Course(id=1, title="Math 101", description="Basic Math Course", teacher_id=None)

    session.add(teacher)
    session.add(course)
    session.commit()

    yield session  # This will be the database session for tests

    # Teardown: drop the tables
    session.query(Course).delete()
    session.query(Teacher).delete()
    session.commit()
    session.close()

def test_assign_teacher_valid_data(setup_database):
    """Test case for assigning a valid teacher to a course."""
    # Arrange
    course_id = 1
    teacher_data = {"teacher_id": 1}

    # Act
    response = CourseService.assign_teacher(course_id, teacher_data)

    # Assert
    assert response['message'] == "Teacher assigned successfully"
    # Check if teacher is correctly assigned in the database
    course = setup_database.query(Course).filter_by(id=course_id).first()
    assert course.teacher_id == teacher_data["teacher_id"]

def test_assign_teacher_invalid_teacher(setup_database):
    """Test case for assigning a non-existent teacher to a course."""
    # Arrange
    course_id = 1
    invalid_teacher_data = {"teacher_id": 999}  # Non-existent teacher

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        CourseService.assign_teacher(course_id, invalid_teacher_data)
    
    assert exc_info.value.status_code == 404  # Expect a 404 Not Found

def test_retrieve_course_with_teacher(setup_database):
    """Test case for retrieving a course and checking assigned teacher data."""
    # Arrange
    course_id = 1
    teacher_data = {"teacher_id": 1}
    CourseService.assign_teacher(course_id, teacher_data)  # Assign teacher first

    # Act
    response = CourseService.get_course_with_teacher(course_id)

    # Assert
    assert response['id'] == course_id
    assert response['title'] == "Math 101"
    assert response['teacher']['name'] == "John Doe"
    assert response['teacher']['email'] == "john.doe@example.com"

def test_retrieve_course_non_existent(setup_database):
    """Test case for retrieving a non-existent course."""
    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        CourseService.get_course_with_teacher(999)  # Non-existent course
    
    assert exc_info.value.status_code == 404  # Expect a 404 Not Found