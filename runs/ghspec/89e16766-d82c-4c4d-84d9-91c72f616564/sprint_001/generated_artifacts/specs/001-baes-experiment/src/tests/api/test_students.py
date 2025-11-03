import pytest
from flask import json
from app import create_app, db
from app.models import Student

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    
    # Create a test client using the Flask application configured for testing
    with app.test_client() as client:
        with app.app_context():
            # Create all tables in the database
            db.create_all()
            yield client
            # Cleanup after tests
            db.drop_all()

def test_create_student_valid(test_client):
    """Test creating a student with valid input"""
    response = test_client.post('/api/students', 
                                 data=json.dumps({'name': 'John Doe', 'age': 20}),
                                 content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'Student created successfully'
    assert 'id' in data  # Check if the student ID is returned

def test_create_student_invalid(test_client):
    """Test creating a student with invalid input"""
    response = test_client.post('/api/students', 
                                 data=json.dumps({'name': '', 'age': 'not_a_number'}),
                                 content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Example error code for validation issue
    assert 'Invalid input' in data['error']['message']

def test_get_student(test_client):
    """Test retrieving an existing student"""
    # First, we create a student to retrieve
    create_response = test_client.post('/api/students', 
                                        data=json.dumps({'name': 'Jane Doe', 'age': 22}),
                                        content_type='application/json')
    student_id = json.loads(create_response.data)['id']
    
    # Now, we attempt to retrieve that student
    response = test_client.get(f'/api/students/{student_id}')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'
    assert data['age'] == 22

def test_get_student_not_found(test_client):
    """Test retrieving a non-existent student"""
    response = test_client.get('/api/students/99999')  # Assuming 99999 doesn't exist
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'  # Example error code for not found
    assert 'Student not found' in data['error']['message']