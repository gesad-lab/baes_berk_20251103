import pytest
from src.app import app  # Assuming the Flask app is defined in app.py
from src.models import db, Student  # Assuming SQLAlchemy is set up in models.py

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for tests
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_create_student_with_email_succeeds(client):
    """Test creating a new student with a valid name and email."""
    response = client.post('/students', json={
        'name': 'Test Student',
        'email': 'test@student.com'
    })
    
    # Assert that the response is successful and contains the expected data
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['name'] == 'Test Student'
    assert data['email'] == 'test@student.com'

def test_get_all_students_includes_email(client):
    """Test retrieving all students includes their emails."""
    # First, create a couple of students
    client.post('/students', json={
        'name': 'Test Student 1',
        'email': 'test1@student.com'
    })
    client.post('/students', json={
        'name': 'Test Student 2',
        'email': 'test2@student.com'
    })
    
    # Now retrieve all students
    response = client.get('/students')
    
    # Assert that the response is successful and contains the expected data
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # The response should be a list
    assert len(data) == 2  # We created 2 students
    assert all('email' in student for student in data)  # Check that 'email' field exists

    # Check if the correct emails are returned
    assert data[0]['email'] == 'test1@student.com'
    assert data[1]['email'] == 'test2@student.com'