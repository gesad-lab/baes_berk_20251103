```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models.teacher import Teacher  # Import the Teacher model
from src.models.course import Course  # Import the Course model
from src.api.course_api import app  # Import the Flask app with the course API
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and db for testing
@pytest.fixture(scope='module')
def test_client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()  # Create database tables
        yield app.test_client()  # Provide the test client
        db.session.remove()
        db.drop_all()  # Clean up database after tests


def test_assign_teacher_to_course(test_client):
    """Test the end-to-end functionality of assigning a teacher to a course."""
    # Arrange: create a teacher and a course
    with test_client.application.app_context():
        teacher = Teacher(name='John Doe')
        course = Course(title='Mathematics 101')
        test_client.application.db.session.add(teacher)
        test_client.application.db.session.add(course)
        test_client.application.db.session.commit()

    # Act: Assign the teacher to the course
    response = test_client.post('/api/courses/assign_teacher', json={
        'course_id': course.id,
        'teacher_id': teacher.id
    })

    # Assert: verify the response
    assert response.status_code == 200 
    assert response.json['message'] == 'Teacher assigned to course successfully.'

    # Verify the actual assignment
    with test_client.application.app_context():
        assigned_course = Course.query.get(course.id)
        assert assigned_course.teacher_id == teacher.id  # Ensure the assignment was made


def test_assign_teacher_to_course_invalid_teacher(test_client):
    """Test assigning a teacher to a course with an invalid teacher ID."""
    # Arrange: define a valid course ID but invalid teacher ID
    course_id = 1  # Assuming the course exists

    # Act: Attempt to assign a non-existent teacher
    response = test_client.post('/api/courses/assign_teacher', json={
        'course_id': course_id,
        'teacher_id': 9999  # Invalid teacher ID
    })

    # Assert: verify error response
    assert response.status_code == 400
    assert response.json['error']['code'] == 'E001'
    assert response.json['error']['message'] == 'Invalid teacher ID.'
```