```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models.course import Course  # Import the Course model
from src.models.teacher import Teacher  # Import the Teacher model
from src.api.course_api import app  # Import the Flask app with the course API
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and db for testing
@pytest.fixture(scope='module')
def test_client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db = SQLAlchemy(app)
        db.create_all()  # Create tables

        yield app.test_client()  # Provide the test client

        db.drop_all()  # Clean up after tests

@pytest.fixture
def sample_teacher(test_client):
    """Fixture to create a sample teacher for testing."""
    with test_client.application.app_context():
        teacher = Teacher(name="John Doe", subject="Mathematics")
        db.session.add(teacher)
        db.session.commit()
        return teacher

@pytest.fixture
def sample_course(test_client):
    """Fixture to create a sample course for testing."""
    with test_client.application.app_context():
        course = Course(title="Calculus 101")
        db.session.add(course)
        db.session.commit()
        return course

def test_assign_teacher_to_course(test_client, sample_teacher, sample_course):
    """Test assigning a teacher to a course."""
    response = test_client.post(f'/courses/{sample_course.id}/assign_teacher', json={'teacher_id': sample_teacher.id})
    assert response.status_code == 200
    assert response.json['message'] == 'Teacher assigned successfully'

def test_assign_teacher_invalid_course(test_client, sample_teacher):
    """Test assigning a teacher to a non-existent course."""
    response = test_client.post('/courses/999/assign_teacher', json={'teacher_id': sample_teacher.id})
    assert response.status_code == 404
    assert response.json['error']['message'] == 'Course not found'

def test_assign_invalid_teacher_to_course(test_client, sample_course):
    """Test assigning a non-existent teacher to a course."""
    response = test_client.post(f'/courses/{sample_course.id}/assign_teacher', json={'teacher_id': 999})
    assert response.status_code == 404
    assert response.json['error']['message'] == 'Teacher not found'

def test_assign_teacher_without_id(test_client, sample_course):
    """Test assigning a teacher without providing an ID."""
    response = test_client.post(f'/courses/{sample_course.id}/assign_teacher', json={})
    assert response.status_code == 400
    assert response.json['error']['message'] == 'Invalid request: teacher_id is required'
```