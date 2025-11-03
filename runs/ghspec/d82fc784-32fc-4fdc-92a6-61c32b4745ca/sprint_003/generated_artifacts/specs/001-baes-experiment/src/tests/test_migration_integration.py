```python
import pytest
from app import create_app, db
from app.models import Student, Course  # Ensure Course is imported

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

def test_create_course(client):
    """Test the creation of a new course."""
    response = client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201  # Check for successful creation

def test_retrieve_courses(client):
    """Test the retrieval of courses."""
    # First, create a course to retrieve
    client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    
    response = client.get('/courses')
    assert response.status_code == 200  # Check for successful retrieval
    assert isinstance(response.json, list)  # Check if it returns a list
    assert len(response.json) > 0  # Verify that the list is not empty
    assert response.json[0]['name'] == "Math 101"  # Verify course data
```