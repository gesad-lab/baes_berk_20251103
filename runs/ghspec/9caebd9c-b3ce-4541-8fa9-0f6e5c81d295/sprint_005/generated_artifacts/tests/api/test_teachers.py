```python
import json
import pytest
from your_application import app, db, Teacher  # Adjust import based on your structure

# Reinitialize the Flask application and SQLAlchemy for testing
@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables for testing
            yield client
            db.drop_all()  # Clean up after tests

def test_create_teacher_success(test_client):
    """Test the creation of a teacher with valid data."""
    response = test_client.post('/teachers', 
                                 data=json.dumps({"name": "John Doe", "email": "john@example.com"}),
                                 content_type='application/json')
    assert response.status_code == 201  # Confirm resource created
    assert b'Teacher created successfully' in response.data

def test_create_teacher_missing_name(test_client):
    """Test creating a teacher without a name."""
    response = test_client.post('/teachers', 
                                 data=json.dumps({"email": "john@example.com"}),
                                 content_type='application/json')
    assert response.status_code == 400  # Bad Request
    assert b'{"error": {"code": "E001", "message": "Name is required"}}' in response.data

def test_create_teacher_missing_email(test_client):
    """Test creating a teacher without an email."""
    response = test_client.post('/teachers', 
                                 data=json.dumps({"name": "John Doe"}),
                                 content_type='application/json')
    assert response.status_code == 400  # Bad Request
    assert b'{"error": {"code": "E002", "message": "Email is required"}}' in response.data

def test_create_teacher_duplicate_email(test_client):
    """Test creating a teacher with a duplicate email."""
    test_client.post('/teachers', 
                     data=json.dumps({"name": "John Doe", "email": "john@example.com"}),
                     content_type='application/json')
    response = test_client.post('/teachers', 
                                 data=json.dumps({"name": "Jane Doe", "email": "john@example.com"}),
                                 content_type='application/json')
    assert response.status_code == 400  # Bad Request
    assert b'{"error": {"code": "E003", "message": "Email must be unique"}}' in response.data

def test_retrieve_teacher_success(test_client):
    """Test retrieving a teacher's information."""
    response = test_client.post('/teachers', 
                                 data=json.dumps({"name": "John Doe", "email": "john@example.com"}),
                                 content_type='application/json')
    teacher_id = json.loads(response.data)['id']  # Extract the ID of the created teacher

    response = test_client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200  # OK
    teacher_data = json.loads(response.data)
    assert teacher_data['name'] == "John Doe"
    assert teacher_data['email'] == "john@example.com"

def test_retrieve_teacher_not_found(test_client):
    """Test retrieving a non-existent teacher."""
    response = test_client.get('/teachers/99999')  # Assuming no teacher has this ID
    assert response.status_code == 404  # Not Found
    assert b'{"error": {"code": "E004", "message": "Teacher not found"}}' in response.data
```