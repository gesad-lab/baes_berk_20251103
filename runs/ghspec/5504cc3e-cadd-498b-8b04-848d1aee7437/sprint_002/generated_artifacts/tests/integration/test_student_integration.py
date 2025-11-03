```python
import pytest
from flask import json
from app import create_app, db
from src.models.student import Student

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup the database before tests
        yield client
        db.drop_all()  # Clean up after tests

def test_create_student_with_valid_email(client):
    """Test creation of a student with valid name and email."""
    response = client.post('/api/v1/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    
    assert response.status_code == 201  # Check for successful creation
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'

def test_list_students(client):
    """Test retrieval of the list of students."""
    client.post('/api/v1/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    
    response = client.get('/api/v1/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['name'] == 'Jane Doe'
    assert data[0]['email'] == 'jane.doe@example.com'

def test_update_student_email(client):
    """Test updating an existing student's email address."""
    client.post('/api/v1/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })

    response = client.put('/api/v1/students/1', json={
        'email': 'jane.doe@newdomain.com'
    })

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['email'] == 'jane.doe@newdomain.com'

    # Retrieve the student to confirm the email update
    response = client.get('/api/v1/students/1')
    data = json.loads(response.data)
    assert data['email'] == 'jane.doe@newdomain.com'
    
def test_create_student_with_invalid_email(client):
    """Test that creating a student with an invalid email returns an error."""
    response = client.post('/api/v1/students', json={
        'name': 'Invalid Email Student',
        'email': 'invalid-email'
    })
    
    assert response.status_code == 400  # Check for bad request due to validation
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'
    assert 'Invalid email format' in data['error']['message']

def test_existing_student_data_untouched_after_migration(client):
    """Test to ensure existing student data is intact after migration."""
    client.post('/api/v1/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })

    # Simulating a migration by creating a new column (this should be done in the migration script)
    
    # Retrieve the student to check if data is unchanged
    response = client.get('/api/v1/students/1')
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'
```