```python
import json
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Assume the Course model is defined in the same manner as outlined in the specification
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)

    def __init__(self, name: str, level: str):
        if not name:
            raise ValueError("Course name cannot be empty")
        if not level:
            raise ValueError("Course level cannot be empty")
        self.name = name
        self.level = level


# Create a fixture to set up the database
@pytest.fixture
def client():
    with app.test_request_context():
        db.create_all()  # Create all tables
        yield app.test_client()
        db.drop_all()  # Drop all tables after tests


# Test suite for the Course model
def test_create_course_successful(client):
    """Test if a course can be created successfully."""
    response = client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    assert response.status_code == 201  # Ensure the status code is 201 Created
    assert 'id' in response.json  # Ensure the response includes an id
    assert response.json['name'] == 'Mathematics'  # Check if name matches
    assert response.json['level'] == 'Beginner'  # Check if level matches


def test_create_course_missing_name(client):
    """Test if an error is returned when course name is missing."""
    response = client.post('/courses', json={'level': 'Beginner'})
    assert response.status_code == 400  # Ensure the status code is 400 Bad Request
    assert response.json['error'] == {
        'code': 'E001',
        'message': 'Course name cannot be empty',
        'details': {}
    }


def test_create_course_missing_level(client):
    """Test if an error is returned when course level is missing."""
    response = client.post('/courses', json={'name': 'Mathematics'})
    assert response.status_code == 400  # Ensure the status code is 400 Bad Request
    assert response.json['error'] == {
        'code': 'E002',
        'message': 'Course level cannot be empty',
        'details': {}
    }


def test_retrieve_course_information(client):
    """Test to retrieve a list of all courses."""
    # First create a course
    client.post('/courses', json={'name': 'Mathematics', 'level': 'Beginner'})
    response = client.get('/courses')
    assert response.status_code == 200  # Ensure the status code is 200 OK
    assert isinstance(response.json, list)  # Ensure the response is a list
    assert len(response.json) == 1  # Check that there is one course in the list
    assert response.json[0]['name'] == 'Mathematics'  # Check the name of the course
    assert response.json[0]['level'] == 'Beginner'  # Check the level of the course
```