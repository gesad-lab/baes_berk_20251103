```python
import json
import pytest
from api import create_app, db
from api.models import Course, Student  # Ensure to import the Student model

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()  # Create the test client
        db.drop_all()  # Clean up the database after tests

def test_assign_courses_invalid_ids(test_client):
    """Ensure the API responds with validation errors for invalid course IDs when assigning to a student."""
    
    # Setup: Create a student in the database
    student = Student(name="John Doe")
    db.session.add(student)
    db.session.commit()
    
    # Attempt to assign invalid course IDs
    invalid_course_ids = [999, 1000]  # IDs that do not exist
    
    response = test_client.post(f'/students/{student.id}/courses', json={"course_ids": invalid_course_ids})
    
    # Check that we received a 400 Bad Request response with the expected error message
    assert response.status_code == 400
    response_json = response.get_json()
    assert response_json['error']['code'] == 'E001'  # Assuming E001 is the error code for invalid course
    assert response_json['error']['message'] == 'Some of the provided course IDs do not exist.'
    assert 'details' in response_json['error']  # Assert validation details are provided

def test_assign_courses_valid_ids(test_client):
    """Ensure the API successfully assigns valid course IDs to a student."""
    
    # Setup: Create a student and valid course in the database
    student = Student(name="John Doe")
    course = Course(name="Mathematics")
    db.session.add(student)
    db.session.add(course)
    db.session.commit()
    
    # Attempt to assign valid course IDs
    response = test_client.post(f'/students/{student.id}/courses', json={"course_ids": [course.id]})
    
    # Check that we received a 200 OK response with the updated student data
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['id'] == student.id
    assert len(response_json['courses']) == 1
    assert response_json['courses'][0]['id'] == course.id
```