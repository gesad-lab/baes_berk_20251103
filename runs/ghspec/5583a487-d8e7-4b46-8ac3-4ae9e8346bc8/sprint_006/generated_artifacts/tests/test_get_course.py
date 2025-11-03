```python
import pytest
from flask import jsonify
from app import app, db, Course, Teacher  # Import the Course and Teacher models

# Setup the Flask application for testing with an in-memory SQLite database
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
            # Create a sample Teacher to associate with Courses
            teacher = Teacher(name="John Doe", email="john@example.com")
            db.session.add(teacher)
            db.session.commit()
            yield client  # Provide the test client to the test functions

def test_create_course_with_teacher(client):
    """Test creating a Course with an associated Teacher."""
    response = client.post('/courses', json={
        'title': 'Mathematics 101',
        'teacher_id': 1  # Assuming the teacher ID is 1
    })
    assert response.status_code == 201
    assert b'Course created successfully' in response.data

def test_create_course_without_teacher(client):
    """Test attempting to create a Course without specifying a Teacher."""
    response = client.post('/courses', json={
        'title': 'Mathematics 101',
        # No teacher_id provided
    })
    assert response.status_code == 400
    assert b'Missing required field: teacher_id' in response.data

def test_get_course_with_teacher(client):
    """Test retrieving a Course and checking associated Teacher details."""
    # Create a Course for testing
    client.post('/courses', json={
        'title': 'Physics 101',
        'teacher_id': 1  # Associate with the previously created teacher
    })
    
    response = client.get('/courses/1')  # Assuming the created course ID is 1
    assert response.status_code == 200
    data = jsonify(response.get_json())
    assert data['title'] == 'Physics 101'
    assert data['teacher']['name'] == 'John Doe'  # Check for associated teacher details

def test_get_non_existent_course(client):
    """Test retrieving a non-existent Course."""
    response = client.get('/courses/9999')  # Assuming this ID does not exist
    assert response.status_code == 404
    assert b'Course not found' in response.data
```