```python
import pytest
from flask import json
from src.app import create_app  # Import the Flask application factory
from src.models import db, Teacher, Course  # Import necessary models for testing

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create database tables
        # Seed the database with a teacher for testing
        teacher = Teacher(name="Test Teacher")  # Assuming Teacher has a name field
        db.session.add(teacher)
        db.session.commit()  
        yield app.test_client()  # Return the test client for making requests
        db.drop_all()  # Clean up after tests

def test_create_course_without_teacher(client):
    """Test the creation of a course without assigning a teacher."""
    response = client.post('/courses', json={
        'title': 'Test Course',
        'description': 'A course without a teacher'
    })
    assert response.status_code == 201  # Check for successful creation
    data = json.loads(response.data)
    assert data['title'] == 'Test Course'
    assert data.get('teacher_id') is None  # Verify no teacher assigned

def test_create_course_with_valid_teacher(client):
    """Test the creation of a course with a valid teacher assigned."""
    # Get the teacher ID from the database
    teacher = Teacher.query.first()
    response = client.post('/courses', json={
        'title': 'Test Course with Teacher',
        'description': 'A course assigned to a teacher',
        'teacher_id': teacher.id
    })
    assert response.status_code == 201  # Check for successful creation
    data = json.loads(response.data)
    assert data['title'] == 'Test Course with Teacher'
    assert data['teacher_id'] == teacher.id  # Verify teacher assigned correctly

def test_create_course_with_invalid_teacher(client):
    """Test the scenario where an invalid teacher ID is provided."""
    response = client.post('/courses', json={
        'title': 'Course with Invalid Teacher',
        'description': 'A course with a non-existent teacher',
        'teacher_id': 9999  # Assuming this ID does not exist
    })
    assert response.status_code == 400  # Check for bad request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Check specific error code
    assert data['error']['message'] == 'Invalid teacher ID provided.'  # Verify error message

def test_update_course_with_teacher(client):
    """Test updating a course to assign a new teacher."""
    # Create initial course without a teacher
    response = client.post('/courses', json={
        'title': 'Initial Course',
        'description': 'A course to be updated'
    })
    initial_course = json.loads(response.data)

    # Now update the course to assign a teacher
    teacher = Teacher.query.first()
    update_response = client.put(f'/courses/{initial_course["id"]}', json={
        'title': 'Updated Course',
        'description': 'Course is now updated.',
        'teacher_id': teacher.id
    })
    assert update_response.status_code == 200  # Check for successful update
    updated_course = json.loads(update_response.data)
    assert updated_course['teacher_id'] == teacher.id  # Verify the teacher assignment is updated

def test_update_course_with_invalid_teacher(client):
    """Test updating a course with an invalid teacher ID."""
    # Create a course first
    response = client.post('/courses', json={
        'title': 'Course to Update',
        'description': 'A course that we will update.'
    })
    course_to_update = json.loads(response.data)

    update_response = client.put(f'/courses/{course_to_update["id"]}', json={
        'title': 'Updated Course',
        'description': 'Trying to assign an invalid teacher.',
        'teacher_id': 9999  # Assuming this ID does not exist
    })
    assert update_response.status_code == 400  # Check for bad request
    data = json.loads(update_response.data)
    assert data['error']['code'] == 'E001'  # Check specific error code
    assert data['error']['message'] == 'Invalid teacher ID provided.'  # Verify error message
```