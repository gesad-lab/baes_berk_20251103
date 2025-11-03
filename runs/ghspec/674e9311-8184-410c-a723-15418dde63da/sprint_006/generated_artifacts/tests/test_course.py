```python
import pytest
from flask import Flask, jsonify, request
from src.api import create_app
from sqlalchemy.exc import IntegrityError
from src.models.course import Course
from src.models.teacher import Teacher
from src.services.course_service import assign_teacher_to_course, get_course_details
from unittest.mock import patch

@pytest.fixture
def app():
    """Setup the Flask app for testing."""
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()

@pytest.fixture
def setup_data(app):
    """Create a test database and add sample data for testing."""
    with app.app_context():
        # Create sample teachers and courses for tests
        teacher = Teacher(name="John Doe")
        course = Course(title="Math 101", description="Basic Mathematics")
        # Assume `db` is your SQLAlchemy database instance
        db.session.add(teacher)
        db.session.add(course)
        db.session.commit()
        return teacher, course

def test_assign_teacher_to_course(client, setup_data):
    """Test assigning a teacher to a course."""
    teacher, course = setup_data

    # Define the payload for the assignment
    payload = {"teacher_id": teacher.id}

    # Make a PUT request to assign the teacher to the course
    response = client.put(f"/courses/{course.id}/assign-teacher", json=payload)

    assert response.status_code == 200
    assert response.json == {"message": "Teacher assigned successfully."}
    
    # Verify that the course object is updated in the database
    updated_course = Course.query.get(course.id)
    assert updated_course.teacher_id == teacher.id

def test_assign_teacher_invalid_id(client, setup_data):
    """Test assigning a teacher with an invalid ID to a course."""
    teacher, course = setup_data

    # Define the payload with an invalid teacher ID
    payload = {"teacher_id": 9999}  # Assuming this ID does not exist

    response = client.put(f"/courses/{course.id}/assign-teacher", json=payload)

    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Invalid teacher ID."}}

def test_get_course_details_with_teacher(client, setup_data):
    """Test retrieving course details with assigned teacher information."""
    teacher, course = setup_data

    # Assign teacher to the course first
    course.teacher_id = teacher.id
    db.session.commit()

    response = client.get(f"/courses/{course.id}")

    assert response.status_code == 200
    assert "teacher" in response.json
    assert response.json['teacher']['id'] == teacher.id
    assert response.json['teacher']['name'] == teacher.name

def test_get_course_details_without_teacher(client, setup_data):
    """Test retrieving course details without assigned teacher."""
    teacher, course = setup_data

    response = client.get(f"/courses/{course.id}")

    assert response.status_code == 200
    assert "teacher" not in response.json
```