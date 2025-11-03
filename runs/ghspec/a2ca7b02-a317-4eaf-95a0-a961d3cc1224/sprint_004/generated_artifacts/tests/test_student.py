```python
import pytest
from services.student_service import StudentService
from db.database import Database
from models.student import Student
from models.course import Course
from fastapi import HTTPException

@pytest.fixture
def setup_database():
    # Setup an in-memory SQLite database for testing
    db = Database('sqlite:///:memory:')
    db.create_schema()  # Assuming that this method sets up the necessary tables, including Student and Course
    yield db
    # Cleanup after tests
    db.close()

def test_enroll_student_in_course_valid_data(setup_database):
    # Arrange
    student_id = 1
    course_id = 1
    
    student = Student(id=student_id, name="John Doe")
    course = Course(id=course_id, name="Math 101", level="Beginner")
    
    setup_database.session.add(student)
    setup_database.session.add(course)
    setup_database.session.commit()

    # Act
    enrolled_student = StudentService.enroll_student_in_course(student_id, course_id)

    # Assert
    assert enrolled_student is not None
    assert course_id in [course.id for course in enrolled_student.courses]

def test_enroll_student_in_nonexistent_course(setup_database):
    # Arrange
    student_id = 1
    non_existent_course_id = 999

    student = Student(id=student_id, name="John Doe")
    setup_database.session.add(student)
    setup_database.session.commit()

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        StudentService.enroll_student_in_course(student_id, non_existent_course_id)
    
    # Verify the error response for non-existent course
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Invalid course ID: Course does not exist."

def test_enroll_nonexistent_student(setup_database):
    # Arrange
    non_existent_student_id = 999
    course_id = 1

    course = Course(id=course_id, name="Math 101", level="Beginner")
    setup_database.session.add(course)
    setup_database.session.commit()

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        StudentService.enroll_student_in_course(non_existent_student_id, course_id)
    
    # Verify the error response for non-existent student
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Invalid student ID: Student does not exist."
```