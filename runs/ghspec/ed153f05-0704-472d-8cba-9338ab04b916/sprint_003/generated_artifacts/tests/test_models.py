```python
import pytest
from src.database import get_db, init_db
from src.models import Student, Course
from src.schemas import CourseSchema
from sqlalchemy.exc import IntegrityError
from flask import json

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

def test_create_course_valid(db):
    """Test creating a new course with valid data."""
    course_data = {"name": "Mathematics", "level": "Intermediate"}
    response = db.post('/courses', json=course_data)
    assert response.status_code == 201  # Check for successful creation
    assert 'id' in response.json  # Ensure the response contains the course ID
    assert response.json['name'] == course_data['name']  # Validate course name
    assert response.json['level'] == course_data['level']  # Validate course level

def test_create_course_missing_name(db):
    """Test creating a course without a name."""
    course_data = {"level": "Beginner"}
    response = db.post('/courses', json=course_data)
    assert response.status_code == 400  # Check for bad request
    assert response.json == {"error": {"code": "E001", "message": "Missing required field: name"}}

def test_create_course_missing_level(db):
    """Test creating a course without a level."""
    course_data = {"name": "Science"}
    response = db.post('/courses', json=course_data)
    assert response.status_code == 400  # Check for bad request
    assert response.json == {"error": {"code": "E001", "message": "Missing required field: level"}}

def test_create_course_missing_fields(db):
    """Test creating a course with missing name and level."""
    course_data = {}
    response = db.post('/courses', json=course_data)
    assert response.status_code == 400  # Check for bad request
    assert response.json == {
        "error": {
            "code": "E001",
            "message": "Missing required fields: name, level"
        }
    }
```