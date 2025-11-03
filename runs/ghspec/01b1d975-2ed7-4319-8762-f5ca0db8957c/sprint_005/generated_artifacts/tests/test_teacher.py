```python
import pytest
from flask import json
from src.app import create_app  # Assuming there's a create_app function to initialize the Flask app
from src.models import db, Teacher  # Importing the database and Teacher model

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app({'TESTING': True})  # Configure the app for testing
    with app.app_context():
        db.create_all()  # Create the database tables
        yield app
        db.drop_all()  # Clean up after the tests

@pytest.fixture
def client(app):
    """Provide a test client for the app."""
    return app.test_client()

def test_create_teacher_success(client):
    """Test the creation of a Teacher with valid details."""
    response = client.post('/teachers', 
                            data=json.dumps({"name": "John Doe", "email": "john.doe@example.com"}),
                            content_type='application/json')
    assert response.status_code == 201
    json_data = response.get_json()
    assert 'id' in json_data  # Verify the response contains the Teacher ID

def test_create_teacher_validation_error(client):
    """Test the creation of a Teacher with missing required fields."""
    response = client.post('/teachers', 
                            data=json.dumps({"name": "", "email": ""}),
                            content_type='application/json')
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error']['code'] == 'E001'  # Check for specific validation error code
    assert 'name' in json_data['error']['details']  # 'name' field should be in error details
    assert 'email' in json_data['error']['details']  # 'email' field should be in error details

def test_retrieve_teacher_success(client):
    """Test retrieving Teacher data by ID."""
    # First create a teacher to retrieve
    create_response = client.post('/teachers', 
                                   data=json.dumps({"name": "Jane Doe", "email": "jane.doe@example.com"}),
                                   content_type='application/json')
    teacher_id = create_response.get_json()['id']

    response = client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['id'] == teacher_id
    assert json_data['name'] == "Jane Doe"
    assert json_data['email'] == "jane.doe@example.com"

def test_retrieve_teacher_not_found(client):
    """Test retrieving a Teacher that does not exist."""
    response = client.get('/teachers/999999')  # An ID that does not exist
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['error']['code'] == 'E002'  # Check for not found error code
```