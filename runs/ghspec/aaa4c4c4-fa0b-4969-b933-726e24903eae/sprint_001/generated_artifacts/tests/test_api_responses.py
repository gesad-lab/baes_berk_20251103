import pytest
import json
from app import app, db, Student

@pytest.fixture(scope='module')
def test_client():
    """Setup the test client for the Flask application."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()  # Create database schema
    yield app.test_client()
    with app.app_context():
        db.drop_all()  # Clean up the database after tests

def test_create_student_success(test_client):
    """Test creating a student record successfully."""
    response = test_client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data
    assert data['name'] == 'John Doe'
    assert data['message'] == 'Student created successfully.'

def test_create_student_without_name(test_client):
    """Test creating a student record without a name."""
    response = test_client.post('/students', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error'] == 'Name is required.'

def test_get_all_students_empty(test_client):
    """Test retrieving all students when no records exist."""
    response = test_client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == []  # Expecting an empty array

def test_create_multiple_students(test_client):
    """Test creating multiple student records."""
    test_client.post('/students', json={'name': 'John Doe'})
    test_client.post('/students', json={'name': 'Jane Doe'})

    response = test_client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    assert data[0]['name'] == 'John Doe'
    assert data[1]['name'] == 'Jane Doe'