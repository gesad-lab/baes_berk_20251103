```python
import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException
from src.service.course_service import create_course, get_course_by_id  # Import the functions to be tested
from src.model.course import Course  # Import the Course model


@pytest.fixture
def mock_db_session():
    """Create a mock database session for testing."""
    session = MagicMock()
    yield session


def test_create_course_success(mock_db_session):
    """Test successfully creating a course with valid data."""
    course_name = "Mathematics"
    course_level = "Undergraduate"
    
    # Call the function under test
    created_course = create_course(mock_db_session, course_name, course_level)
    
    # Assertions to ensure course is created correctly
    assert created_course.name == course_name
    assert created_course.level == course_level


def test_get_course_by_id_success(mock_db_session):
    """Test retrieving a course by ID."""
    course_id = 1
    expected_course = Course(id=course_id, name="Mathematics", level="Undergraduate")
    
    # Mock the behavior of the database session to return the expected course
    mock_db_session.query.return_value.filter.return_value.first.return_value = expected_course
    
    # Call the function under test
    retrieved_course = get_course_by_id(mock_db_session, course_id)

    # Assertions to ensure the returned course matches expectations
    assert retrieved_course.id == expected_course.id
    assert retrieved_course.name == expected_course.name
    assert retrieved_course.level == expected_course.level


def test_create_course_missing_name(mock_db_session):
    """Test error handling when course name is missing."""
    course_name = ""
    course_level = "Undergraduate"
    
    with pytest.raises(HTTPException) as excinfo:
        create_course(mock_db_session, course_name, course_level)
    
    # Assertions to check the error message and status code
    assert excinfo.value.detail == "Course name is required."
    assert excinfo.value.status_code == 400


def test_create_course_missing_level(mock_db_session):
    """Test error handling when course level is missing."""
    course_name = "Mathematics"
    course_level = ""
    
    with pytest.raises(HTTPException) as excinfo:
        create_course(mock_db_session, course_name, course_level)
    
    # Assertions to check the error message and status code
    assert excinfo.value.detail == "Course level is required."
    assert excinfo.value.status_code == 400
```