```python
import json
import pytest
from your_app import create_app, db  # Adjust import based on your app structure
from your_app.models import Student, Course, Teacher  # Adjust import for your Teacher model

app = create_app()

# Centralized error handling for missing course data
@app.errorhandler(400)
def handle_bad_request(error):
    response = {
        "error": {
            "code": "E400",
            "message": "Bad request",
            "details": str(error.description),
        }
    }
    return jsonify(response), 400

# Centralized error handling for duplicate email
@app.errorhandler(409)
def handle_conflict(error):
    response = {
        "error": {
            "code": "E409",
            "message": "Conflict: Email must be unique",
            "details": str(error.description),
        }
    }
    return jsonify(response), 409

# Test function for creating teachers
@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables in the database
        yield client

def test_create_teacher_success(client):
    """Test creating a teacher with valid data"""
    response = client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201  # HTTP 201 Created
    assert 'id' in response.json  # Ensure the response includes the teacher ID

def test_create_teacher_duplicate_email(client):
    """Test creating a teacher with a duplicate email"""
    # First, create a teacher with this email
    client.post('/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    
    # Now, attempt to create another teacher with the same email
    response = client.post('/teachers', json={
        'name': 'Jane Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 409  # HTTP 409 Conflict
    assert response.json == {
        "error": {
            "code": "E409",
            "message": "Conflict: Email must be unique",
            "details": f"The email 'john.doe@example.com' is already registered."
        }
    }

def test_create_teacher_missing_name(client):
    """Test creating a teacher without a name"""
    response = client.post('/teachers', json={
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 400  # HTTP 400 Bad Request
    assert response.json == {
        "error": {
            "code": "E400",
            "message": "Bad request",
            "details": "Missing required data: name"
        }
    }
```