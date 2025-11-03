import json
import pytest
from api import create_app, db
from api.models import Student

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()  # Create the test client
        db.drop_all()  # Drop the database after tests


def test_create_student(test_client):
    """Test creating a new student with valid data."""
    student_data = {
        "name": "John Doe",
        "age": 20
    }
    response = test_client.post('/api/v1/students', json=student_data)
    
    assert response.status_code == 201
    assert response.json['message'] == "Student created successfully"
    
    # Check if the student is persisted in the database
    student = Student.query.filter_by(name="John Doe").first()
    assert student is not None
    assert student.age == 20


def test_create_student_missing_name(test_client):
    """Test creating a student with missing name should return error."""
    student_data = {
        "age": 20
    }
    response = test_client.post('/api/v1/students', json=student_data)

    assert response.status_code == 400
    assert response.json['error']['message'] == "Name is required"


def test_get_student(test_client):
    """Test retrieving a student that exists in the database."""
    student_data = {
        "name": "Jane Doe",
        "age": 22
    }
    test_client.post('/api/v1/students', json=student_data)  # Create the student first
    
    response = test_client.get('/api/v1/students/1')  # Get the student by ID

    assert response.status_code == 200
    assert response.json['name'] == "Jane Doe"
    assert response.json['age'] == 22


def test_get_student_not_found(test_client):
    """Test retrieving a student that does not exist."""
    response = test_client.get('/api/v1/students/999')  # Non-existent ID

    assert response.status_code == 404
    assert response.json['error']['message'] == "Student not found"


def test_delete_student(test_client):
    """Test deleting an existing student."""
    student_data = {
        "name": "Mark Smith",
        "age": 19
    }
    test_client.post('/api/v1/students', json=student_data)  # Create the student first
    
    response = test_client.delete('/api/v1/students/1')  # Delete the student by ID

    assert response.status_code == 200
    assert response.json['message'] == "Student deleted successfully"
    
    # Check if the student is removed from the database
    student = Student.query.filter_by(name="Mark Smith").first()
    assert student is None


def test_delete_student_not_found(test_client):
    """Test deleting a student that does not exist should return error."""
    response = test_client.delete('/api/v1/students/999')  # Non-existent ID
    
    assert response.status_code == 404
    assert response.json['error']['message'] == "Student not found"