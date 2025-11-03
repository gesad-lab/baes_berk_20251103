```python
import pytest
from flask import json
from app import create_app, db  # Assuming create_app sets up the Flask app and db is the SQLAlchemy instance
from app.models import Student  # Assuming the Student model is defined in models.py

@pytest.fixture
def client():
    app = create_app({'TESTING': True})  # Create a test instance of the application
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client

def test_create_student_success(client):
    """Test successful creation of a new student."""
    response = client.post('/students', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    assert response.status_code == 201  # Check for successful creation
    data = json.loads(response.data)
    assert 'id' in data  # Check that the response includes student ID
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_student_missing_name(client):
    """Test creation of student fails when name is missing."""
    response = client.post('/students', json={
        'email': 'john.doe@example.com'
    })
    
    assert response.status_code == 400  # Check for bad request
    data = json.loads(response.data)
    assert data == {"error": {"code": "E001", "message": "Name is required."}}

def test_create_student_missing_email(client):
    """Test creation of student fails when email is missing."""
    response = client.post('/students', json={
        'name': 'John Doe'
    })
    
    assert response.status_code == 400  # Check for bad request
    data = json.loads(response.data)
    assert data == {"error": {"code": "E001", "message": "Email is required."}}

def test_get_all_students_empty(client):
    """Test retrieval of all students returns an empty list when no students exist."""
    response = client.get('/students')
    
    assert response.status_code == 200  # Check for successful retrieval
    data = json.loads(response.data)
    assert data == []  # Should return an empty array

def test_get_all_students_with_data(client):
    """Test retrieval of students returns the correct records after creation."""
    client.post('/students', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    client.post('/students', json={
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com'
    })

    response = client.get('/students')
    
    assert response.status_code == 200  # Check for successful retrieval
    data = json.loads(response.data)
    assert len(data) == 2  # Two students should be returned
    assert data[0]['name'] == 'John Doe'
    assert data[0]['email'] == 'john.doe@example.com'
    assert data[1]['name'] == 'Jane Smith'
    assert data[1]['email'] == 'jane.smith@example.com'
```