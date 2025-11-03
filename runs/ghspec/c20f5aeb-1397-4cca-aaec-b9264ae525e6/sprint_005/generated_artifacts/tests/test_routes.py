```python
import json
import time
import pytest
from app import app, db
from models import Teacher  # Importing the Teacher model for testing

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables
        yield client
        db.drop_all()  # Cleanup after each test

def test_create_teacher_success(client):
    """Test that creating a teacher with valid data succeeds."""
    response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert 'id' in response.get_json()  # Check if ID is returned
    assert response.get_json()['name'] == "John Doe"
    assert response.get_json()['email'] == "john.doe@example.com"

def test_get_teacher_details(client):
    """Test fetching details of a specific teacher."""
    # First, create a teacher to test retrieval
    response_create = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    teacher_id = response_create.get_json()['id']
    
    # Now, retrieve the teacher's details using the returned ID
    response = client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200
    assert response.get_json()['id'] == teacher_id
    assert response.get_json()['name'] == "John Doe"
    assert response.get_json()['email'] == "john.doe@example.com"

def test_create_teacher_missing_name(client):
    """Test creating a teacher without a name returns error."""
    response = client.post('/teachers', json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert 'missing' in response.get_json()['error']['message']

def test_create_teacher_missing_email(client):
    """Test creating a teacher without an email returns error."""
    response = client.post('/teachers', json={"name": "John Doe"})
    assert response.status_code == 400
    assert 'missing' in response.get_json()['error']['message']
```