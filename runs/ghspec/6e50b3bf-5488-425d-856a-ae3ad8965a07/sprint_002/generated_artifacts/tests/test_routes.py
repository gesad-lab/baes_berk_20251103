```python
import pytest
from flask import Flask, json
from src.routes import app, db
from src.models import Student

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create all tables for the test
        yield client
        with app.app_context():
            db.drop_all()  # clean up after the test


def test_create_student_with_email(client):
    """Test creating a student with a name and email."""
    response = client.post('/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"


def test_create_student_without_email(client):
    """Test error response when trying to create a student without an email."""
    response = client.post('/students', json={
        "name": "John Doe",
        "email": ""
    })
    assert response.status_code == 400
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E001'
    assert error_data['error']['message'] == 'Email field is required.'


def test_retrieve_student(client):
    """Test retrieving a student by ID."""
    # First, create a student
    response_create = client.post('/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    student_id = json.loads(response_create.data)["id"]

    # Now, retrieve the student by ID
    response_retrieve = client.get(f'/students/{student_id}')
    assert response_retrieve.status_code == 200
    data = json.loads(response_retrieve.data)
    assert data['id'] == student_id
    assert data['name'] == "John Doe"
    assert data['email'] == "john.doe@example.com"


def test_retrieve_non_existent_student(client):
    """Test retrieving a student that does not exist."""
    response = client.get('/students/999999')  # Assuming this ID does not exist
    assert response.status_code == 404
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E002'
    assert error_data['error']['message'] == 'Student not found.'
```