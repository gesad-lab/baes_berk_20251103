```python
import pytest
from models import db, Course
from services.course_service import create_course, get_course_by_id, list_courses

@pytest.fixture
def setup_database():
    """Setup a test database before each test."""
    db.create_all()  # Create the database tables
    yield
    db.session.remove()  # Cleanup the session
    db.drop_all()  # Drop all tables after tests

@pytest.fixture
def course_data():
    """Fixture providing sample course data."""
    return {
        "name": "Introduction to Programming",
        "level": "Beginner"
    }

def test_create_course(setup_database, course_data):
    """Test that a course is created successfully."""
    course = create_course(course_data['name'], course_data['level'])
    assert course.id is not None  # Check that the course has been assigned an ID
    assert course.name == course_data['name']
    assert course.level == course_data['level']

def test_get_course_by_id(setup_database, course_data):
    """Test fetching a course by ID."""
    course = create_course(course_data['name'], course_data['level'])
    fetched_course = get_course_by_id(course.id)
    assert fetched_course is not None
    assert fetched_course.id == course.id
    assert fetched_course.name == course_data['name']
    assert fetched_course.level == course_data['level']

def test_list_courses(setup_database, course_data):
    """Test retrieving a list of all courses."""
    create_course(course_data['name'], course_data['level'])
    create_course("Advanced Programming", "Intermediate")  # Add another course

    courses = list_courses()
    assert len(courses) == 2  # Verify that two courses are returned
    assert all(course.name in ["Introduction to Programming", "Advanced Programming"] for course in courses)
    assert all(course.level in ["Beginner", "Intermediate"] for course in courses)
```