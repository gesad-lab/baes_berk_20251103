import pytest
import json

from src.app import app  # Assuming `app` is where the Flask app is defined
from src.models.student import Student  # Assuming a Student model exists
from src.db.database import db  # Assuming a database instance is created

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the tables
            yield client
            db.drop_all()  # Cleanup

def test_create_student_with_email(client):
    """Test creating a student with valid name and email."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_retrieve_student_includes_email(client):
    """Test retrieving a student includes email in response."""
    student = Student(name='Jane Doe', email='jane.doe@example.com')
    db.session.add(student)
    db.session.commit()
    response = client.get(f'/students/{student.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'

def test_update_student_email(client):
    """Test updating a student's email."""
    student = Student(name='Mike Smith', email='mike.smith@example.com')
    db.session.add(student)
    db.session.commit()
    
    response = client.put(f'/students/{student.id}', json={'email': 'new.email@example.com'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['email'] == 'new.email@example.com'

def test_create_student_with_invalid_email(client):
    """Test creating a student with invalid email returns an error."""
    response = client.post('/students', json={'name': 'Invalid Email', 'email': 'invalid-email'})
    assert response.status_code == 400  # Bad Request
    error_data = response.get_json()
    assert 'error' in error_data
    assert error_data['error']['code'] == 'E001'  # Assuming this is the error code for invalid email

def test_create_student_without_email(client):
    """Test creating a student without email returns an error."""
    response = client.post('/students', json={'name': 'Missing Email'})
    assert response.status_code == 400  # Bad Request
    error_data = response.get_json()
    assert 'error' in error_data
    assert error_data['error']['code'] == 'E002'  # Assuming this is the error code for missing email field

def test_retrieve_nonexistent_student(client):
    """Test retrieving a non-existent student returns a 404."""
    response = client.get('/students/9999')
    assert response.status_code == 404  # Not Found
    error_data = response.get_json()
    assert 'error' in error_data
    assert error_data['error']['code'] == 'E003'  # Assuming this is the error code for not found
