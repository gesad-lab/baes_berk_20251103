```python
import pytest
from flask import json
from src.app import create_app  # Import the Flask application factory
from src.models import db  # Import the database instance to manage the app context

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    # Set up the database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()  # Create database tables
        with app.test_client() as client:
            yield client
        db.drop_all()  # Clean up after tests

def test_create_course(client):
    """Test that creating a course with valid data returns a success response."""
    response = client.post('/courses', json={'name': 'Math 101', 'level': 'beginner'})
    assert response.status_code == 201  # Check for HTTP 201 Created
    data = json.loads(response.data)
    assert 'id' in data  # Ensure that an ID is returned

def test_get_courses(client):
    """Test that retrieving courses returns a list of courses."""
    client.post('/courses', json={'name': 'Math 101', 'level': 'beginner'})  # Create a course
    response = client.get('/courses')
    assert response.status_code == 200  # Check for HTTP 200 OK
    data = json.loads(response.data)
    assert isinstance(data, list)  # Ensure the result is a list

def test_create_course_with_empty_name(client):
    """Test that creating a course with an empty name returns an error."""
    response = client.post('/courses', json={'name': '', 'level': 'beginner'})
    assert response.status_code == 400  # Check for HTTP 400 Bad Request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Check for specific error code

def test_create_course_with_missing_level(client):
    """Test that creating a course without a level returns an error."""
    response = client.post('/courses', json={'name': 'Science 101'})
    assert response.status_code == 400  # Check for HTTP 400 Bad Request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'  # Check for specific error code

def test_associate_student_with_course(client):
    """Test that associating a student with a course returns a success response."""
    # Assuming 'students' endpoint to create a student first
    student_response = client.post('/students', json={'name': 'John Doe'})  
    assert student_response.status_code == 201
    student_id = json.loads(student_response.data)['id']
    
    course_response = client.post('/courses', json={'name': 'Math 101', 'level': 'beginner'})
    assert course_response.status_code == 201
    course_id = json.loads(course_response.data)['id']
    
    association_response = client.post('/associations', json={'student_id': student_id, 'course_id': course_id})  # Endpoint to associate
    assert association_response.status_code == 201  # Check for HTTP 201 Created

def test_get_student_courses(client):
    """Test that retrieving a student's courses works correctly."""
    student_response = client.post('/students', json={'name': 'Jane Doe'})
    assert student_response.status_code == 201
    student_id = json.loads(student_response.data)['id']
    
    course_response = client.post('/courses', json={'name': 'Art 101', 'level': 'intermediate'})
    assert course_response.status_code == 201
    course_id = json.loads(course_response.data)['id']
    
    client.post('/associations', json={'student_id': student_id, 'course_id': course_id})
    student_courses_response = client.get(f'/students/{student_id}/courses')
    assert student_courses_response.status_code == 200
    data = json.loads(student_courses_response.data)
    assert isinstance(data, list)  # Ensure the result is a list
    assert len(data) == 1  # We've added one course to this student
```