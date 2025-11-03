```python
import pytest
from flask import jsonify
from app import app, db, Course  # Import the app and Course model from the main application

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
            db.drop_all()  # Clean up database after tests

def test_create_course_success(client):
    """Test creating a course with valid data returns 201 Created."""
    response = client.post('/courses', json={'name': 'Mathematics', 'level': 'Intermediate'})
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Course created successfully.'}

def test_create_course_missing_name(client):
    """Test creating a course without a name returns 400 Bad Request."""
    response = client.post('/courses', json={'level': 'Intermediate'})
    assert response.status_code == 400
    assert response.get_json() == {'error': {'code': 'E001', 'message': 'Name is required.'}}

def test_create_course_missing_level(client):
    """Test creating a course without a level returns 400 Bad Request."""
    response = client.post('/courses', json={'name': 'Mathematics'})
    assert response.status_code == 400
    assert response.get_json() == {'error': {'code': 'E002', 'message': 'Level is required.'}}

def test_get_courses_empty(client):
    """Test retrieving courses when none exist returns 200 OK with empty list."""
    response = client.get('/courses')
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_courses_after_creation(client):
    """Test retrieving courses returns the correct list after creation."""
    client.post('/courses', json={'name': 'Mathematics', 'level': 'Intermediate'})
    response = client.get('/courses')
    assert response.status_code == 200
    assert response.get_json() == [{'name': 'Mathematics', 'level': 'Intermediate'}]
```