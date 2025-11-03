```python
import json
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.teacher import Teacher  # Assuming Teacher model is defined in models.teacher

# Initialize the Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
db = SQLAlchemy(app)


@pytest.fixture
def client():
    """A test client for the Flask app."""
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after the tests


def test_add_new_teacher_succeeds(client):
    """Test successful addition of a new teacher."""
    new_teacher = {
        "name": "John Smith",
        "email": "john.smith@example.com"
    }
    response = client.post('/teachers', data=json.dumps(new_teacher), content_type='application/json')
    assert response.status_code == 201  # 201 Created
    data = json.loads(response.data)
    assert data['name'] == new_teacher['name']
    assert data['email'] == new_teacher['email']


def test_add_teacher_with_missing_name_fails(client):
    """Test adding a teacher with missing name fails."""
    new_teacher = {
        "email": "john.smith@example.com"
    }
    response = client.post('/teachers', data=json.dumps(new_teacher), content_type='application/json')
    assert response.status_code == 400  # 400 Bad Request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Custom error code for missing name
    assert "name is required" in data['error']['message']


def test_add_teacher_with_invalid_email_fails(client):
    """Test adding a teacher with an invalid email format fails."""
    new_teacher = {
        "name": "John Smith",
        "email": "invalid-email"
    }
    response = client.post('/teachers', data=json.dumps(new_teacher), content_type='application/json')
    assert response.status_code == 400  # 400 Bad Request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'  # Custom error code for invalid email
    assert "email must be a valid email address" in data['error']['message']


def test_retrieve_teacher_information_succeeds(client):
    """Test retrieving information of a teacher by ID."""
    new_teacher = {
        "name": "John Smith",
        "email": "john.smith@example.com"
    }
    # First, add the teacher to the database
    response = client.post('/teachers', data=json.dumps(new_teacher), content_type='application/json')
    teacher_data = json.loads(response.data)
    teacher_id = teacher_data['id']
    
    # Now, retrieve the teacher's information by ID
    response = client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200  # 200 OK
    data = json.loads(response.data)
    assert data['name'] == new_teacher['name']
    assert data['email'] == new_teacher['email']


def test_retrieve_non_existent_teacher_fails(client):
    """Test retrieving a non-existent teacher fails."""
    response = client.get('/teachers/99999')  # Assuming 99999 is an invalid ID
    assert response.status_code == 404  # 404 Not Found
    data = json.loads(response.data)
    assert data['error']['code'] == 'E003'  # Custom error code for not found
    assert "Teacher not found" in data['error']['message']
```