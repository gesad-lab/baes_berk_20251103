```python
import pytest
from app import create_app, db
from app.models import Teacher  # Ensure the Teacher model is imported
import json

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables for testing
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after tests

def test_create_teacher(client):
    """Test creating a teacher successfully."""
    response = client.post('/teachers', json={"name": "Teacher Name", "email": "teacher@example.com"})
    assert response.status_code == 201  # Check for 201 Created
    assert response.json['name'] == "Teacher Name"  # Verify the teacher's name
    assert response.json['email'] == "teacher@example.com"  # Verify the teacher's email

def test_retrieve_all_teachers(client):
    """Test retrieving all teachers."""
    client.post('/teachers', json={"name": "Teacher Name", "email": "teacher@example.com"})  # Create a teacher
    response = client.get('/teachers')  # Retrieve all teachers
    assert response.status_code == 200  # Check for 200 OK
    assert isinstance(response.json, list)  # Verify response is a list
    assert len(response.json) > 0  # Ensure there is at least one teacher

def test_update_teacher(client):
    """Test updating existing teacher information."""
    # First create a teacher to update
    create_response = client.post('/teachers', json={"name": "Old Name", "email": "old@example.com"})
    teacher_id = create_response.json['id']  # Get the created teacher's ID

    # Now update the teacher's information
    update_response = client.put(f'/teachers/{teacher_id}', json={"name": "Updated Name", "email": "updated@example.com"})
    assert update_response.status_code == 200  # Check for 200 OK
    assert update_response.json['name'] == "Updated Name"  # Verify updated name
    assert update_response.json['email'] == "updated@example.com"  # Verify updated email
```