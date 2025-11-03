```python
import pytest
from flask import json
from app import create_app, db
from src.models.course import Course  # Import the Course model

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup the database before tests
        yield client
        db.drop_all()  # Clean up after tests

def test_create_course_with_valid_data(client):
    """Test course creation with valid name and level."""
    new_course = {
        'name': 'Physics 101',
        'level': 'Beginner'
    }
    response = client.post('/api/courses', data=json.dumps(new_course), content_type='application/json')
    assert response.status_code == 201  # Verify that creation was successful
    data = json.loads(response.data)
    assert 'id' in data  # Verify that the ID of the new course is returned
    assert data['name'] == new_course['name']
    assert data['level'] == new_course['level']

def test_create_course_with_missing_name(client):
    """Test course creation without a name."""
    new_course = {
        'level': 'Beginner'
    }
    response = client.post('/api/courses', data=json.dumps(new_course), content_type='application/json')
    assert response.status_code == 400  # Verify that a bad request is returned
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E001'  # Check specific error code
    assert error_data['error']['message'] == 'Name is required'  # Check error message

def test_create_course_with_missing_level(client):
    """Test course creation without a level."""
    new_course = {
        'name': 'Physics 101'
    }
    response = client.post('/api/courses', data=json.dumps(new_course), content_type='application/json')
    assert response.status_code == 400  # Verify that a bad request is returned
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E002'  # Check specific error code
    assert error_data['error']['message'] == 'Level is required'  # Check error message

def test_retrieve_courses(client):
    """Test retrieving the list of all courses."""
    # First, create a couple of courses
    client.post('/api/courses', data=json.dumps({'name': 'Physics 101', 'level': 'Beginner'}),
                content_type='application/json')
    client.post('/api/courses', data=json.dumps({'name': 'Chemistry 101', 'level': 'Intermediate'}),
                content_type='application/json')

    response = client.get('/api/courses')
    assert response.status_code == 200  # Verify that retrieval was successful
    courses = json.loads(response.data)
    assert len(courses) == 2  # Ensure that both courses are returned
    assert {'name': 'Physics 101', 'level': 'Beginner'} in courses
    assert {'name': 'Chemistry 101', 'level': 'Intermediate'} in courses
```