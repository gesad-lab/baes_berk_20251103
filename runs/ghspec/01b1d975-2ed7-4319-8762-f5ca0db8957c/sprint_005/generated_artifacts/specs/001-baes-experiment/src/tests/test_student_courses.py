```python
import pytest
from flask import json
from src.app import create_app  # Assuming there's a create_app function to initialize the Flask app
from src.models import db, Course, Student, Teacher  # Importing the Teacher model along with existing models

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app({'TESTING': True})  # Configure the app for testing
    with app.app_context():
        db.create_all()  # Create the database tables
        yield app
        db.drop_all()  # Drop the database tables after tests

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()

@pytest.fixture
def create_teacher(client):
    """Helper function to create a Teacher for testing."""
    def _create_teacher(name, email):
        response = client.post('/teachers', json={'name': name, 'email': email})
        return response
    return _create_teacher

def test_create_teacher(client):
    """Test the creation of a Teacher."""
    response = create_teacher(client, 'John Doe', 'john.doe@example.com')
    assert response.status_code == 201  # Assert that creation returns 201 Created
    data = json.loads(response.data)
    assert 'id' in data  # Ensure an ID is returned
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_teacher_with_missing_fields(client):
    """Test creating a Teacher with missing fields should return 400 Bad Request."""
    response = client.post('/teachers', json={'name': 'Jane Doe'})
    assert response.status_code == 400  # Bad Request for missing email
    assert b'missing email' in response.data

def test_get_teacher(client, create_teacher):
    """Test retrieving a Teacher by ID."""
    create_teacher('Alice Smith', 'alice.smith@example.com')
    response = client.get('/teachers/1')  # Assuming the ID is 1 for the first created teacher
    assert response.status_code == 200  # Check for successful retrieval
    data = json.loads(response.data)
    assert data['name'] == 'Alice Smith'
    assert data['email'] == 'alice.smith@example.com'

def test_get_nonexistent_teacher(client):
    """Test retrieving a nonexistent Teacher should return 404 Not Found."""
    response = client.get('/teachers/999')  # Nonexistent ID
    assert response.status_code == 404  # Not Found
```