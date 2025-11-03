```python
import pytest
from flask import Flask, jsonify, request
from your_app import create_app, db  # make sure to replace with actual import paths
from your_app.models import Student  # update with actual model import


@pytest.fixture
def client():
    app = create_app('testing')  # use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create the database schema
        yield client
        with app.app_context():
            db.drop_all()  # drop the database schema after tests

# Test for creating a student with an email
def test_create_student_with_email(client):
    """Test creating a student with an email."""
    response = client.post('/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com',  # New email field
    })
    assert response.status_code == 201  # Check that creation was successful
    json_data = response.get_json()
    assert json_data['name'] == 'Jane Doe'
    assert json_data['email'] == 'jane.doe@example.com'  # Validate the email is returned correctly

# Test for retrieving a student with email
def test_get_student_with_email(client):
    """Test retrieving a student with email."""
    # First, create a student
    client.post('/students', json={
        'name': 'John Smith',
        'email': 'john.smith@example.com',  # New email field
    })

    # Now retrieve the student
    response = client.get('/students/1')  # Assuming the student ID is 1
    assert response.status_code == 200  # Check that retrieval was successful
    json_data = response.get_json()
    assert json_data['name'] == 'John Smith'
    assert json_data['email'] == 'john.smith@example.com'  # Validate the email is returned correctly
```