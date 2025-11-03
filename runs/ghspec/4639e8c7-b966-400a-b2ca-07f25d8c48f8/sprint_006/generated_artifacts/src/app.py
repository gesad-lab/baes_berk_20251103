```python
import pytest
from flask import json
from src.app import create_app  # Import the Flask application factory
from src.models import db, Teacher, Course  # Import the Course model for testing

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    # Set up the database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create database tables
        yield app.test_client()  # Provide a test client for requests

def test_create_course_with_teacher(client):
    """Test to ensure an Admin can associate a teacher with a course while creating it."""
    # Given a teacher exists in the DB
    teacher_data = {"name": "Jane Doe"}
    response = client.post('/teachers', json=teacher_data)
    assert response.status_code == 201  # Teacher created successfully

    # When creating a new course with the teacher's ID
    course_data = {"name": "Mathematics", "teacher_id": 1}
    response = client.post('/courses', json=course_data)
    
    # Then the course should be created successfully with the teacher associated
    assert response.status_code == 201  # Course creation successful
    course_response = json.loads(response.data)
    assert course_response['teacher_id'] == 1  # Validate teacher_id is set

def test_update_course_teacher(client):
    """Test to ensure an Admin can update a course's associated teacher."""
    # Given a teacher and course exist
    teacher_data = {"name": "Jane Doe"}
    response = client.post('/teachers', json=teacher_data)
    assert response.status_code == 201  # Teacher created successfully

    course_data = {"name": "Mathematics", "teacher_id": 1}
    response = client.post('/courses', json=course_data)
    assert response.status_code == 201  # Course created successfully

    # When updating the course to a different teacher
    new_teacher_data = {"name": "John Smith"}
    response = client.post('/teachers', json=new_teacher_data)
    assert response.status_code == 201  # New teacher created successfully

    update_data = {"teacher_id": 2}  # Assuming new teacher gets ID 2
    response = client.put('/courses/1', json=update_data)

    # Then the course should be updated with the new teacher
    assert response.status_code == 200  # Course updated successfully
    updated_course_response = json.loads(response.data)
    assert updated_course_response['teacher_id'] == 2  # Validate updated teacher_id

def test_course_without_teacher(client):
    """Test to ensure a course can be created without assigning a teacher."""
    # When creating a new course without a teacher
    course_data = {"name": "History"}
    response = client.post('/courses', json=course_data)
    
    # Then the course should be created successfully without a teacher
    assert response.status_code == 201  # Course creation successful
    course_response = json.loads(response.data)
    assert course_response['teacher_id'] is None  # Validate teacher_id is None

def test_fetch_course_with_teacher(client):
    """Test to ensure the system maintains integrity of course-teacher associations when retrieving."""
    # Given a teacher and course are created
    teacher_data = {"name": "Jane Doe"}
    response = client.post('/teachers', json=teacher_data)
    assert response.status_code == 201  # Teacher created successfully
    
    course_data = {"name": "Mathematics", "teacher_id": 1}
    response = client.post('/courses', json=course_data)
    assert response.status_code == 201  # Course created successfully

    # When fetching course details
    response = client.get('/courses/1')

    # Then the course details should accurately reflect the teacher information
    assert response.status_code == 200  # Fetch course successful
    course_response = json.loads(response.data)
    assert course_response['teacher_id'] == 1  # Validate correct teacher_id is shown
```