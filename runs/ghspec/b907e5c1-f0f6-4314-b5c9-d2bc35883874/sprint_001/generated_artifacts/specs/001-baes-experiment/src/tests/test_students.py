import pytest
from flask import Flask, json
from your_application import create_app  # import your app factory function
from your_application.models import db, Student  # import db and Student model
from your_application.database import init_db  # import your database initialization function

@pytest.fixture
def app():
    """Create a Flask application for testing."""
    app = create_app('testing')  # create the app with the 'testing' configuration
    with app.app_context():
        init_db()  # initialize the database
        yield app  # provide the test client

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

def test_create_student(client):
    """Test the endpoint for creating a student."""
    response = client.post('/students', json={
        'name': 'John Doe',
        'age': 20,
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['student']['name'] == 'John Doe'

def test_create_student_missing_fields(client):
    """Test creating a student with missing required fields."""
    response = client.post('/students', json={
        'name': '',
        'age': 20,
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'
    assert 'name is required' in data['error']['message']

def test_get_student(client):
    """Test retrieving a student by ID."""
    # First create a student to retrieve
    create_response = client.post('/students', json={
        'name': 'Jane Doe',
        'age': 22,
        'email': 'jane.doe@example.com'
    })
    student_id = json.loads(create_response.data)['student']['id']

    # Now retrieve the student
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['student']['id'] == student_id

def test_get_student_not_found(client):
    """Test retrieving a student that does not exist."""
    response = client.get('/students/999')  # Assuming this ID does not exist
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'
    assert 'Student not found' in data['error']['message'] 

def test_list_students(client):
    """Test listing all students."""
    client.post('/students', json={
        'name': 'Alice',
        'age': 21,
        'email': 'alice@example.com'
    })
    client.post('/students', json={
        'name': 'Bob',
        'age': 23,
        'email': 'bob@example.com'
    })
    
    response = client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['students']) >= 2  # We expect at least 2 students

def test_list_students_empty(client):
    """Test listing students when no students are present."""
    response = client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['students']) == 0  # Should be empty if no students are created