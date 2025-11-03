```python
import pytest
from flask import json
from app import create_app, db
from models import Student, Course, Teacher  # Importing the Teacher model
from teacher_service import create_teacher_service  # Assuming service layer exists

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

@pytest.fixture(scope='function')
def initialized_database():
    # Create a new teacher entry for testing purposes
    with db.session.begin():
        teacher = Teacher(name="John Doe", email="john.doe@example.com")
        db.session.add(teacher)
    db.session.commit()

def test_create_teacher(test_client):
    """Test the teacher creation endpoint."""
    response = test_client.post('/teachers',
                                 data=json.dumps({'name': 'Jane Doe', 'email': 'jane.doe@example.com'}),
                                 content_type='application/json')
    
    assert response.status_code == 201  # Check the response status code
    data = json.loads(response.data)
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'

def test_create_teacher_with_duplicate_email(test_client, initialized_database):
    """Test creating a teacher with a duplicate email."""
    response = test_client.post('/teachers',
                                 data=json.dumps({'name': 'John Smith', 'email': 'john.doe@example.com'}),
                                 content_type='application/json')
    
    assert response.status_code == 400  # Expecting bad request for duplicate email
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'  # Assuming error code for duplicate email
    assert 'Email already exists' in data['error']['message']

def test_get_teacher(test_client, initialized_database):
    """Test the retrieval of a specific teacher."""
    response = test_client.get('/teachers/1')  # Assuming ID is 1 for the created teacher

    assert response.status_code == 200  # Should be successful
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_get_nonexistent_teacher(test_client):
    """Test retrieving a teacher that does not exist."""
    response = test_client.get('/teachers/9999')  # ID that does not exist

    assert response.status_code == 404  # Expecting not found
    data = json.loads(response.data)
    assert data['error']['code'] == 'E003'  # Assuming error code for not found
    assert 'Teacher not found' in data['error']['message']
```