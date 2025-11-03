```python
import json
import time
import pytest
from app import app, db
from models import Student

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables
        yield client
        db.drop_all()  # Cleanup after each test

def test_create_student_with_email_response_time(client):
    """Test that creating a student with an email responds within 2 seconds."""
    start_time = time.time()
    response = client.post('/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    assert 'email' in response.get_json()
    assert response.get_json()['email'] == "john.doe@example.com"
    assert time.time() - start_time < 2

def test_create_student_with_invalid_email(client):
    """Test that creating a student with an invalid email format results in a 400 error."""
    response = client.post('/students', json={
        "name": "Jane Doe",
        "email": "invalid-email"
    })
    assert response.status_code == 400
    assert response.get_json() == {
        "error": {
            "code": "E001",
            "message": "Invalid email format. Email is required and must be in a valid format.",
            "details": {}
        }
    }

def test_update_student_with_invalid_email(client):
    """Test that updating a student's email to an invalid format results in a 400 error."""
    # First, create a valid student
    response = client.post('/students', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    student_id = response.get_json()['id']

    # Try to update with an invalid email
    response = client.put(f'/students/{student_id}', json={
        "name": "John Doe Updated",
        "email": "invalid-email"
    })
    assert response.status_code == 400
    assert response.get_json() == {
        "error": {
            "code": "E001",
            "message": "Invalid email format. Email is required and must be in a valid format.",
            "details": {}
        }
    }
```