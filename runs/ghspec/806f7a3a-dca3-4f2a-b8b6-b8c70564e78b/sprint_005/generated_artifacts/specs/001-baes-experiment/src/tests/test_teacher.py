```python
import pytest
from flask import json
from app import create_app, db
from models.teacher import Teacher  # Import the Teacher model
from models.student import Student  # Import the Student model
from routes.teacher_routes import teacher_bp  # Import the teacher routes

@pytest.fixture
def client():
    app = create_app('testing')  # Use a separate testing configuration
    app.register_blueprint(teacher_bp)  # Register the teacher routes
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create fresh database for testing
            yield client
            db.drop_all()  # Drop all tables after tests are complete

def test_create_teacher(client):
    """Test that a teacher can be created successfully."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }), content_type='application/json')
    
    assert response.status_code == 201  # Check status code for created
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'  # Verify returned name
    assert data['email'] == 'john.doe@example.com'  # Verify returned email

def test_create_teacher_invalid_email(client):
    """Test that creating a teacher with invalid email fails."""
    response = client.post('/teachers', data=json.dumps({
        'name': 'Jane Doe',
        'email': 'invalid-email'  # Invalid email format
    }), content_type='application/json')
    
    assert response.status_code == 400  # Check for bad request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Confirm error code for invalid input

def test_get_teacher(client):
    """Test that a created teacher can be retrieved successfully."""
    # First, create a teacher
    create_response = client.post('/teachers', data=json.dumps({
        'name': 'John Smith',
        'email': 'john.smith@example.com'
    }), content_type='application/json')
    
    teacher_id = json.loads(create_response.data)['id']  # Get the teacher ID from the response

    # Now, attempt to retrieve the teacher
    response = client.get(f'/teachers/{teacher_id}')
    
    assert response.status_code == 200  # Check for successful retrieval
    data = json.loads(response.data)
    assert data['name'] == 'John Smith'  # Verify returned name
    assert data['email'] == 'john.smith@example.com'  # Verify returned email

def test_get_teacher_not_found(client):
    """Test that retrieving a nonexistent teacher returns a 404 error."""
    response = client.get('/teachers/9999')  # Nonexistent ID
    
    assert response.status_code == 404  # Check for not found
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'  # Confirm error code for not found
```