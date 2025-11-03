```python
import pytest
from flask import Flask, json
from your_application import create_app  # import your app factory function
from your_application.models import db, Student  # import db and Student model
from your_application.database import init_db  # import your database initialization function
from your_application.migrations import migrate_add_email_field  # import the migration function

@pytest.fixture
def app():
    """Create a Flask application for testing."""
    app = create_app('testing')  # create the app with the 'testing' configuration
    with app.app_context():
        init_db()  # Initialize the database.
        migrate_add_email_field()  # Apply the migration before tests run
        yield app  # Return the app for tests

@pytest.fixture
def client(app):
    """Create a test client for the application."""
    return app.test_client()

def test_create_student_with_email(client):
    """Test creating a student with a valid name and email."""
    response = client.post('/students', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201  # Check for successful creation
    data = json.loads(response.data)
    assert data['message'] == "Student created successfully."
    
    # Verify that the student has been added to the database
    student = Student.query.filter_by(email="john@example.com").first()
    assert student is not None
    assert student.name == "John Doe"

def test_retrieve_student_by_id(client):
    """Test retrieving student details by ID."""
    response = client.post('/students', json={"name": "Jane Doe", "email": "jane@example.com"})
    student_id = json.loads(response.data)['id']
    
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200  # Ensure successful retrieval
    data = json.loads(response.data)
    assert data['name'] == "Jane Doe"
    assert data['email'] == "jane@example.com"

def test_create_student_missing_email(client):
    """Test response when creating a student without an email."""
    response = client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 400  # Check for bad request
    data = json.loads(response.data)
    assert data['error']['code'] == "E001"
    assert data['error']['message'] == "Email field is required."

def test_display_all_students_with_emails(client):
    """Test retrieving all students including their emails."""
    response = client.get('/students')
    assert response.status_code == 200  # Ensure successful retrieval
    data = json.loads(response.data)
    
    # Check that data contains the expected structure
    assert isinstance(data, list)  # Response should be a list
    for student in data:
        assert 'name' in student
        assert 'email' in student  # Each student should have an email
```