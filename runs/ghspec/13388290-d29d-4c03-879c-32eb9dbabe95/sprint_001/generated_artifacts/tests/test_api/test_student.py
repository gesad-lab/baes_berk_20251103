import pytest
from app import create_app, db
from app.models import Student

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_create_student_with_valid_name(client):
    """Test successful creation of a student with a valid name."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201  # Expect a 201 Created status code
    assert 'student_id' in response.get_json()  # Validate that student ID is returned
    
def test_create_student_without_name(client):
    """Test creation of a student without a name should return an error."""
    response = client.post('/students', json={'name': ''})
    assert response.status_code == 400  # Expect a 400 Bad Request status code
    assert response.get_json() == {
        'error': {
            'code': 'E001',
            'message': 'Name is required.'
        }
    }

def test_retrieve_existing_student(client):
    """Test retrieval of an existing student using their ID."""
    response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = response.get_json()['student_id']

    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200  # Expect a 200 OK status code
    assert response.get_json()['name'] == 'Jane Doe'

def test_retrieve_non_existing_student(client):
    """Test retrieval of a non-existing student should return an error."""
    response = client.get('/students/9999')  # Assume this ID does not exist
    assert response.status_code == 404  # Expect a 404 Not Found status code
    assert response.get_json() == {
        'error': {
            'code': 'E002',
            'message': 'Student not found.'
        }
    }