```python
import pytest
from unittest.mock import patch
from src.services.course_service import create_course, get_course_by_id
from src.models import Course

@pytest.fixture
def mock_course():
    """Create a mock course data for testing."""
    return Course(id=1, name="Introduction to Programming", level="Beginner")

def test_create_course_creates_course_successfully():
    """Test creating a course successfully."""
    course_details = {
        "name": "Advanced Python Programming",
        "level": "Advanced"
    }
    
    with patch('src.models.Course.save') as mock_save:
        course = create_course(course_details)
        mock_save.assert_called_once()
        assert course.name == course_details["name"]
        assert course.level == course_details["level"]

def test_get_course_by_id_retrieves_course_successfully(mock_course):
    """Test retrieving a course by ID successfully."""
    with patch('src.models.Course.query.get') as mock_query_get:
        mock_query_get.return_value = mock_course
        course = get_course_by_id(mock_course.id)
        assert course.id == mock_course.id
        assert course.name == mock_course.name
        assert course.level == mock_course.level

def test_create_course_missing_name_field():
    """Test creating a course without the name field returns an error."""
    course_details = {
        "level": "Intermediate"
    }
    
    with pytest.raises(ValueError) as excinfo:
        create_course(course_details)
    
    assert str(excinfo.value) == "Course name is required"

def test_create_course_missing_level_field():
    """Test creating a course without the level field returns an error."""
    course_details = {
        "name": "Data Science"
    }
    
    with pytest.raises(ValueError) as excinfo:
        create_course(course_details)
    
    assert str(excinfo.value) == "Course level is required"
```