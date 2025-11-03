```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.models.course import Course  # Importing the Course model
from src.models.teacher import Teacher  # Importing the Teacher model
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

@pytest.fixture
def db_session():
    """Create a new database session for a test."""
    with app.app_context():
        db.create_all()  # Create the database and tables
        yield db.session  # Provide the session to the test
        db.drop_all()  # Clean up after the test

# Test case for assigning a teacher to a course
def test_assign_teacher_to_course(db_session):
    # Setup: Create a teacher and a course
    teacher = Teacher(name="John Doe", email="john@example.com")
    course = Course(name="Math 101")
    db_session.add(teacher)
    db_session.add(course)
    db_session.commit()

    # Assign the teacher to the course
    response = app.test_client().post(
        f'/courses/{course.id}/assign_teacher',
        json={'teacher_id': teacher.id}
    )

    assert response.status_code == 200  # Expect success
    data = response.get_json()
    assert data['teacher_id'] == teacher.id  # Verify teacher assignment

# Test case for retrieving course information with teacher details
def test_get_course_info_with_teacher(db_session):
    # Setup: Create a teacher and a course
    teacher = Teacher(name="John Doe", email="john@example.com")
    course = Course(name="Math 101", teacher_id=teacher.id)
    db_session.add(teacher)
    db_session.add(course)
    db_session.commit()

    response = app.test_client().get(f'/courses/{course.id}')

    assert response.status_code == 200  # Expect success
    data = response.get_json()
    assert data['teacher_id'] == teacher.id  # Verify teacher info is included 

# Test case for handling invalid teacher assignment
def test_assign_invalid_teacher_to_course(db_session):
    # Setup: Create a course
    course = Course(name="Math 101")
    db_session.add(course)
    db_session.commit()

    # Attempt to assign an invalid teacher ID (does not exist)
    response = app.test_client().post(
        f'/courses/{course.id}/assign_teacher',
        json={'teacher_id': 999}  # Non-existing teacher ID
    )

    assert response.status_code == 400  # Expect bad request
    data = response.get_json()
    assert data['error']['message'] == "Invalid teacher assignment"  # Verify error message

# Test case for updating teacher assignment for a course
def test_update_teacher_assignment(db_session):
    # Setup: Create a teacher and course
    teacher1 = Teacher(name="John Doe", email="john@example.com")
    teacher2 = Teacher(name="Jane Smith", email="jane@example.com")
    course = Course(name="Math 101", teacher_id=teacher1.id)
    db_session.add(teacher1)
    db_session.add(teacher2)
    db_session.add(course)
    db_session.commit()

    # Update teacher assignment
    response = app.test_client().post(
        f'/courses/{course.id}/assign_teacher',
        json={'teacher_id': teacher2.id}
    )

    assert response.status_code == 200  # Expect success
    data = response.get_json()
    assert data['teacher_id'] == teacher2.id  # Verify the course has the new teacher
```