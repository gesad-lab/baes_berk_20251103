```python
import pytest
from flask import json
from src.app import create_app  # Import the Flask application factory
from src.models import db, Teacher  # Import the Teacher model for testing

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    # Set up the database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create database tables
        yield app.test_client()  # Provide a test client

def test_create_teacher_success(client):
    """Test that an admin can successfully create a teacher."""
    response = client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201  # Check if the creation was successful
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_teacher_missing_fields(client):
    """Test that creating a teacher without name and/or email returns an error."""
    # Missing name
    response = client.post('/teachers', json={
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 400  # Bad request
    assert 'name' in json.loads(response.data)['error']['message']

    # Missing email
    response = client.post('/teachers', json={
        'name': 'John Doe'
    })
    assert response.status_code == 400  # Bad request
    assert 'email' in json.loads(response.data)['error']['message']

def test_get_teacher_details(client):
    """Test that existing teacher details can be retrieved successfully."""
    # First create a teacher
    client.post('/teachers', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    
    # Now retrieve the teacher's details
    response = client.get('/teachers/jane.doe@example.com')
    assert response.status_code == 200  # Check if retrieval was successful
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'
```