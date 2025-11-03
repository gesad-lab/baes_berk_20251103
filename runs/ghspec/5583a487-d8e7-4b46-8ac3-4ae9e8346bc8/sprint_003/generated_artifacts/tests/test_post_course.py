```python
import pytest
from flask import jsonify, request
from app import app, db, Course  # Import the Course model from the main application

# Setup the Flask application for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Cleanup the database after tests

def test_create_course_success(client):
    """Test successful creation of a new course."""
    response = client.post('/courses', json={
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    })
    assert response.status_code == 201  # Check for Created status
    data = response.get_json()
    assert data['message'] == 'Course created successfully'  # Check success message

def test_create_course_missing_fields(client):
    """Test creation of a course with missing name and level."""
    response = client.post('/courses', json={})
    assert response.status_code == 400  # Check for Bad Request status
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Check error code for missing fields
    assert data['error']['message'] == 'Both name and level fields are required.'

def test_retrieve_courses(client):
    """Test retrieval of course information."""
    # First create a course to retrieve
    client.post('/courses', json={
        'name': 'Introduction to Programming',
        'level': 'Beginner'
    })

    response = client.get('/courses')
    assert response.status_code == 200  # Check for OK status
    data = response.get_json()
    assert isinstance(data, list)  # Check that the response is a list
    assert len(data) == 1  # Ensure there's one course created
    assert data[0]['name'] == 'Introduction to Programming'
    assert data[0]['level'] == 'Beginner'
```