```python
import json
import pytest
from api import create_app, db
from api.models import Teacher  # Importing the Teacher model


@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()


def test_create_teacher_success(test_client):
    """Test the successful creation of a teacher."""
    response = test_client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data  # Check if teacher ID is returned


def test_create_teacher_missing_name(test_client):
    """Test error response for missing teacher name."""
    response = test_client.post('/teachers', json={
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Custom error code for validation
    assert data['error']['message'] == 'Name is required'


def test_create_teacher_invalid_email(test_client):
    """Test error response for invalid email format."""
    response = test_client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe'
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'  # Custom error code for invalid email
    assert data['error']['message'] == 'Invalid email format'


def test_get_teacher_by_id_success(test_client):
    """Test fetching a teacher by ID successfully."""
    # First, create a teacher to retrieve
    create_response = test_client.post('/teachers', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    teacher_id = json.loads(create_response.data)['id']
    
    response = test_client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == teacher_id
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'


def test_get_teacher_by_id_not_found(test_client):
    """Test error response for requesting a non-existent teacher."""
    response = test_client.get('/teachers/99999')  # Assuming 99999 is an invalid ID
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error']['code'] == 'E003'  # Custom error code for not found
    assert data['error']['message'] == 'Teacher not found'
```