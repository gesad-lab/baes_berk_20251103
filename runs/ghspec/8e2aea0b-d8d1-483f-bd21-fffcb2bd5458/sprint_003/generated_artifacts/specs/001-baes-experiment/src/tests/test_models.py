```python
import json
import pytest
from flask import Flask
from flask.testing import FlaskClient
from src.app import create_app  # Assuming there is a function to create your Flask app
from src.models import db, Course  # Importing the Course model

@pytest.fixture
def client() -> FlaskClient:
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            # Create the database and add test data
            db.create_all()
            yield client
            db.drop_all()  # Clean up after tests

def test_create_course_with_valid_data(client):
    # Test course creation with valid data
    response = client.post('/courses', json={'name': 'Mathematics', 'level': '101'})
    assert response.status_code == 201  # 201 Created
    assert 'id' in response.json  # Check for course ID in the response
    assert response.json['name'] == 'Mathematics'
    assert response.json['level'] == '101'

def test_create_course_with_empty_fields(client):
    # Test error handling for empty fields
    response = client.post('/courses', json={'name': '', 'level': ''})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json == {
        "error": {
            "code": "E003",
            "message": "Name and level are required."
        }
    }

def test_retrieve_courses(client):
    # First, create a course to ensure there is data to retrieve
    client.post('/courses', json={'name': 'Science', 'level': '102'})
    
    # Test data retrieval of courses
    response = client.get('/courses')
    assert response.status_code == 200  # 200 OK
    assert isinstance(response.json, list)  # Ensure the response is a list
    assert len(response.json) > 0  # Ensure at least one course exists
    assert 'id' in response.json[0]  # Check for course ID in the first course
    assert 'name' in response.json[0]  # Check for course name
    assert 'level' in response.json[0]  # Check for course level
```