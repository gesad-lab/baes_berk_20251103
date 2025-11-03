```python
import pytest
from flask import json
from app import create_app, db
from src.models.student import Student

@pytest.fixture
def client():
    """Setup testing client for the application."""
    app = create_app('testing')  # Create app in testing mode
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Setup the database before tests
        yield client
        db.drop_all()  # Clean up after tests

# Unit tests for updating student email
def test_update_student_email_success(client):
    """Test updating a student's email successfully."""
    # Setup: Register a new student
    response = client.post('/api/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    assert response.status_code == 201  # Check if student created successfully
    student_id = response.get_json()['id']

    # Act: Update the student's email
    new_email = 'jane.d.new@example.com'
    update_response = client.put(f'/api/students/{student_id}', json={
        'email': new_email
    })

    # Assert: Verify response and database update
    assert update_response.status_code == 200
    updated_student = Student.query.get(student_id)
    assert updated_student.email == new_email, "Student email should be updated"

def test_update_student_email_invalid_format(client):
    """Test updating a student's email with an invalid format returns an error."""
    # Setup: Register a new student
    response = client.post('/api/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    assert response.status_code == 201
    student_id = response.get_json()['id']

    # Act: Attempt to update the student's email to an invalid format
    invalid_email = 'invalid-email-format'
    update_response = client.put(f'/api/students/{student_id}', json={
        'email': invalid_email
    })

    # Assert: Verify that an error message is received
    assert update_response.status_code == 400
    assert 'error' in update_response.get_json(), "Should return error message"
    assert update_response.get_json()['error']['code'] == 'E001', "Should return specific error code"

def test_update_student_email_non_existent(client):
    """Test updating an email for a non-existent student returns a not found error."""
    non_existent_id = 9999  # Assume this ID does not exist
    update_response = client.put(f'/api/students/{non_existent_id}', json={
        'email': 'some.email@example.com'
    })

    # Assert: Verify the response for a non-existent student
    assert update_response.status_code == 404
    assert 'error' in update_response.get_json(), "Should return error message"
```
