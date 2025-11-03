import json
import time
import pytest
from app import app, db
from models import Student

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables
        yield client
        db.drop_all()  # Cleanup after each test

def test_create_student_response_time(client):
    """Test that creating a student responds within 2 seconds."""
    start_time = time.time()
    response = client.post('/students', json={'name': 'John Doe'})
    end_time = time.time()

    assert response.status_code == 201  # Check for successful creation
    assert end_time - start_time < 2  # Validate response time is under 2 seconds

def test_retrieve_students_response_time(client):
    """Test that retrieving students responds within 2 seconds."""
    # Create a sample student to ensure there's data to retrieve
    client.post('/students', json={'name': 'John Doe'})

    start_time = time.time()
    response = client.get('/students')
    end_time = time.time()

    assert response.status_code == 200  # Check for successful retrieval
    assert isinstance(response.json, list)  # Validate response is a list
    assert end_time - start_time < 2  # Validate response time is under 2 seconds

def test_create_student_with_empty_name(client):
    """Test that creating a student with an empty name returns an error."""
    response = client.post('/students', json={'name': ''})

    assert response.status_code == 400  # Check for bad request
    assert response.json['error']['message'] == 'Name is required'  # Validate error message

def test_retrieve_students_empty(client):
    """Test retrieving students when no students have been created."""
    response = client.get('/students')

    assert response.status_code == 200  # Check retrieval is successful
    assert response.json == []  # Validate that the list of students is empty