```python
import pytest
from flask import json
from your_app import create_app, db  # make sure to replace with actual import paths
from your_app.models import Teacher  # include the new Teacher model

@pytest.fixture
def client():
    app = create_app('testing')  # use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create the database schema
            yield client  # yield the test client
            db.drop_all()  # clean up the database after tests

def test_create_teacher(client):
    """Test the creation of a new teacher."""
    # Define the payload to create a new teacher
    payload = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    
    # Send a POST request to create a new teacher
    response = client.post('/teachers', data=json.dumps(payload), content_type='application/json')
    
    # Check for successful creation response
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Teacher created successfully.'}

def test_retrieve_teacher(client):
    """Test retrieving an existing teacher's information."""
    # Create a teacher first to retrieve
    teacher = Teacher(name='Jane Smith', email='jane.smith@example.com')
    db.session.add(teacher)
    db.session.commit()

    # Send a GET request to retrieve the teacher by ID
    response = client.get(f'/teachers/{teacher.id}')

    # Check for the response containing teacher information
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data['name'] == teacher.name
    assert response_data['email'] == teacher.email

def test_create_teacher_missing_fields(client):
    """Test error handling when missing required fields for teacher creation."""
    # Define payload with missing email
    payload = {
        'name': 'Alice'
    }
    
    # Send a POST request to create a new teacher
    response = client.post('/teachers', data=json.dumps(payload), content_type='application/json')
    
    # Check for error response indicating required fields
    assert response.status_code == 400
    assert response.get_json() == {'error': {'code': 'E001', 'message': 'Email is required.'}}

def test_database_schema_update(client):
    """Test to verify the Teacher table exists in the database."""
    # After the application starts, check the database schema
    with app.app_context():
        # Ensure the Teacher table exists
        assert db.engine.dialect.has_table(db.engine, 'teacher')  # replace 'teacher' with actual table name if different
        # Ensure existing data in other tables remains intact
        assert db.engine.dialect.has_table(db.engine, 'student')
        assert db.engine.dialect.has_table(db.engine, 'course')
```