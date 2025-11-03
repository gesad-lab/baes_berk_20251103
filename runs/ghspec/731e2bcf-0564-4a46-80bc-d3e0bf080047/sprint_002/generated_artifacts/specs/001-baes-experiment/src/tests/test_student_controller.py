```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.student import Student

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})
    
    with app.app_context():
        # Create the database and tables
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture for the test client."""
    return app.test_client()

def test_create_student_with_valid_email(client):
    """Test creating a student with a valid email."""
    response = client.post('/students', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })

    assert response.status_code == 201  # Check for 201 status code
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_student_with_invalid_email(client):
    """Test creating a student with an invalid email format."""
    response = client.post('/students', json={
        'name': 'John Doe',
        'email': 'invalid-email-format'
    })

    assert response.status_code == 400  # Check for 400 status code
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Check for specific error code
    assert data['error']['message'] == 'Invalid email format'  # Check error message

def test_create_student_without_email(client):
    """Test creating a student without providing an email."""
    response = client.post('/students', json={
        'name': 'Jane Doe'
        # Missing email field
    })

    assert response.status_code == 400  # Check for 400 status code
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'  # Check for specific error code
    assert data['error']['message'] == 'Email is required'  # Check error message

def test_get_students_list(client):
    """Test retrieving the list of students with their emails."""
    client.post('/students', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    client.post('/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })

    response = client.get('/students')
    assert response.status_code == 200  # Check for 200 status code
    data = json.loads(response.data)
    assert len(data) == 2  # Check that two students are returned
    assert any(student['email'] == 'john.doe@example.com' for student in data)
    assert any(student['email'] == 'jane.doe@example.com' for student in data)

def test_get_students_empty_list(client):
    """Test retrieving the list of students when no students exist."""
    response = client.get('/students')
    assert response.status_code == 200  # Check for 200 status code
    data = json.loads(response.data)
    assert data == []  # Check that the list is empty
```