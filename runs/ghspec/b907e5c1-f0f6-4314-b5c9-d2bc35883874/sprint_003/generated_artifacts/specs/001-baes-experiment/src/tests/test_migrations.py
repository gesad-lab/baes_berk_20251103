```python
import pytest
from flask import json
from your_application import create_app  # import your app factory function
from your_application.models import db, Course  # import db and Course model
from your_application.database import init_db  # import your database initialization function

@pytest.fixture
def app():
    """Create a Flask application for testing."""
    app = create_app('testing')  # Use the testing configuration
    with app.app_context():
        init_db()  # Initialize the database
        yield app

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

def test_create_course(client):
    """Test creating a new course with valid data."""
    response = client.post('/courses', json={
        'name': 'Mathematics',
        'level': 'Beginner'
    })
    assert response.status_code == 201  # Check if the response status is 201 Created
    json_data = json.loads(response.data)
    assert json_data['message'] == 'Course created successfully'
    
    # Verify that the course is stored in the database
    course = Course.query.filter_by(name='Mathematics').first()
    assert course is not None
    assert course.level == 'Beginner'

def test_get_course(client):
    """Test retrieving a course by ID."""
    # Create a course to retrieve later
    new_course = Course(name='Science', level='Intermediate')
    db.session.add(new_course)
    db.session.commit()
    
    response = client.get(f'/courses/{new_course.id}')
    assert response.status_code == 200  # Check if the response status is 200 OK
    json_data = json.loads(response.data)
    assert json_data['name'] == 'Science'
    assert json_data['level'] == 'Intermediate'

def test_create_course_missing_fields(client):
    """Test error handling for missing fields when creating a course."""
    response = client.post('/courses', json={})
    assert response.status_code == 400  # Check if the response status is 400 Bad Request
    json_data = json.loads(response.data)
    assert json_data['error']['code'] == 'E001'
    assert json_data['error']['message'] == 'Both name and level fields are required'

def test_get_all_courses(client):
    """Test retrieving a list of all courses."""
    # Create a couple of courses
    course1 = Course(name='History', level='Advanced')
    course2 = Course(name='Geography', level='Intermediate')
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    response = client.get('/courses')
    assert response.status_code == 200  # Check if the response status is 200 OK
    json_data = json.loads(response.data)
    assert len(json_data) == 2  # Ensure all courses are returned
    assert any(course['name'] == 'History' for course in json_data)
    assert any(course['name'] == 'Geography' for course in json_data)
```