```python
import json
import pytest
from app import app, db, Student

# Fixture to set up the test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_add_student_with_valid_name(client):
    """Test adding a student with a valid name"""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201  # Created
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'

def test_retrieve_all_students(client):
    """Test retrieving all students"""
    client.post('/students', json={'name': 'John Doe'})
    client.post('/students', json={'name': 'Jane Smith'})
    response = client.get('/students')
    assert response.status_code == 200  # OK
    data = json.loads(response.data)
    assert len(data) == 2  # Two students should be present

def test_validation_error_on_empty_name(client):
    """Test validation error when name field is empty"""
    response = client.post('/students', json={'name': ''})
    assert response.status_code == 400  # Bad Request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Specific error code for validation
    assert data['error']['message'] == 'Name field is required.'
```