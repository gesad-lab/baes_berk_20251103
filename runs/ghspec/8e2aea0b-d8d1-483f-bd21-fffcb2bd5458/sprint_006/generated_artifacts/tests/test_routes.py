```python
import json
import pytest
from flask import Flask
from flask.testing import FlaskClient
from src.app import create_app
from src.models import db, Teacher, Course  # Importing the Course model

@pytest.fixture
def client() -> FlaskClient:
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            # Create the database and add test data
            db.create_all()
            # Add sample teacher
            teacher = Teacher(name='John Doe')
            db.session.add(teacher)
            db.session.commit()
            yield client

def test_assign_teacher_to_course(client):
    """Test assigning a teacher to an existing course."""

    # Create a test course
    course = Course(name='Math 101')
    db.session.add(course)
    db.session.commit()

    # Assign a teacher to the course
    response = client.put(
        f'/courses/{course.id}/assign_teacher',
        json={'teacher_id': teacher.id}  # Use the previously created teacher's ID
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Teacher assigned successfully'

    # Verify in the database
    updated_course = Course.query.get(course.id)
    assert updated_course.teacher_id == teacher.id

def test_view_course_with_assigned_teacher(client):
    """Test retrieving course details with assigned teacher information."""

    # Create a test teacher and course
    teacher = Teacher(name='Jane Smith')
    db.session.add(teacher)
    course = Course(name='Science 101', teacher_id=teacher.id)
    db.session.add(course)
    db.session.commit()

    # Retrieve course details
    response = client.get(f'/courses/{course.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Science 101'
    assert data['teacher']['name'] == 'Jane Smith'

def test_assign_teacher_to_invalid_course(client):
    """Test assigning a non-existent teacher to a course."""

    # Attempting to assign a teacher that does not exist
    response = client.put('/courses/999/assign_teacher', json={'teacher_id': 999})
    assert response.status_code == 404
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Assuming error code for resource not found
    assert data['error']['message'] == 'Course not found'

def test_assign_non_existent_teacher(client):
    """Test error handling for assigning a non-existent teacher to a course."""

    # Create a test course
    course = Course(name='History 101')
    db.session.add(course)
    db.session.commit()

    # Attempt to assign a non-existent teacher
    response = client.put(
        f'/courses/{course.id}/assign_teacher',
        json={'teacher_id': 999}  # Non-existent teacher ID
    )
    assert response.status_code == 404
    data = response.get_json()
    assert data['error']['code'] == 'E002'  # Assuming error code for teacher not found
    assert data['error']['message'] == 'Teacher not found'
```