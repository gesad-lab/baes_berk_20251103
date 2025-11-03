import pytest
from app import create_app, db
from models.student import Student

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')  # Initialize app with testing configuration
    testing_client = app.test_client()

    # Establish an application context
    with app.app_context():
        # Create the database and the database table(s)
        db.create_all()

        yield testing_client  # This is where the testing happens!

        # Teardown the database after tests
        db.drop_all()

def test_add_student(test_client):
    """Test adding a new student successfully."""
    response = test_client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert b'John Doe' in response.data

def test_add_student_missing_name(test_client):
    """Test adding a student with missing name."""
    response = test_client.post('/students', json={'name': ''})
    assert response.status_code == 400
    assert b'Invalid input: name is required.' in response.data

def test_retrieve_student(test_client):
    """Test retrieving an existing student."""
    response = test_client.post('/students', json={'name': 'Jane Doe'})
    assert response.status_code == 201

    response = test_client.get('/students/1')  # Assuming '1' is the ID of the student added
    assert response.status_code == 200
    assert b'Jane Doe' in response.data

def test_retrieve_non_existent_student(test_client):
    """Test retrieving a non-existent student."""
    response = test_client.get('/students/999')  # ID that does not exist
    assert response.status_code == 404
    assert b'Student not found.' in response.data

def test_list_students(test_client):
    """Test listing all students."""
    response = test_client.get('/students')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Check if the response is a list

# Ensure to run this test suite with: pytest tests/test_student.py