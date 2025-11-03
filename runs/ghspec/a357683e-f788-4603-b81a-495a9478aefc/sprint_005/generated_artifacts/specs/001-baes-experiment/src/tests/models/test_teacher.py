```python
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
            yield testing_client  # Provide the test client to the test functions
            db.drop_all()  # Cleanup after tests

def test_create_teacher_success(test_client):
    """Test successful creation of a teacher with a unique email."""
    response = test_client.post('/teachers', json={'name': 'Alice Smith', 'email': 'alice@example.com'})
    assert response.status_code == 201  # Check for 201 Created
    json_data = json.loads(response.data)
    assert json_data['name'] == 'Alice Smith'
    assert json_data['email'] == 'alice@example.com'

def test_create_teacher_duplicate_email(test_client):
    """Test error handling when creating a teacher with a duplicate email."""
    # First, create a teacher
    test_client.post('/teachers', json={'name': 'Alice Smith', 'email': 'alice@example.com'})
    
    # Attempt to create another teacher with the same email
    response = test_client.post('/teachers', json={'name': 'Bob Johnson', 'email': 'alice@example.com'})
    
    assert response.status_code == 400  # Check for 400 Bad Request
    json_data = json.loads(response.data)
    assert json_data['error']['code'] == 'E002'  # Check for specific error code for duplicate email
    assert 'email is already associated with another teacher' in json_data['error']['message']

def test_retrieve_teacher(test_client):
    """Test retrieving a teacher's information."""
    response = test_client.get('/teachers/1')  # Assume teacher ID is 1
    assert response.status_code == 200  # Check for 200 OK
    json_data = json.loads(response.data)
    assert json_data['name'] == 'Alice Smith'  # Verify teacher's name

def test_update_teacher_email(test_client):
    """Test updating a teacher's email."""
    response = test_client.put('/teachers/1', json={'email': 'newalice@example.com'})  # Assume teacher ID is 1
    assert response.status_code == 200  # Check for 200 OK
    json_data = json.loads(response.data)
    assert json_data['email'] == 'newalice@example.com'  # Verify updated email
```