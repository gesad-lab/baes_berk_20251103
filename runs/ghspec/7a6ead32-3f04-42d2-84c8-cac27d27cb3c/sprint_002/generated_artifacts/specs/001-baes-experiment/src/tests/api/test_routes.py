```python
import json
import pytest
from flask import Flask
from your_application import create_app, db, Student

# Instantiate the Flask app for testing
app = create_app()

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
    with app.app_context():
        db.drop_all()  # Cleanup after tests

def test_create_student_with_valid_email(client):
    """Test that creating a student with a valid email returns 201 Created."""
    response = client.post('/api/v1/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    json_data = response.get_json()
    assert 'id' in json_data
    assert json_data['name'] == "John Doe"
    assert json_data['email'] == "john.doe@example.com"


def test_create_student_with_invalid_email(client):
    """Test that creating a student with an invalid email returns 400 Bad Request."""
    response = client.post('/api/v1/students', json={
        "name": "John Doe",
        "email": "invalid-email"
    })
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error']['code'] == "E002"
    assert json_data['error']['message'] == "Email format is invalid."


def test_update_student_with_valid_email(client):
    """Test updating a student's email with valid format returns 200 OK."""
    # First, create a student to update
    create_response = client.post('/api/v1/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    student_id = create_response.get_json()['id']

    update_response = client.put(f'/api/v1/students/{student_id}', json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    })
    assert update_response.status_code == 200
    json_data = update_response.get_json()
    assert json_data['name'] == "Jane Doe"
    assert json_data['email'] == "jane.doe@example.com"


def test_update_student_with_invalid_email(client):
    """Test updating a student's email with an invalid format returns 400 Bad Request."""
    # First, create a student to update
    create_response = client.post('/api/v1/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    student_id = create_response.get_json()['id']

    update_response = client.put(f'/api/v1/students/{student_id}', json={
        "name": "Jane Doe",
        "email": "invalid-email"
    })
    assert update_response.status_code == 400
    json_data = update_response.get_json()
    assert json_data['error']['code'] == "E002"
    assert json_data['error']['message'] == "Email format is invalid."


def test_retrieve_student_with_email(client):
    """Test retrieving a student shows the email field correctly."""
    # First, create a student
    create_response = client.post('/api/v1/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    student_id = create_response.get_json()['id']

    retrieve_response = client.get(f'/api/v1/students/{student_id}')
    assert retrieve_response.status_code == 200
    json_data = retrieve_response.get_json()
    assert json_data['id'] == student_id
    assert json_data['email'] == "john.doe@example.com"
```