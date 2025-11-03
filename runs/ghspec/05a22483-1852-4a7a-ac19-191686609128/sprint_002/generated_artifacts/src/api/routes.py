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
            db.drop_all()  # ensure database is clean after tests


def test_create_student_with_email(client):
    """Test creating a student with valid name and email."""
    response = client.post('/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'


def test_create_student_without_email(client):
    """Test error when trying to create a student without an email."""
    response = client.post('/students', json={
        'name': 'John Doe'
    })
    assert response.status_code == 400  # Expecting validation error
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Check for specific error code
    assert data['error']['message'] == 'Email is required'


def test_retrieve_student_with_email(client):
    """Test retrieving a student's details by ID."""
    # First, create a student
    response = client.post('/students', json={
        'name': 'Alice Smith',
        'email': 'alice.smith@example.com'
    })
    student_id = response.get_json()['id']

    # Now retrieve the student
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == student_id
    assert data['name'] == 'Alice Smith'
    assert data['email'] == 'alice.smith@example.com'

```