```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.services.course_service import create_course, get_all_courses, update_course_level
from src.models import Course  # Assuming Course model is defined in src/models/course.py

# Initialize Flask app and db for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create all database tables for testing
with app.app_context():
    db.create_all()

@pytest.fixture
def course_data():
    """Fixture for course data."""
    return {"name": "Intro to Programming", "level": "Beginner"}

def test_create_course_with_valid_data(course_data):
    """Test creating a new course successfully with valid data."""
    course = create_course(course_data)
    assert course.id is not None
    assert course.name == course_data["name"]
    assert course.level == course_data["level"]

def test_create_course_with_missing_name():
    """Test creating a course with missing name raises an error."""
    invalid_course_data = {"level": "Beginner"}
    with pytest.raises(Exception) as excinfo:
        create_course(invalid_course_data)
    assert "name is required" in str(excinfo.value)

def test_create_course_with_missing_level():
    """Test creating a course with missing level raises an error."""
    invalid_course_data = {"name": "Intro to Programming"}
    with pytest.raises(Exception) as excinfo:
        create_course(invalid_course_data)
    assert "level is required" in str(excinfo.value)

def test_get_all_courses_empty():
    """Test getting all courses when none exist."""
    courses = get_all_courses()
    assert courses == []

def test_get_all_courses_with_data(course_data):
    """Test retrieving all courses after adding a course."""
    create_course(course_data)
    courses = get_all_courses()
    assert len(courses) == 1
    assert courses[0].name == course_data["name"]

def test_update_course_level():
    """Test updating the level of an existing course."""
    course = create_course({"name": "Advanced Python", "level": "Intermediate"})
    updated_course = update_course_level(course.id, "Advanced")
    assert updated_course.level == "Advanced"

def test_update_course_level_invalid_course():
    """Test updating the level of a non-existent course raises an error."""
    with pytest.raises(Exception) as excinfo:
        update_course_level(99999, "Advanced")  # Assuming 99999 does not exist
    assert "Course not found" in str(excinfo.value)
```