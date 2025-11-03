```python
import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException
from src.service.student_course_service import associate_courses, get_student_courses  # Import the functions to be tested
from src.model.student_course import StudentCourse  # Import the StudentCourse model

@pytest.fixture
def mock_db_session():
    """Create a mock database session for testing."""
    session = MagicMock()
    yield session

def test_associate_courses_success(mock_db_session):
    """Test successfully associating courses with a student."""
    # Mock the database session's behavior to succeed
    mock_db_session.add.side_effect = None  # Simulate successful add operation
    
    # Mock student_course_repository to perform association
    student_id = 1
    course_ids = [1, 2, 3]
    result = associate_courses(mock_db_session, student_id, course_ids)
    
    # Assertions to verify successful association
    assert result == "Courses associated successfully with the student."
    mock_db_session.add.assert_called()  # Ensure add was called
    assert mock_db_session.commit.called  # Check if commit was called afterward

def test_associate_courses_invalid_student(mock_db_session):
    """Test associating courses with an invalid student."""
    mock_db_session.add.side_effect = HTTPException(status_code=404, detail="Student not found")
    
    student_id = 999  # Non-existent student
    course_ids = [1, 2]
    
    with pytest.raises(HTTPException) as exc_info:
        associate_courses(mock_db_session, student_id, course_ids)
    
    # Assertions to verify the HTTPException raised with the correct message
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Student not found"

def test_get_student_courses_success(mock_db_session):
    """Test retrieving courses associated with a student."""
    # Mocking the return value for a student with courses
    student_id = 1
    mock_courses = [StudentCourse(course_id=1), StudentCourse(course_id=2)]
    mock_db_session.query.return_value.filter.return_value.all.return_value = mock_courses
    
    courses = get_student_courses(mock_db_session, student_id)
    
    # Assertions to ensure we get the correct course list
    assert len(courses) == 2
    assert courses[0].course_id == 1
    assert courses[1].course_id == 2

def test_get_student_courses_no_courses(mock_db_session):
    """Test retrieving courses for a student with no associated courses."""
    student_id = 1
    mock_db_session.query.return_value.filter.return_value.all.return_value = []

    courses = get_student_courses(mock_db_session, student_id)
    
    # Assertions to ensure no courses are returned
    assert len(courses) == 0
```