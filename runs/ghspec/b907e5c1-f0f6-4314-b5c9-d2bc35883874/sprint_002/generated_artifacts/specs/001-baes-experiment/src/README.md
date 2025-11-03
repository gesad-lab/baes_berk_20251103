import pytest
from flask import json
from your_application import create_app  # import your app factory function
from your_application.models import db, Student  # import db and Student model
from your_application.database import init_db  # import your database initialization function

@pytest.fixture
def app():
    """Create a Flask application for testing."""
    app = create_app('testing')  # create the app with the 'testing' configuration
    with app.app_context():
        init_db()  # initialize the database
        yield app

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()

def test_create_student_with_email(client):
    """Test creating a student record with a valid name and email."""
    response = client.post('/students', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    assert response.status_code == 201  # Expecting a 201 Created response
    data = response.get_json()
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_student_without_email(client):
    """Test creating a student record without an email."""
    response = client.post('/students', json={
        'name': 'Jane Doe'
    })
    
    assert response.status_code == 400  # Expecting a 400 Bad Request response
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Check for specific error code
    assert data['error']['message'] == 'Email is required.'  # Check for correct error message

def test_retrieve_student(client):
    """Test retrieving a student by ID, verifying response includes email."""
    # First, create a student to retrieve
    create_response = client.post('/students', json={
        'name': 'Alice Smith',
        'email': 'alice.smith@example.com'
    })
    student_id = create_response.get_json()['id']  # Get the ID of the created student
    
    response = client.get(f'/students/{student_id}')
    
    assert response.status_code == 200  # Expecting a 200 OK response
    data = response.get_json()
    assert data['id'] == student_id
    assert data['name'] == 'Alice Smith'
    assert data['email'] == 'alice.smith@example.com'

def test_list_students(client):
    """Test listing all students, verifying email is included in the response."""
    client.post('/students', json={
        'name': 'Bob Brown',
        'email': 'bob.brown@example.com'
    })
    client.post('/students', json={
        'name': 'Carol White',
        'email': 'carol.white@example.com'
    })
    
    response = client.get('/students')
    
    assert response.status_code == 200  # Expecting a 200 OK response
    data = response.get_json()
    assert len(data) >= 2  # Ensure at least two records are returned
    assert all('email' in student for student in data)  # Check that each student has an email field