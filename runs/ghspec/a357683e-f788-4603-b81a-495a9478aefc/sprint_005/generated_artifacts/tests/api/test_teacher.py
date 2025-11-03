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
            yield testing_client  # Directly use the testing client in test cases
            db.drop_all()  # Drop the database tables after testing

def test_create_teacher(test_client):
    """Test case for creating a new teacher with valid name and email."""
    response = test_client.post('/teachers', json={'name': 'Jane Smith', 'email': 'jane.smith@example.com'})
    assert response.status_code == 201  # Check for creation status
    assert response.json['name'] == 'Jane Smith'  # Verify name in response
    assert response.json['email'] == 'jane.smith@example.com'  # Verify email in response

def test_retrieve_teacher(test_client):
    """Test case for retrieving a teacher's information."""
    # Create a teacher to retrieve
    create_response = test_client.post('/teachers', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    teacher_id = create_response.json['id']  # Get the created teacher's ID

    response = test_client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200  # Check for successful retrieval
    assert response.json['name'] == 'John Doe'  # Verify name in response
    assert response.json['email'] == 'john.doe@example.com'  # Verify email in response

def test_create_teacher_duplicate_email(test_client):
    """Test case for handling duplicate teacher email."""
    # Create the first teacher
    test_client.post('/teachers', json={'name': 'Alice Johnson', 'email': 'alice.johnson@example.com'})

    # Attempt to create a second teacher with the same email
    response = test_client.post('/teachers', json={'name': 'Bob Brown', 'email': 'alice.johnson@example.com'})
    assert response.status_code == 400  # Check for error due to duplicate email
    assert response.json['error']['code'] == 'E001'  # Check for the correct error code
    assert 'already associated with another teacher' in response.json['error']['message']  # Confirm error message

def test_update_teacher_email(test_client):
    """Test case for updating an existing teacher's email."""
    # Create a teacher to update
    create_response = test_client.post('/teachers', json={'name': 'Charlie Green', 'email': 'charlie.green@example.com'})
    teacher_id = create_response.json['id']  # Get the created teacher's ID

    # Update the teacher's email
    update_response = test_client.put(f'/teachers/{teacher_id}', json={'email': 'charlie.new@example.com'})
    assert update_response.status_code == 200  # Check for successful update
    assert update_response.json['email'] == 'charlie.new@example.com'  # Verify updated email

    # Verify the update was successful in the database
    retrieve_response = test_client.get(f'/teachers/{teacher_id}')
    assert retrieve_response.json['email'] == 'charlie.new@example.com'  # Ensure the new email is reflected
```