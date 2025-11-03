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


def test_create_student(test_client):
    """Test creating a new student with a valid name."""
    response = test_client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'Student created successfully'  # Assuming response format


def test_get_students(test_client):
    """Test retrieving all registered students."""
    # Create sample students
    test_client.post('/students', json={'name': 'John Doe'})
    test_client.post('/students', json={'name': 'Jane Smith'})
    
    response = test_client.get('/students')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2  # Should return two students
    assert all('name' in student for student in data)  # Each student should have a name


def test_update_student(test_client):
    """Test updating a student's name."""
    # Create a student to update
    response = test_client.post('/students', json={'name': 'John Doe'})
    student_id = json.loads(response.data)['student_id']  # Assuming response contains the student ID

    response = test_client.put(f'/students/{student_id}', json={'name': 'John Smith'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Student updated successfully'  # Check response message


def test_delete_student(test_client):
    """Test deleting a student."""
    # Create a student to delete
    response = test_client.post('/students', json={'name': 'John Doe'})
    student_id = json.loads(response.data)['student_id']  # Assuming response contains the student ID

    response = test_client.delete(f'/students/{student_id}')
    assert response.status_code == 204  # Check for No Content status

    # Verify student is deleted
    response = test_client.get('/students')
    data = json.loads(response.data)
    assert len(data) == 0  # Should return no students after deletion