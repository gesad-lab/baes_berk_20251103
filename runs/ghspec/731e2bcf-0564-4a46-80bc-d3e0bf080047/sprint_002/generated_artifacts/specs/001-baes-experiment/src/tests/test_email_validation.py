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
    """Fixture for testing the Flask application."""
    return app.test_client()

def test_create_student_with_valid_email(client):
    """Test case for creating a student with valid name and email."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201
    response_data = json.loads(response.data)
    assert response_data['name'] == 'John Doe'
    assert response_data['email'] == 'john.doe@example.com'

def test_create_student_with_empty_name(client):
    """Test case for creating a student with an empty name."""
    response = client.post('/students', json={'name': '', 'email': 'john.doe@example.com'})
    assert response.status_code == 400  # Assuming a 400 error for bad request
    assert 'name is required' in response.get_data(as_text=True)

def test_create_student_with_empty_email(client):
    """Test case for creating a student with an empty email."""
    response = client.post('/students', json={'name': 'John Doe', 'email': ''})
    assert response.status_code == 400  # Assuming a 400 error for bad request
    assert 'email is required' in response.get_data(as_text=True)

def test_create_student_with_invalid_email_format(client):
    """Test case for creating a student with an invalid email format."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@com'})
    assert response.status_code == 400  # Assuming a 400 error for bad request
    assert 'email is not valid' in response.get_data(as_text=True)

def test_retrieve_students_with_email(client):
    """Test case for retrieving student records."""
    # First, create a student to ensure the database is populated
    client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    
    response = client.get('/students')
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert len(response_data) == 1
    assert response_data[0]['name'] == 'John Doe'
    assert response_data[0]['email'] == 'john.doe@example.com'

def test_retrieve_students_empty_list(client):
    """Test case for retrieving students when the database is empty."""
    response = client.get('/students')
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data == []
```