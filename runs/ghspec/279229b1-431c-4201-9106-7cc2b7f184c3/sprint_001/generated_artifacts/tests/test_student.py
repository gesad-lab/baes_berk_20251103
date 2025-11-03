```python
import pytest
import json
from your_app_name import create_app, db  # Adjust according to your application structure
from your_app_name.models import Student  # Adjust according to your application structure

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests
    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.drop_all()  # Drop tables after tests

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def add_student(client):
    """Helper function to add a student for testing purposes."""
    response = client.post('/students', json={'name': 'Test Student'})
    return response.get_json()  # Return the newly created student record

def test_update_student_name(client, add_student):
    """Test updating an existing student's name."""
    student_id = add_student['id']  # Get the ID of the created student
    new_name = "Updated Student Name"
    
    # Update the student's name
    response = client.put(f'/students/{student_id}', json={'name': new_name})
    
    # Assert the response status code and data
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Student updated successfully'}

    # Validate the student's name has been updated in the database
    updated_student = Student.query.get(student_id)
    assert updated_student.name == new_name

def test_update_student_name_invalid_id(client):
    """Test updating a student with an invalid ID."""
    invalid_id = 99999  # Assuming this ID does not exist
    response = client.put(f'/students/{invalid_id}', json={'name': 'New Name'})

    # Assert the response for a non-existent student
    assert response.status_code == 404
    assert response.get_json() == {'error': {'code': 'E404', 'message': 'Student not found'}}

def test_update_student_name_missing_name(client, add_student):
    """Test updating a student's name with a missing name field."""
    student_id = add_student['id']  # Get the ID of the created student
    response = client.put(f'/students/{student_id}', json={})  # No name provided

    # Assert the response for missing name error
    assert response.status_code == 400
    assert response.get_json() == {'error': {'code': 'E400', 'message': 'Name field is required'}}
```