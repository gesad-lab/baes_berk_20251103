```python
import json
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.teacher import Teacher  # Assuming Teacher model is defined in models.teacher

# Initialize the Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
db = SQLAlchemy(app)

@pytest.fixture
def client():
    """Fixture for creating a test client."""
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_database():
    """Fixture for initializing the database."""
    db.create_all()
    yield db
    db.drop_all()

def test_add_teacher_success(client, init_database):
    """Test adding a new teacher successfully."""
    response = client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_get_teacher_success(client, init_database):
    """Test retrieving teacher information by ID."""
    # First, add a teacher
    post_response = client.post('/teachers', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    teacher_id = json.loads(post_response.data)['id']

    # Now retrieve the teacher
    response = client.get(f'/teachers/{teacher_id}')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'

def test_add_teacher_invalid_email(client, init_database):
    """Test handling error when adding a teacher with an invalid email."""
    response = client.post('/teachers', json={
        'name': 'Invalid Teacher',
        'email': 'invalid-email'
    })
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error']['code'] == 'E001'  # Example error code for invalid email
    assert 'message' in data['error']

def test_add_teacher_missing_name(client, init_database):
    """Test handling error when adding a teacher without a name."""
    response = client.post('/teachers', json={
        'email': 'no.name@example.com'
    })
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error']['code'] == 'E002'  # Example error code for missing name
    assert 'message' in data['error']
```