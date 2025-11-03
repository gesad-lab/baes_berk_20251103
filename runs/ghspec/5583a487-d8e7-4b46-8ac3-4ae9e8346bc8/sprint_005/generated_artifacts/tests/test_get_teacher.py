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
            yield client  # Allow tests to run using this client

# Scenario 1: Create a New Teacher
def test_create_teacher_success(client):
    response = client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201  # Check for 201 Created
    assert response.json == {'message': 'Teacher created successfully.'}

# Scenario 2: Retrieve Teacher Information
def test_retrieve_teacher_success(client):
    # First, create a teacher
    client.post('/teachers', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    
    response = client.get('/teachers/1')  # Get the teacher created above
    assert response.status_code == 200  # Check for 200 OK
    assert response.json['name'] == 'Jane Doe'
    assert response.json['email'] == 'jane.doe@example.com'

# Scenario 3: Validate Teacher Input
def test_create_teacher_missing_fields(client):
    response = client.post('/teachers', json={})  # Submit without required fields
    assert response.status_code == 400  # Check for 400 Bad Request
    assert response.json == {
        'error': {
            'code': 'E001',
            'message': 'Both name and email are required.'
        }
    }
```