```python
import json
import pytest
from api import create_app, db
from api.models import Course, Teacher  # Importing the necessary models

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        # Creating a sample teacher to assign
        sample_teacher = Teacher(name="John Doe", email="john@example.com")
        db.session.add(sample_teacher)
        db.session.commit()

        yield app.test_client()

        db.drop_all()  # Clean up after tests


def test_assign_teacher_to_course(test_client):
    """Test assigning a teacher to a course successfully."""
    # Setup: creating a course to assign
    course = Course(name="Mathematics")
    db.session.add(course)
    db.session.commit()

    response = test_client.post(f'/courses/{course.id}/assign-teacher', json={'teacher_id': 1})
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['course']['teacher_id'] == 1
    assert data['course']['name'] == "Mathematics"


def test_assign_teacher_to_non_existing_course(test_client):
    """Test assigning a teacher to a non-existing course."""
    response = test_client.post('/courses/999/assign-teacher', json={'teacher_id': 1})
    
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error']['code'] == 'E404'
    assert data['error']['message'] == 'Course not found'


def test_assign_non_existing_teacher_to_course(test_client):
    """Test assigning a non-existing teacher to a course."""
    # Setup: creating a course
    course = Course(name="Biology")
    db.session.add(course)
    db.session.commit()

    response = test_client.post(f'/courses/{course.id}/assign-teacher', json={'teacher_id': 999})
    
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error']['code'] == 'E404'
    assert data['error']['message'] == 'Teacher not found'


def test_update_teacher_assignment_for_course(test_client):
    """Test reassigning a teacher to an existing course."""
    # Setup: creating a course and assigning a teacher
    course = Course(name="Chemistry")
    db.session.add(course)
    db.session.commit()

    # Assign the first teacher
    test_client.post(f'/courses/{course.id}/assign-teacher', json={'teacher_id': 1})

    # Now reassign to the same teacher or a different one if needed
    response = test_client.post(f'/courses/{course.id}/assign-teacher', json={'teacher_id': 1})
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['course']['teacher_id'] == 1
    assert data['course']['name'] == "Chemistry"

```