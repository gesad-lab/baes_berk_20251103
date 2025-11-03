```python
import pytest
from src.services import create_course, get_course_by_id
from src.models import Course
from src.database import get_db_session

@pytest.fixture
def db_session():
    """Provides a transactional scope around a test, rolling back at the end."""
    session = get_db_session()
    yield session
    session.rollback()


def test_create_course_success(db_session):
    """Test successful creation of a course with valid name and level."""
    course_name = "Biology 101"
    course_level = "Beginner"
    
    course = create_course(course_name, course_level, db_session)
    
    # Check if the course was created successfully
    assert course.name == course_name
    assert course.level == course_level
    assert course.id is not None


def test_create_course_missing_name(db_session):
    """Test creation of a course fails when name is missing."""
    course_level = "Intermediate"
    
    with pytest.raises(ValueError) as excinfo:
        create_course("", course_level, db_session)
    
    # Assert that a specific error message is raised
    assert "Course name is required" in str(excinfo.value)


def test_create_course_missing_level(db_session):
    """Test creation of a course fails when level is missing."""
    course_name = "Chemistry 101"
    
    with pytest.raises(ValueError) as excinfo:
        create_course(course_name, "", db_session)

    # Assert that a specific error message is raised
    assert "Course level is required" in str(excinfo.value)


def test_get_course_by_id_success(db_session):
    """Test retrieving a course by its ID."""
    course_name = "Physics 101"
    course_level = "Beginner"
    
    # Create a course to retrieve later
    course = create_course(course_name, course_level, db_session)
    
    retrieved_course = get_course_by_id(course.id, db_session)
    
    # Assert the retrieved course matches the created course
    assert retrieved_course.name == course_name
    assert retrieved_course.level == course_level


def test_get_course_by_id_not_found(db_session):
    """Test retrieving a course by ID that does not exist."""
    with pytest.raises(ValueError) as excinfo:
        get_course_by_id(999, db_session)  # Assuming 999 does not exist
    
    # Assert that a specific error message is raised
    assert "Course not found" in str(excinfo.value)
```