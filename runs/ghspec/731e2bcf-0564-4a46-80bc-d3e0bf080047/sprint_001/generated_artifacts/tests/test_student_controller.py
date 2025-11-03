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
    """Fixture for the test client to simulate HTTP requests."""
    return app.test_client()

def test_create_student(client):
    """Test the creation of a new student."""
    response = client.post('/students', 
                            json={'name': 'John Doe'},
                            content_type='application/json')
    
    assert response.status_code == 201  # Check if creation is successful
    data = json.loads(response.data)
    assert 'id' in data  # Check if an ID is returned
    assert data['name'] == 'John Doe'  # Check if the name matches

def test_get_students(client):
    """Test retrieving all students."""
    # First, create a student to ensure the list is not empty
    client.post('/students', json={'name': 'Jane Doe'}, content_type='application/json')

    response = client.get('/students')
    
    assert response.status_code == 200  # Check if retrieval is successful
    data = json.loads(response.data)
    assert isinstance(data, list)  # Check that the response is a list
    assert len(data) > 0  # Check that the list is not empty
    assert data[0]['name'] == 'Jane Doe'  # Verify the name of the created student

def test_create_student_invalid(client):
    """Test creating a student without a name."""
    response = client.post('/students', 
                            json={},  # No name provided
                            content_type='application/json')
    
    assert response.status_code == 400  # Check for bad request
    data = json.loads(response.data)
    assert 'error' in data  # Check if error key is in the response
    assert data['error']['code'] == 'E001'  # Check if error code matches
    assert data['error']['message'] == 'Name is required'  # Verify the error message

def test_get_students_empty(client):
    """Test retrieving students when none exist."""
    response = client.get('/students')
    
    assert response.status_code == 200  # Check retrieval's success
    data = json.loads(response.data)
    assert data == []  # Expect an empty list when no students

