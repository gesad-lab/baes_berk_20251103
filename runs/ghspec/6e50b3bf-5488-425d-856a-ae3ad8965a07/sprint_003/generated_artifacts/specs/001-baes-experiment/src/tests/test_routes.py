```python
import pytest
from flask import json
from src.routes import app, db
from src.models import Course

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables for the test
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after the test

def test_get_course_success(client):
    """Test successful retrieval of a course by ID."""
    # First, create a course to test against
    course_data = {"name": "Mathematics", "level": "Intermediate"}
    response = client.post('/courses', json=course_data)
    assert response.status_code == 201  # Course created successfully

    course_id = response.json['id']  # Get the ID of the created course

    # Now, retrieve the course by its ID
    response = client.get(f'/courses/{course_id}')
    
    assert response.status_code == 200  # Ensure request was successful
    assert response.json['id'] == course_id  # Check if the correct ID is returned
    assert response.json['name'] == course_data['name']  # Verify name
    assert response.json['level'] == course_data['level']  # Verify level

def test_get_course_not_found(client):
    """Test retrieval of a course that does not exist."""
    # Attempt to retrieve a course with a nonexistent ID
    response = client.get('/courses/999999')  # Assuming this ID doesn't exist
    assert response.status_code == 404  # Ensure it returns a Not Found status
    assert response.json['error']['code'] == 'E404'  # Assuming a well-defined error code
    assert response.json['error']['message'] == 'Course not found'  # Check the error message
```