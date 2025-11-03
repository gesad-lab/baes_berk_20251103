```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.student import Student
from src.models.course import Course  # Importing the new Course model

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})

    with app.app_context():
        # Create the database and tables for Student and Course
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture for providing a test client for the Flask application."""
    return app.test_client()

def test_create_course(client):
    """Test the creation of a new course."""
    response = client.post('/courses', 
                            data=json.dumps({'name': 'Biology', 'level': 'Undergraduate'}),
                            content_type='application/json')
    
    assert response.status_code == 201  # Check if the status code is 201 Created
    data = json.loads(response.data)
    assert 'name' in data and 'level' in data  # Ensure the response includes 'name' and 'level'
    assert data['name'] == 'Biology'  # Verify the course name
    assert data['level'] == 'Undergraduate'  # Verify the course level

def test_get_courses(client):
    """Test retrieving all courses."""
    # First create a course to retrieve
    client.post('/courses', 
                data=json.dumps({'name': 'Chemistry', 'level': 'Undergraduate'}),
                content_type='application/json')

    response = client.get('/courses')
    
    assert response.status_code == 200  # Check if the status code is 200 OK
    data = json.loads(response.data)
    assert isinstance(data, list)  # Ensure the response is a list
    assert len(data) > 0  # Verify that there are courses returned
    assert 'name' in data[0] and 'level' in data[0]  # Verify course fields in the response
```