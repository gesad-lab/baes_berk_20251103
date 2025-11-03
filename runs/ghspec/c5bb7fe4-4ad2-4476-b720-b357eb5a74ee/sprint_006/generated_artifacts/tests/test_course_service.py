```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models.course import Course  # Assuming the Course model is defined here
from src.services.course_service import assign_teacher, update_teacher_assignment  # Import service methods
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and db for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@pytest.fixture(scope='module')
def test_client():
    with app.app_context():
        db.create_all()  # Create tables
        yield app.test_client()  # Provide the test client to the test case
        db.drop_all()  # Clean up after tests

@pytest.fixture(scope='module')
def setup_courses():
    with app.app_context():
        # Create a sample course for testing
        course = Course(id=1, name='Math 101', teacher_id=None)
        db.session.add(course)
        db.session.commit()
        yield course  # Provide the course object for tests
        db.session.delete(course)
        db.session.commit()

def test_assign_teacher(setup_courses):
    """Test assigning a teacher to a course."""
    teacher_id = 1  # Example teacher ID
    result = assign_teacher(course_id=setup_courses.id, teacher_id=teacher_id)

    assert result is True  # Expect the assignment to succeed
    updated_course = Course.query.get(setup_courses.id)
    assert updated_course.teacher_id == teacher_id  # Assert the teacher_id was updated

def test_update_teacher_assignment(setup_courses):
    """Test updating the teacher assignment for a course."""
    initial_teacher_id = 1
    new_teacher_id = 2

    # Initially assign a teacher
    assign_teacher(course_id=setup_courses.id, teacher_id=initial_teacher_id)

    # Now update the teacher assignment
    result = update_teacher_assignment(course_id=setup_courses.id, teacher_id=new_teacher_id)

    assert result is True  # Expect the update to succeed
    updated_course = Course.query.get(setup_courses.id)
    assert updated_course.teacher_id == new_teacher_id  # Assert the teacher_id was updated
```