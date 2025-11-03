```python
import pytest
from flask import json
from app import create_app, db
from app.models import Student

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield testing_client  # This is where the testing happens
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_create_student_with_email(test_client):
    """Test creating a new student with a valid email."""
    response = test_client.post('/students', json={
        'name': 'John Doe',
        'age': 20,
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_retrieve_students_with_email(test_client):
    """Test retrieving a list of students, checking that emails are included."""
    response = test_client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)  # Response should be a list
    assert all('email' in student for student in data)  # Each student should have an email

def test_update_student_email(test_client):
    """Test updating a student's email."""
    # First, create a student
    response = test_client.post('/students', json={
        'name': 'Jane Doe',
        'age': 22,
        'email': 'jane.doe@example.com'
    })
    assert response.status_code == 201
    student_id = json.loads(response.data)['id']

    # Now, update the student's email
    update_response = test_client.put(f'/students/{student_id}', json={
        'email': 'jane.new@example.com'
    })
    assert update_response.status_code == 200
    updated_data = json.loads(update_response.data)
    assert updated_data['email'] == 'jane.new@example.com'

def test_create_student_with_invalid_email(test_client):
    """Test that a student cannot be created with an invalid email."""
    response = test_client.post('/students', json={
        'name': 'Invalid Email Student',
        'age': 21,
        'email': 'invalid-email'
    })
    assert response.status_code == 400
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E001'  # Custom error code for invalid email
    assert 'email' in error_data['error']['message']  # Error message should mention email
```