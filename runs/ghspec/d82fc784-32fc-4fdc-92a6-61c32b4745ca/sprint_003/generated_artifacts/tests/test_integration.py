```python
import pytest
from app import create_app, db
from app.models import Student, Course  # Import the newly created Course model

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
    # Existing test for Student creation
    response = client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 201

# New tests for Course routes

def test_create_course(client):
    """Test case for creating a new course."""
    response = client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201  # Expecting a successful creation response

def test_retrieve_courses(client):
    """Test case for retrieving the list of courses."""
    # First, create a course to ensure there is at least one course to retrieve
    client.post('/courses', json={"name": "Math 101", "level": "Beginner"})

    response = client.get('/courses')
    assert response.status_code == 200  # Expecting a success response
    assert isinstance(response.json, list)  # Check if it returns a list
    assert len(response.json) > 0  # Ensure there is at least one course in the list
```