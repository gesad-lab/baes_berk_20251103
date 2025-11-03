```python
import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.models import Course  # Assuming Course model exists
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

@pytest.fixture
def db_session():
    """Create a new database session for a test."""
    with app.app_context():
        db.create_all()  # Setup database before tests
        yield db.session
        db.drop_all()  # Clean up after tests

def test_retrieve_course_information(db_session):
    """Test retrieving course information by course ID."""
    # Arrange: Create a new course
    course = Course(name="Math 101", level="Beginner")
    db_session.add(course)
    db_session.commit()

    # Act: Retrieve the course information
    response = app.test_client().get(f'/courses/{course.id}')

    # Assert: The response contains the correct course details
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['name'] == "Math 101"
    assert json_data['level'] == "Beginner"

def test_retrieve_nonexistent_course(db_session):
    """Test retrieving a course that does not exist."""
    # Act: Retrieve course information for a non-existent ID
    response = app.test_client().get('/courses/9999')  # Assuming this ID does not exist

    # Assert: The response is a 404 Not Found
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['error']['code'] == "E404"
    assert json_data['error']['message'] == "Course not found"

def test_create_course_with_missing_fields(db_session):
    """Test creating a course without providing required fields."""
    response = app.test_client().post('/courses', json={"name": ""})

    # Assert: The response indicates missing fields error
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error']['code'] == "E001"
    assert json_data['error']['message'] == "Both name and level are required."

def test_create_course_with_invalid_level(db_session):
    """Test creating a course with an invalid level."""
    response = app.test_client().post('/courses', json={"name": "Science", "level": "InvalidLevel"})

    # Assert: The response indicates invalid level error
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error']['code'] == "E002"
    assert json_data['error']['message'] == "The provided level is invalid."
```