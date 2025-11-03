```python
import pytest
from app import create_app, db
from app.models import Teacher  # Assuming the Teacher model has been defined

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database tables after tests

def test_create_teacher(client):
    """Test creating a new teacher."""
    response = client.post('/teachers', json={"name": "Test Teacher", "email": "test@example.com"})
    assert response.status_code == 201  # Expecting Created status
    assert response.json['email'] == "test@example.com"
    assert response.json['name'] == "Test Teacher"

def test_create_teacher_with_duplicate_email(client):
    """Test creating a teacher with a duplicate email."""
    client.post('/teachers', json={"name": "Test Teacher 1", "email": "duplicate@example.com"})
    response = client.post('/teachers', json={"name": "Test Teacher 2", "email": "duplicate@example.com"})
    assert response.status_code == 400  # Expecting Bad Request status

def test_retrieve_all_teachers(client):
    """Test retrieving all teachers."""
    client.post('/teachers', json={"name": "Test Teacher 1", "email": "test1@example.com"})
    client.post('/teachers', json={"name": "Test Teacher 2", "email": "test2@example.com"})
    response = client.get('/teachers')
    assert response.status_code == 200  # Expecting OK status
    assert len(response.json) == 2  # Expecting two teachers in the response

def test_update_teacher(client):
    """Test updating teacher information."""
    response = client.post('/teachers', json={"name": "Old Teacher", "email": "old@example.com"})
    teacher_id = response.json['id']  # Get the ID of the created teacher
    update_response = client.put(f'/teachers/{teacher_id}', json={"name": "Updated Teacher", "email": "updated@example.com"})
    assert update_response.status_code == 200  # Expecting OK status
    assert update_response.json['name'] == "Updated Teacher"
    assert update_response.json['email'] == "updated@example.com"
```