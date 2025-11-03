```python
# teacher_management/tests/test_api.py

import pytest
from flask import json
from teacher_management.app import app  # Import the Flask app
from teacher_management.models import Teacher  # Import the Teacher model

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_teacher(client):
    """Test creating a new teacher."""
    response = client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })

    # Assert that the response is 201 Created
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_get_teacher(client):
    """Test retrieving a teacher's information."""
    # First create a new teacher
    client.post('/teachers', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })

    # Now retrieve the teacher's information
    response = client.get('/teachers/1')

    # Assert that the response is 200 OK
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'

def test_update_teacher(client):
    """Test updating a teacher's information."""
    # First create a new teacher
    client.post('/teachers', json={
        'name': 'Jake Doe',
        'email': 'jake.doe@example.com'
    })

    # Update the teacher's information
    response = client.put('/teachers/1', json={
        'name': 'Jacob Doe',
        'email': 'jacob.doe@example.com'
    })

    # Assert that the response is 200 OK
    assert response.status_code == 200

    # Retrieve the updated teacher's information
    response = client.get('/teachers/1')
    data = json.loads(response.data)

    # Verify the updated information
    assert data['name'] == 'Jacob Doe'
    assert data['email'] == 'jacob.doe@example.com'
```