```python
import pytest
from flask import json
from app import create_app, db
from src.models.course import Course  # Importing Course model
from src.models.teacher import Teacher  # Importing Teacher model
from src.services.course_service import assign_teacher_to_course, get_course_with_teacher  # Importing service functions

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
            yield client  # Provide the client for tests
            db.drop_all()  # Cleanup after tests

def test_assign_teacher_to_course(client):
    """Test case for assigning a teacher to a course."""
    
    # Create a teacher and course in the test database
    teacher = Teacher(name='John Doe')
    db.session.add(teacher)
    db.session.commit()

    course = Course(title='Mathematics 101')
    db.session.add(course)
    db.session.commit()

    # Assign the teacher to the course
    response = assign_teacher_to_course(course.id, teacher.id)

    # Assert the response to ensure assignment was successful
    assert response['status'] == 'success'
    assert response['data']['course_id'] == course.id
    assert response['data']['teacher_id'] == teacher.id

def test_get_course_with_teacher(client):
    """Test case for retrieving a course with assigned teacher details."""

    # Create a teacher and course in the test database
    teacher = Teacher(name='Jane Smith')
    db.session.add(teacher)
    db.session.commit()

    course = Course(title='Biology 101', teacher_id=teacher.id)
    db.session.add(course)
    db.session.commit()

    # Retrieve course with teacher information
    response = get_course_with_teacher(course.id)

    # Assert the retrieved data is correct
    assert response['course']['title'] == course.title
    assert response['course']['teacher']['name'] == teacher.name
```