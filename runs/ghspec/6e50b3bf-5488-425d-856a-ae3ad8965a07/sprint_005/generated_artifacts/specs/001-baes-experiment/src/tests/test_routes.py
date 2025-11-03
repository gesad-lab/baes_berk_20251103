```python
import pytest
from flask import json
from src.routes import app, db
from src.models import Teacher  # Importing the Teacher model

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables for the test
            yield client  # Yield the test client for use in tests
            db.drop_all()  # Drop all tables after tests run

def test_create_teacher(client):
    """Test creating a new teacher with valid data."""
    teacher_data = {
        "name": "John Doe",
        "email": "johndoe@example.com"
    }
    response = client.post('/api/v1/teachers', 
                           data=json.dumps(teacher_data), 
                           content_type='application/json')
    assert response.status_code == 201  # Expecting 201 Created
    assert 'id' in response.json  # Check if ID is in the response
    assert response.json['name'] == teacher_data['name']
    assert response.json['email'] == teacher_data['email']

def test_retrieve_teacher(client):
    """Test retrieving a teacher's details by ID."""
    # First create a teacher to retrieve
    teacher_data = {
        "name": "Jane Smith",
        "email": "janesmith@example.com"
    }
    create_response = client.post('/api/v1/teachers', 
                                   data=json.dumps(teacher_data), 
                                   content_type='application/json')
    teacher_id = create_response.json['id']

    # Now retrieve the newly created teacher
    response = client.get(f'/api/v1/teachers/{teacher_id}')
    assert response.status_code == 200  # Expecting 200 OK
    assert response.json['name'] == teacher_data['name']
    assert response.json['email'] == teacher_data['email']

def test_create_teacher_with_missing_fields(client):
    """Test creating a teacher with missing fields returns an error."""
    teacher_data = {
        "email": "missingname@example.com"  # Name is missing
    }
    response = client.post('/api/v1/teachers', 
                           data=json.dumps(teacher_data), 
                           content_type='application/json')
    assert response.status_code == 400  # Expecting 400 Bad Request
    assert response.json['error']['code'] == 'E001'  # Assuming specific error code for validation
    assert 'name' in response.json['error']['message']  # Check error message includes name requirement
```