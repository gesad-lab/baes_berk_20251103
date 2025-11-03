import pytest
from app import create_app, db
from app.models import Student, Course  # Assuming Course model has been defined

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after tests

def test_create_student(client):
    # Existing test for creating a student
    response = client.post('/students', json={"name": "John Doe", "age": 20})
    assert response.status_code == 201

def test_create_course(client):
    """Test creating a new course."""
    response = client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json['name'] == "Math 101"
    assert response.json['level'] == "Beginner"

def test_retrieve_courses(client):
    """Test retrieving the list of courses."""
    # First create a course to retrieve
    client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    
    response = client.get('/courses')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check if it returns a list
    assert len(response.json) > 0  # Ensure that there is at least one course in the list

def test_create_course_invalid_data(client):
    """Test creating a course with invalid data."""
    response = client.post('/courses', json={"name": "", "level": "Beginner"})  # Invalid name
    assert response.status_code == 400  # Expecting a Bad Request status

    response = client.post('/courses', json={"name": "Math 101"})  # Missing level
    assert response.status_code == 400  # Expecting a Bad Request status