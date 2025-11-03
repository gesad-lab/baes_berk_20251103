```python
import pytest
from flask import json
from app import create_app, db
from app.models import Student

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    
    # Create a test client using the Flask application configured for testing
    with app.test_client() as client:
        with app.app_context():
            # Create all tables in the database
            db.create_all()
            yield client
            # Cleanup after tests
            db.drop_all()

def test_create_student_with_valid_email(test_client):
    """Test that a student record can be created successfully with valid email."""
    response = test_client.post('/students', 
        data=json.dumps({'name': 'John Doe', 'email': 'john.doe@example.com'}),
        content_type='application/json'
    )
    assert response.status_code == 201  # Expecting a successful creation
    assert 'student_id' in response.json

def test_create_student_with_invalid_email_format(test_client):
    """Test that error is raised for invalid email format."""
    response = test_client.post('/students', 
        data=json.dumps({'name': 'Jane Doe', 'email': 'invalid_email'}),
        content_type='application/json'
    )
    assert response.status_code == 400  # Bad Request expected
    assert response.json['error']['code'] == "E002"
    assert response.json['error']['message'] == "Invalid email format"

def test_create_student_with_missing_email(test_client):
    """Test that error is raised when email is missing."""
    response = test_client.post('/students', 
        data=json.dumps({'name': 'Alice'}),
        content_type='application/json'
    )
    assert response.status_code == 400  # Bad Request expected
    assert response.json['error']['code'] == "E001"
    assert response.json['error']['message'] == "Missing required email field"
```