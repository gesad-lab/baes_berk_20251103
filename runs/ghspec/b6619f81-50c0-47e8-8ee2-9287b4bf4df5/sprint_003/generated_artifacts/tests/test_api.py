```python
import pytest
from src.models import Course  # Import the Course model
from src.repositories import CourseRepository  # Assuming a repository exists for course data operations
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def course_repository():
    """Fixture for creating a course repository for testing."""
    return CourseRepository()

@pytest.fixture
def new_course():
    """Fixture for a new course with valid attributes."""
    return Course(name="Introduction to Programming", level="Beginner")

def test_create_course(course_repository, new_course):
    """Test creating a new course with valid attributes."""
    course_repository.create(new_course)  # Assuming the repository has a create method
    assert course_repository.get_by_id(new_course.id) is not None  # Ensure the course can be retrieved

def test_create_course_with_missing_name(course_repository):
    """Test creating a course with a missing name raises an error."""
    incomplete_course = Course(name=None, level="Beginner")
    with pytest.raises(IntegrityError):  # Expect an integrity error for missing name
        course_repository.create(incomplete_course)

def test_create_course_with_missing_level(course_repository):
    """Test creating a course with a missing level raises an error."""
    incomplete_course = Course(name="Advanced Programming", level=None)
    with pytest.raises(IntegrityError):  # Expect an integrity error for missing level
        course_repository.create(incomplete_course)

def test_get_course(course_repository, new_course):
    """Test retrieving course information."""
    created_course = course_repository.create(new_course)
    retrieved_course = course_repository.get_by_id(created_course.id)
    assert retrieved_course.name == created_course.name
    assert retrieved_course.level == created_course.level

def test_update_course(course_repository, new_course):
    """Test updating course information."""
    created_course = course_repository.create(new_course)
    created_course.name = "Advanced Programming"
    created_course.level = "Intermediate"
    course_repository.update(created_course)  # Assuming the repository has an update method
    
    updated_course = course_repository.get_by_id(created_course.id)
    assert updated_course.name == "Advanced Programming"
    assert updated_course.level == "Intermediate"
```