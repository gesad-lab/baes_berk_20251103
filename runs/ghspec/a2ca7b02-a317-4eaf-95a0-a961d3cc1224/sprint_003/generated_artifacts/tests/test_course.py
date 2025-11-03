```python
import pytest
from services.course_service import CourseService
from db.database import Database
from models.course import Course

@pytest.fixture
def setup_database():
    # Setup an in-memory SQLite database for testing
    db = Database('sqlite:///:memory:')
    db.create_schema()  # Assuming that this method sets up the necessary tables, including Course
    yield db
    # Cleanup after tests
    db.close()

def test_create_course_valid_data(setup_database):
    # Arrange
    course_service = CourseService(setup_database)
    valid_course_data = {"name": "Mathematics", "level": "Intermediate"}

    # Act
    created_course = course_service.create_course(valid_course_data)

    # Assert
    assert created_course.name == valid_course_data["name"]
    assert created_course.level == valid_course_data["level"]

def test_create_course_missing_name(setup_database):
    # Arrange
    course_service = CourseService(setup_database)
    invalid_course_data = {"level": "Intermediate"}

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        course_service.create_course(invalid_course_data)
    
    assert "name is required" in str(excinfo.value)

def test_create_course_missing_level(setup_database):
    # Arrange
    course_service = CourseService(setup_database)
    invalid_course_data = {"name": "Mathematics"}

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        course_service.create_course(invalid_course_data)
    
    assert "level is required" in str(excinfo.value)

def test_create_course_invalid_level_format(setup_database):
    # Arrange
    course_service = CourseService(setup_database)
    invalid_course_data = {"name": "Science", "level": "Expert"}

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        course_service.create_course(invalid_course_data)
    
    assert "Invalid level format" in str(excinfo.value)

def test_retrieve_courses_empty(setup_database):
    # Arrange
    course_service = CourseService(setup_database)

    # Act
    courses = course_service.retrieve_courses()

    # Assert
    assert courses == []

def test_retrieve_courses_with_data(setup_database):
    # Arrange
    course_service = CourseService(setup_database)
    course_service.create_course({"name": "Mathematics", "level": "Intermediate"})
    course_service.create_course({"name": "Physics", "level": "Beginner"})

    # Act
    courses = course_service.retrieve_courses()

    # Assert
    assert len(courses) == 2
    assert courses[0].name in ["Mathematics", "Physics"]
    assert courses[1].name in ["Mathematics", "Physics"]
    assert set(course.level for course in courses) == {"Intermediate", "Beginner"}
```