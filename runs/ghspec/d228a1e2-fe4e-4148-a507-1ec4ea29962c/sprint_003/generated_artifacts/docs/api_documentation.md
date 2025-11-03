```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application and database for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Assuming Course model is defined elsewhere and imported here
from src.models.course import Course  # Importing the Course model

# Setting up the test database
@pytest.fixture
def client():
    with app.app_context():
        db.create_all()  # Create all tables
        yield app.test_client()  # Provide the test client

        db.drop_all()  # Cleanup after the tests

# Test case: Creating a Course with valid data
def test_create_course_success(client):
    response = client.post('/courses', json={'name': 'Math 101', 'level': 'Beginner'})
    assert response.status_code == 201  # Check if course creation is successful
    assert 'id' in response.json  # Check if the response contains the course ID

# Test case: Creating a Course without name
def test_create_course_missing_name(client):
    response = client.post('/courses', json={'level': 'Beginner'})
    assert response.status_code == 400  # Expect a Bad Request error
    assert 'error' in response.json  # Check for error message in the response

# Test case: Creating a Course without level
def test_create_course_missing_level(client):
    response = client.post('/courses', json={'name': 'Math 101'})
    assert response.status_code == 400  # Expect a Bad Request error
    assert 'error' in response.json  # Check for error message in the response

# Test case: Retrieving a non-existent Course by ID
def test_get_non_existent_course(client):
    response = client.get('/courses/9999')  # Assuming this ID does not exist
    assert response.status_code == 404  # Expect a Not Found error
    assert 'error' in response.json  # Check for error message in the response

# Test case: Listing all Courses
def test_list_courses(client):
    # Create a course to test retrieval
    client.post('/courses', json={'name': 'Math 101', 'level': 'Beginner'})
    client.post('/courses', json={'name': 'Science 101', 'level': 'Intermediate'})

    response = client.get('/courses')  # Get the list of courses
    assert response.status_code == 200  # Check if retrieval is successful
    assert len(response.json) == 2  # Check if two courses are retrieved
    assert response.json[0]['name'] == 'Math 101'  # Validate course details
    assert response.json[1]['name'] == 'Science 101'
```