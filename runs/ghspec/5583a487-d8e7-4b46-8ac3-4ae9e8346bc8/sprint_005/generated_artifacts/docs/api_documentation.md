```python
import pytest
from flask import jsonify
from app import app, db, Teacher  # Import the Teacher model from the main application

# Setup the Flask application for testing with an in-memory SQLite database
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
            yield client  # Provide the test client to the tests
            db.drop_all()  # Cleanup after tests

def test_create_teacher(client):
    """Test creating a new teacher with valid input."""
    response = client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201  # Verify the response status code
    assert 'id' in response.json  # Check if the teacher ID is returned
    assert response.json['name'] == 'John Doe'  # Validate the name
    assert response.json['email'] == 'john.doe@example.com'  # Validate the email

def test_retrieve_teacher(client):
    """Test retrieving teacher information."""
    # First, create a teacher
    create_response = client.post('/teachers', json={
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com'
    })
    teacher_id = create_response.json['id']  # Get the ID of the created teacher

    # Now retrieve the teacher
    response = client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200  # Verify the response status code
    assert response.json['id'] == teacher_id  # Confirm the teacher ID matches
    assert response.json['name'] == 'Jane Smith'  # Validate the name
    assert response.json['email'] == 'jane.smith@example.com'  # Validate the email

def test_retrieve_nonexistent_teacher(client):
    """Test retrieving a teacher that does not exist."""
    response = client.get('/teachers/999')  # Attempt to retrieve a non-existent teacher
    assert response.status_code == 404  # Expect a 404 Not Found
    assert 'error' in response.json  # Ensure error message present

def test_create_teacher_without_name(client):
    """Test trying to create a teacher without a name."""
    response = client.post('/teachers', json={
        'email': 'missing.name@example.com'
    })
    assert response.status_code == 400  # Expect a bad request
    assert response.json['error']['message'] == 'Name is required.'  # Check error message

def test_create_teacher_without_email(client):
    """Test trying to create a teacher without an email."""
    response = client.post('/teachers', json={
        'name': 'Missing Email'
    })
    assert response.status_code == 400  # Expect a bad request
    assert response.json['error']['message'] == 'Email is required.'  # Check error message
```