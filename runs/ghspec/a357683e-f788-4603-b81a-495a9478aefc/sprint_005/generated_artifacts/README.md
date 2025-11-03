```python
# File: tests/api/test_teacher.py

import pytest
from flask import json
from app import create_app, db
from app.models import Teacher

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Create the database tables
            yield testing_client  # Provide the test client to test functions
            db.drop_all()  # Clean up after tests

def test_create_teacher(test_client):
    """Test creating a new teacher with valid data."""
    response = test_client.post('/api/v1/teachers', 
                                 data=json.dumps({'name': 'Jane Smith', 'email': 'jane.smith@example.com'}),
                                 content_type='application/json')
    
    assert response.status_code == 201  # Assert teacher is created successfully
    data = json.loads(response.data)
    assert data['name'] == 'Jane Smith'
    assert data['email'] == 'jane.smith@example.com'

def test_retrieve_teacher(test_client):
    """Test retrieving teacher information."""
    # Assuming the Teacher was created in the previous test
    response = test_client.get('/api/v1/teachers/1')  # Adjust ID based on your data
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Jane Smith'
    assert data['email'] == 'jane.smith@example.com'

def test_create_teacher_with_duplicate_email(test_client):
    """Test attempting to create a teacher with an already existing email."""
    response = test_client.post('/api/v1/teachers', 
                                 data=json.dumps({'name': 'John Doe', 'email': 'jane.smith@example.com'}),
                                 content_type='application/json')
    
    assert response.status_code == 400  # Assert error is returned for duplicate email
    data = json.loads(response.data)
    assert data['error']['message'] == "Email address is already in use."

def test_update_teacher(test_client):
    """Test updating an existing teacher's information."""
    response = test_client.put('/api/v1/teachers/1',  # Assuming ID 1 for the test
                                data=json.dumps({'name': 'Jane Smith', 'email': 'jane.new@example.com'}),
                                content_type='application/json')
    
    assert response.status_code == 200  # Assert update is successful
    data = json.loads(response.data)
    
    assert data['email'] == 'jane.new@example.com'  # Check if the email was updated
    
    # Check if the updated teacher can still be retrieved
    retrieval_response = test_client.get('/api/v1/teachers/1')
    assert retrieval_response.status_code == 200
    retrieval_data = json.loads(retrieval_response.data)
    assert retrieval_data['email'] == 'jane.new@example.com'  # Verify the updated email
```