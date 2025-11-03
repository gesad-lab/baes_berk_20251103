```python
import pytest
from flask import json
from app import create_app, db
from src.models.teacher import Teacher  # Importing Teacher model
from src.services.teacher_service import create_teacher, get_teacher  # Importing service functions

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup the database before tests
            yield client  # This will allow us to use the client in our tests
            db.drop_all()  # Cleanup after tests

def test_create_teacher(client):
    """Test API for creating a new teacher."""
    response = client.post('/api/v1/teachers', 
                            data=json.dumps({'name': 'John Doe', 'email': 'john.doe@example.com'}),
                            content_type='application/json')
    
    assert response.status_code == 201  # Assert that the teacher was created successfully
    data = json.loads(response.data)
    assert data['teacher']['name'] == 'John Doe'
    assert data['teacher']['email'] == 'john.doe@example.com'

def test_get_teacher(client):
    """Test API for retrieving a teacher."""
    # First, create a teacher to retrieve
    client.post('/api/v1/teachers', 
                data=json.dumps({'name': 'Jane Smith', 'email': 'jane.smith@example.com'}),
                content_type='application/json')
    
    response = client.get('/api/v1/teachers?email=jane.smith@example.com')
    
    assert response.status_code == 200  # Assert we got a successful response
    data = json.loads(response.data)
    assert data['teacher']['name'] == 'Jane Smith'
    assert data['teacher']['email'] == 'jane.smith@example.com'

def test_create_teacher_invalid_email(client):
    """Test creating a teacher with an invalid email returns an error."""
    response = client.post('/api/v1/teachers', 
                            data=json.dumps({'name': 'Invalid Teacher', 'email': 'invalid-email'}),
                            content_type='application/json')
    
    assert response.status_code == 400  # Assert we got a bad request response
    assert 'Invalid email format' in str(response.data)

def test_create_teacher_missing_name(client):
    """Test creating a teacher with missing name returns an error."""
    response = client.post('/api/v1/teachers', 
                            data=json.dumps({'email': 'no-name@example.com'}),
                            content_type='application/json')
    
    assert response.status_code == 400  # Assert we got a bad request response
    assert 'Name is required' in str(response.data)
```