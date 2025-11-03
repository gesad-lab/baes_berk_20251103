```python
import pytest
from src.app import app, db
from src.models import Student

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_create_student(client):
    """Test that a student can be created successfully."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.json == {'message': 'Student created successfully', 'id': response.json['id']}

def test_retrieve_student(client):
    """Test that a student can be retrieved by ID."""
    # First, create a student
    response = client.post('/students', json={'name': 'John Doe'})
    student_id = response.json['id']
    
    # Now, retrieve the student
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json == {'id': student_id, 'name': 'John Doe'}

def test_retrieve_non_existent_student(client):
    """Test that retrieving a non-existent student returns an error message."""
    response = client.get('/students/99999')  # Assuming 99999 is an ID that does not exist
    assert response.status_code == 404
    assert response.json == {'error': {'code': 'E404', 'message': 'Student not found'}}

def test_create_student_missing_name(client):
    """Test that creating a student without a name returns a validation error."""
    response = client.post('/students', json={})  # Empty payload
    assert response.status_code == 400
    assert response.json == {'error': {'code': 'E400', 'message': 'Missing required field: name'}}
```