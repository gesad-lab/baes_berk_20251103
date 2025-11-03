```python
import pytest
from flask import json
from app import app, db
from models import Teacher

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client
        with app.app_context():
            db.drop_all()  # Cleanup after tests

def test_create_teacher_success(client):
    """Test the creation of a new Teacher with valid data."""
    response = client.post('/teachers', 
                            data=json.dumps({"name": "John Doe", "email": "john.doe@example.com"}),
                            content_type='application/json')

    # Check for a successful creation response
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == "Teacher created successfully."
    assert data['teacher']['name'] == "John Doe"
    assert data['teacher']['email'] == "john.doe@example.com"

def test_create_teacher_missing_name(client):
    """Test the creation of a Teacher without a name field."""
    response = client.post('/teachers', 
                            data=json.dumps({"email": "john.doe@example.com"}),
                            content_type='application/json')
    
    # Check for a validation error response
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == "E001"
    assert data['error']['message'] == "Name and email are required."

def test_create_teacher_missing_email(client):
    """Test the creation of a Teacher without an email field."""
    response = client.post('/teachers', 
                            data=json.dumps({"name": "John Doe"}),
                            content_type='application/json')
    
    # Check for a validation error response
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == "E001"
    assert data['error']['message'] == "Name and email are required."

def test_retrieve_teacher_success(client):
    """Test retrieving the details of a teacher after creation."""
    # First create a teacher
    response = client.post('/teachers', 
                            data=json.dumps({"name": "John Doe", "email": "john.doe@example.com"}),
                            content_type='application/json')

    # Get the id of the created teacher
    teacher_id = json.loads(response.data)['teacher']['id']

    # Now retrieve the teacher by id
    response = client.get(f'/teachers/{teacher_id}')
    
    # Check that the retrieved teacher data matches the input data
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['teacher']['id'] == teacher_id
    assert data['teacher']['name'] == "John Doe"
    assert data['teacher']['email'] == "john.doe@example.com"
```