```python
import pytest
from flask import json
from src.app import create_app  # Assuming there's a create_app function to initialize the Flask app
from src.models import db, Course, Student  # Importing the database, Course, and Student models

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app({'TESTING': True})  # Configure the app for testing
    with app.app_context():
        db.create_all()  # Create the database tables
        yield app
        db.drop_all()  # Clean up after each test

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def add_student(app):
    """Create a student record for testing."""
    with app.app_context():
        student = Student(name="Test Student")
        db.session.add(student)
        db.session.commit()
        return student

@pytest.mark.parametrize("course_id", [999, 1000])  # Assuming 999 and 1000 do not exist
def test_enroll_student_in_non_existing_course(client, add_student, course_id):
    """Test enrollment validation error for non-existing courses."""
    response = client.post(f'/students/{add_student.id}/enroll', 
                           data=json.dumps({'course_id': course_id}),
                           content_type='application/json')
    assert response.status_code == 400  # Expect Bad Request
    assert response.json['error'] == {
        'code': 'E001',
        'message': 'Course not found.',
        'details': {'course_id': course_id}
    }

def test_enroll_student_with_no_course_id(client, add_student):
    """Test enrollment validation error when no course ID is provided."""
    response = client.post(f'/students/{add_student.id}/enroll', 
                           data=json.dumps({}),  # No course_id provided
                           content_type='application/json')
    assert response.status_code == 400  # Expect Bad Request
    assert response.json['error'] == {
        'code': 'E002',
        'message': 'Course ID is required.',
        'details': {}
    }

def test_enroll_student_with_invalid_course_id_type(client, add_student):
    """Test enrollment validation error when course ID is not an integer."""
    response = client.post(f'/students/{add_student.id}/enroll', 
                           data=json.dumps({'course_id': "not-an-integer"}), 
                           content_type='application/json')
    assert response.status_code == 400  # Expect Bad Request
    assert response.json['error'] == {
        'code': 'E003',
        'message': 'Invalid course ID format.',
        'details': {}
    }
```