```python
import json
import pytest
from api import create_app, db
from api.models import Teacher  # Assuming the Teacher model is defined in models.py

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()  # Provide the test client to the tests

def test_create_teacher_missing_name(test_client):
    """Test creating a teacher without a name results in validation error."""
    response = test_client.post('/teachers', json={'email': 'teacher@example.com'})
    assert response.status_code == 400  # Bad Request
    assert response.json == {
        'error': {
            'code': 'E001',
            'message': 'Missing required fields: name',
            'details': {}
        }
    }

def test_create_teacher_missing_email(test_client):
    """Test creating a teacher without an email results in validation error."""
    response = test_client.post('/teachers', json={'name': 'John Doe'})
    assert response.status_code == 400  # Bad Request
    assert response.json == {
        'error': {
            'code': 'E002',
            'message': 'Missing required fields: email',
            'details': {}
        }
    }

def test_create_teacher_invalid_email_format(test_client):
    """Test creating a teacher with an invalid email format results in validation error."""
    response = test_client.post('/teachers', json={'name': 'John Doe', 'email': 'invalid-email'})
    assert response.status_code == 400  # Bad Request
    assert response.json == {
        'error': {
            'code': 'E003',
            'message': 'Invalid email format',
            'details': {}
        }
    }

def test_update_teacher_missing_fields(test_client):
    """Test updating a teacher without required fields results in validation error."""
    response = test_client.put('/teachers/1', json={})  # No fields to update
    assert response.status_code == 400  # Bad Request
    assert response.json == {
        'error': {
            'code': 'E001',
            'message': 'Missing required fields: name or email',
            'details': {}
        }
    }

def test_update_teacher_invalid_email_format(test_client):
    """Test updating a teacher with an invalid email format results in validation error."""
    response = test_client.put('/teachers/1', json={'name': 'Updated Name', 'email': 'invalid-email'})
    assert response.status_code == 400  # Bad Request
    assert response.json == {
        'error': {
            'code': 'E003',
            'message': 'Invalid email format',
            'details': {}
        }
    }
```