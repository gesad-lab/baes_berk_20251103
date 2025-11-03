```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.course import Course
from src.models.teacher import Teacher

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})

    with app.app_context():
        # Create the database and tables for Course and Teacher
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture for testing with the Flask test client."""
    return app.test_client()

def test_assign_teacher_success(client):
    """Test assigning a valid teacher to a course successfully."""
    # Arrange: create a course and a teacher for the tests
    teacher = Teacher(name="John Doe", email="john@example.com")
    course = Course(name="Mathematics", level="101")
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()
    
    # Act: assign the teacher to the course
    response = client.put(f'/courses/{course.id}/assign-teacher', json={'teacher_id': teacher.id})
    
    # Assert: check response and database update
    assert response.status_code == 200
    assert response.json == {
        "message": "Teacher assigned successfully.",
        "course": {
            "id": course.id,
            "name": course.name,
            "level": course.level,
            "teacher_id": teacher.id
        }
    }

def test_assign_teacher_invalid_teacher(client):
    """Test assigning a non-existent teacher to a course returns a validation error."""
    # Arrange: create a course
    course = Course(name="Science", level="102")
    db.session.add(course)
    db.session.commit()
    
    # Act: attempt to assign an invalid teacher
    response = client.put(f'/courses/{course.id}/assign-teacher', json={'teacher_id': 999})
    
    # Assert: check response for validation error
    assert response.status_code == 400
    assert response.json == {
        "error": {
            "code": "E002",
            "message": "The specified teacher does not exist."
        }
    }

def test_assign_teacher_update_existing_relationship(client):
    """Test assigning a teacher to a course that already has an assigned teacher."""
    # Arrange: create two teachers and a course
    teacher1 = Teacher(name="Jane Doe", email="jane@example.com")
    teacher2 = Teacher(name="John Smith", email="johnsmith@example.com")
    course = Course(name="History", level="201")
    db.session.add(teacher1)
    db.session.add(course)
    db.session.commit()
    
    # Act: assign the first teacher to the course
    client.put(f'/courses/{course.id}/assign-teacher', json={'teacher_id': teacher1.id})
    
    # Act: reassign a different teacher to the same course
    response = client.put(f'/courses/{course.id}/assign-teacher', json={'teacher_id': teacher2.id})
    
    # Assert: check response and ensure we updated the teacher correctly
    assert response.status_code == 200
    assert response.json == {
        "message": "Teacher assigned successfully.",
        "course": {
            "id": course.id,
            "name": course.name,
            "level": course.level,
            "teacher_id": teacher2.id
        }
    }

def test_get_course_with_teacher(client):
    """Test retrieving course information with an assigned teacher."""
    # Arrange: create a teacher and a course
    teacher = Teacher(name="Mark Brown", email="mark@example.com")
    course = Course(name="Art", level="301", teacher_id=teacher.id)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Act: get the course
    response = client.get(f'/courses/{course.id}')
    
    # Assert: check response with course details and teacher information
    assert response.status_code == 200
    assert response.json == {
        "id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher": {
            "name": teacher.name,
            "email": teacher.email
        }
    }

def test_get_course_invalid_id(client):
    """Test retrieving a course with an invalid course ID returns an error."""
    # Act: attempt to retrieve a course that does not exist
    response = client.get('/courses/999')
    
    # Assert: check response for error message
    assert response.status_code == 404
    assert response.json == {
        "error": {
            "code": "E003",
            "message": "Course not found."
        }
    }
```