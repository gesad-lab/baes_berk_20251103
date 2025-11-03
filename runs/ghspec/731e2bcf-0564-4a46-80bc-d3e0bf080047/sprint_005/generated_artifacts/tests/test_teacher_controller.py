```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.teacher import Teacher

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})

    with app.app_context():
        # Create the database and tables for Teacher
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture for providing a test client for the Flask application."""
    return app.test_client()

def test_create_teacher_success(client):
    """Test that creating a new teacher with valid data succeeds."""
    response = client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_teacher_missing_fields(client):
    """Test that creating a teacher without required fields returns an error."""
    response = client.post('/teachers', json={
        'name': '',
        'email': ''
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['message'] == "Name and email are required fields."

def test_create_teacher_duplicate_email(client):
    """Test creating a teacher with a duplicate email returns an error."""
    client.post('/teachers', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })

    response = client.post('/teachers', json={
        'name': 'John Smith',
        'email': 'jane.doe@example.com'
    })
    assert response.status_code == 409
    data = json.loads(response.data)
    assert data['error']['message'] == "Email already exists."
```