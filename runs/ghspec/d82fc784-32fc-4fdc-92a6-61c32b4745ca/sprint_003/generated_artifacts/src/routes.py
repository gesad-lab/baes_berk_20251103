```python
import pytest
from app import create_app, db
from app.models import Student, Course  # Importing the new Course model

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
    # Existing test implementation (not shown for brevity)

# New test for creating a course
def test_create_course(client):
    # Test creating a new course
    response = client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json['message'] == 'Course created successfully'  # Assuming a success message

# New test for retrieving all courses
def test_retrieve_courses(client):
    # First create a course to retrieve
    client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    
    # Test retrieving courses
    response = client.get('/courses')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check if it returns a list
    assert len(response.json) > 0  # Ensure there's at least one course retrieved
```