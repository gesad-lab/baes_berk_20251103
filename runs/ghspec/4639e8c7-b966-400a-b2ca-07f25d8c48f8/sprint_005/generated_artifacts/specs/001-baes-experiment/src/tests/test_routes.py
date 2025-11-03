```python
import pytest
from flask import json
from src.app import create_app  # Import the Flask application factory
from src.models import db  # Import the database instance to manage the app context
from src.models import Teacher  # Import the Teacher model for testing

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    # Set up the database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()  # Create database tables
        yield app.test_client()  # Provide access to the app test client

def test_create_teacher_with_valid_data(client):
    """Test that an admin can successfully create a teacher record with valid inputs."""
    response = client.post('/api/v1/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201  # Expect created response
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_teacher_missing_name(client):
    """Test that attempting to create a teacher without a name returns an error."""
    response = client.post('/api/v1/teachers', json={
        'email': 'email@example.com'
    })
    assert response.status_code == 400  # Expect bad request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'
    assert data['error']['message'] == 'Name is required.'

def test_create_teacher_missing_email(client):
    """Test that attempting to create a teacher without an email returns an error."""
    response = client.post('/api/v1/teachers', json={
        'name': 'John Doe'
    })
    assert response.status_code == 400  # Expect bad request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'
    assert data['error']['message'] == 'Email is required.'

def test_create_teacher_with_duplicate_email(client):
    """Test that attempting to create a teacher with a duplicate email returns an error."""
    # First create a teacher
    client.post('/api/v1/teachers', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    # Attempt to create another teacher with the same email
    response = client.post('/api/v1/teachers', json={
        'name': 'John Smith',
        'email': 'jane.doe@example.com'
    })
    assert response.status_code == 400  # Expect bad request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E003'
    assert data['error']['message'] == 'Email must be unique.'

def test_retrieve_teachers(client):
    """Test that an admin can retrieve the list of existing teachers."""
    # Create some teachers in the test database
    client.post('/api/v1/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    client.post('/api/v1/teachers', json={
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com'
    })
    
    # Now retrieve the list of teachers
    response = client.get('/api/v1/teachers')
    assert response.status_code == 200  # Expect success
    data = json.loads(response.data)
    assert len(data) == 2  # We expect two teachers in the response
    assert any(teacher['name'] == 'John Doe' for teacher in data)
    assert any(teacher['name'] == 'Jane Smith' for teacher in data)
```