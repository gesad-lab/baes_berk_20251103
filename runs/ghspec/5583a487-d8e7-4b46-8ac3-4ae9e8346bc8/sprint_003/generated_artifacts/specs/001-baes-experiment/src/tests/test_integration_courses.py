```python
import pytest
from flask import jsonify
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
            db.drop_all()  # Clean up after tests

def test_create_course(client):
    """Test the creation of a new course with valid input."""
    response = client.post('/courses', json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.get_json() == {"message": "Course created successfully."}

def test_create_course_missing_fields(client):
    """Test creating a course without required fields."""
    response = client.post('/courses', json={"name": "", "level": ""})
    assert response.status_code == 400
    assert response.get_json() == {"error": {"code": "E001", "message": "Both name and level are required."}}

def test_get_courses(client):
    """Test retrieving the list of courses."""
    # Create a course to get
    client.post('/courses', json={"name": "Science", "level": "Intermediate"})
    
    response = client.get('/courses')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['name'] == "Science"
    assert data[0]['level'] == "Intermediate"
```