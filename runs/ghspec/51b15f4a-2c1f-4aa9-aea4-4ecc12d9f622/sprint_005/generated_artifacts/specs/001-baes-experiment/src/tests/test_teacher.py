```python
# tests/test_teacher.py

import pytest
from app import create_app, db
from models.teacher import Teacher

@pytest.fixture(scope='module')
def test_client():
    """Initialize the app for testing and create a test client."""
    app = create_app('testing')  # Initialize app with testing configuration
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()  # Setup test database environment
        yield testing_client  # This is where the testing happens!
        db.drop_all()  # Cleanup the test database

def test_create_teacher(test_client):
    """Test creating a teacher successfully."""
    response = test_client.post('/api/v1/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    assert response.status_code == 201
    assert response.json['name'] == 'John Doe'
    assert response.json['email'] == 'john.doe@example.com'

def test_create_teacher_missing_name(test_client):
    """Test trying to create a teacher without a name."""
    response = test_client.post('/api/v1/teachers', json={
        'email': 'john.doe@example.com'
    })
    
    assert response.status_code == 400
    assert response.json['error']['message'] == 'Name is required'

def test_create_teacher_missing_email(test_client):
    """Test trying to create a teacher without an email."""
    response = test_client.post('/api/v1/teachers', json={
        'name': 'John Doe'
    })
    
    assert response.status_code == 400
    assert response.json['error']['message'] == 'Email is required'

def test_get_teacher(test_client):
    """Test retrieving a teacher by ID."""
    # First, create a teacher to retrieve
    response = test_client.post('/api/v1/teachers', json={
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com'
    })
    teacher_id = response.json['id']

    # Now retrieve the created teacher
    response = test_client.get(f'/api/v1/teachers/{teacher_id}')
    
    assert response.status_code == 200
    assert response.json['id'] == teacher_id
    assert response.json['name'] == 'Jane Smith'
    assert response.json['email'] == 'jane.smith@example.com'

def test_get_teacher_not_found(test_client):
    """Test retrieving a non-existent teacher."""
    response = test_client.get('/api/v1/teachers/9999')  # Assuming 9999 does not exist
    assert response.status_code == 404
    assert response.json['error']['message'] == 'Teacher not found'
```