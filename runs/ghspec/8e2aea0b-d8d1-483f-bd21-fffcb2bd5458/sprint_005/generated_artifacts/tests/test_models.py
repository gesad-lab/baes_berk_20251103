```python
import json
import pytest
from flask import Flask
from flask.testing import FlaskClient
from src.app import create_app  # Function to create the Flask app
from src.models import db, Teacher  # Importing the Teacher model

@pytest.fixture
def client() -> FlaskClient:
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            # Create the database and add test data
            db.create_all()
            # Insert test data if necessary; this can include a teacher

            yield client  # Allows the tests to run with the client

            db.drop_all()  # Clean up after tests


def test_view_teacher_information_with_valid_id(client: FlaskClient):
    """Test retrieval of teacher information for a valid ID."""
    # Creating a new teacher to test retrieval
    response = client.post('/teachers', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    data = response.get_json()
    teacher_id = data['teacher_id']

    # Now, retrieve the teacher information by ID
    response = client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200
    teacher_data = response.get_json()
    assert teacher_data['name'] == "John Doe"
    assert teacher_data['email'] == "john.doe@example.com"


def test_view_teacher_information_with_invalid_id(client: FlaskClient):
    """Test retrieval of teacher information for an invalid ID."""
    response = client.get('/teachers/9999')  # Assuming 9999 does not exist
    assert response.status_code == 404
    error_data = response.get_json()
    assert error_data['error']['code'] == "E002"  # Assuming E002 is the error code for "Not Found"
    assert error_data['error']['message'] == "Teacher not found."
```