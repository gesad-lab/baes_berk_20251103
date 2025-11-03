```python
import pytest
from src.models.course import Course
from src.repositories.course_repository import CourseRepository
from src.services.course_service import CourseService


@pytest.fixture
def course_repository():
    """Fixture for initializing the CourseRepository for tests."""
    return CourseRepository()

@pytest.fixture
def course_service(course_repository):
    """Fixture for initializing the CourseService for tests."""
    return CourseService(course_repository)


def test_create_course(course_service):
    """Test creating a new course."""
    course_data = {
        'name': 'Mathematics 101',
        'level': 'Beginner',
    }
    course = course_service.create_course(course_data)
    assert course['name'] == course_data['name']
    assert course['level'] == course_data['level']
    assert 'id' in course  # Check if the course has an ID


def test_create_course_without_name(course_service):
    """Test creating a course without a name."""
    course_data = {
        'name': '',
        'level': 'Beginner',
    }
    with pytest.raises(ValueError) as excinfo:
        course_service.create_course(course_data)
    assert str(excinfo.value) == "Course name and level can't be blank"


def test_create_course_without_level(course_service):
    """Test creating a course without a level."""
    course_data = {
        'name': 'Science 101',
        'level': '',
    }
    with pytest.raises(ValueError) as excinfo:
        course_service.create_course(course_data)
    assert str(excinfo.value) == "Course name and level can't be blank"


def test_retrieve_course(course_service):
    """Test retrieving an existing course."""
    course_data = {
        'name': 'History 101',
        'level': 'Intermediate',
    }
    course = course_service.create_course(course_data)  # Create a course first
    retrieved_course = course_service.get_course(course['id'])
    assert retrieved_course['name'] == course_data['name']
    assert retrieved_course['level'] == course_data['level']


def test_retrieve_non_existent_course(course_service):
    """Test retrieving a non-existent course."""
    with pytest.raises(ValueError) as excinfo:
        course_service.get_course(999)  # Assuming 999 does not exist
    assert str(excinfo.value) == "Course not found"
```