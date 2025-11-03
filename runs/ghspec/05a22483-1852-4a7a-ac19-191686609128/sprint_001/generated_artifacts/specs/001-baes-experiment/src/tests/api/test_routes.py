import pytest
from flask import Flask, jsonify, request
from your_app import create_app, db  # make sure to replace with actual import paths
from your_app.models import Student  # update with actual model import


@pytest.fixture
def client():
    app = create_app('testing')  # use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create the database schema
        yield client
        with app.app_context():
            db.drop_all()  # clean up the database after tests


def test_create_student(client):
    """Test the creation of a new student."""
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201  # Assert student is created successfully
    data = response.get_json()
    assert 'id' in data  # Assert a student ID is returned
    assert data['name'] == 'John Doe'  # Assert the name is correct


def test_create_student_invalid_data(client):
    """Test the failure of creating a student with invalid data."""
    response = client.post('/students', json={'name': ''})  # Empty name
    assert response.status_code == 400  # Assert bad request
    data = response.get_json()
    assert data['error']['code'] == 'E001'  # Check for specific error code
    assert data['error']['message'] == 'Name is required'  # Check error message


def test_get_student(client):
    """Test retrieving a student's details by ID."""
    # First, we need to create a student to retrieve
    post_response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = post_response.get_json()['id']

    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200  # Assert successful retrieval
    data = response.get_json()
    assert data['id'] == student_id  # Assert student ID matches
    assert data['name'] == 'Jane Doe'  # Assert name matches


def test_get_nonexistent_student(client):
    """Test the retrieval of a non-existing student."""
    response = client.get('/students/999999')  # Assume this ID does not exist
    assert response.status_code == 404  # Assert not found
    data = response.get_json()
    assert data['error']['code'] == 'E002'  # Check for specific error code
    assert data['error']['message'] == 'Student not found'  # Check error message