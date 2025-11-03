import pytest
from app import app  # Import the Flask app
from flask import json
from models.teacher import Teacher  # Assuming the Teacher model is defined here
from database import session  # Assuming the database session management

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_create_teacher_with_valid_data(client):
    """
    Test case for creating a teacher with valid input data.
    
    Expected Outcome: 
    Status code 201, confirmation message containing teacher details.
    """
    response = client.post('/teachers', json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['message'] == "Teacher created successfully."
    assert json_data['teacher']['name'] == "John Doe"
    assert json_data['teacher']['email'] == "john.doe@example.com"


def test_create_teacher_without_required_fields(client):
    """
    Test case for attempting to create a teacher without providing required fields.
    
    Expected Outcome: 
    Status code 400, error message indicating required fields.
    """
    response = client.post('/teachers', json={
        "name": "",
        "email": ""
    })
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data
    assert json_data['error']['message'] == "Both name and email are required."


def test_create_teacher_with_duplicate_email(client):
    """
    Test case for attempting to create a teacher with an email that already exists.
    
    Expected Outcome: 
    Status code 409, error message stating the email is already in use.
    """
    # First, create a teacher
    client.post('/teachers', json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    })

    # Now attempt to create another teacher with the same email
    response = client.post('/teachers', json={
        "name": "John Smith",
        "email": "jane.doe@example.com"
    })
    assert response.status_code == 409
    json_data = response.get_json()
    assert "error" in json_data
    assert json_data['error']['message'] == "Email is already in use."


def test_retrieve_teacher_with_valid_id(client):
    """
    Test case for retrieving a teacher using a valid ID.
    
    Expected Outcome: 
    Status code 200, returns the teacher's details in JSON format.
    """
    # First, create a teacher to retrieve
    response = client.post('/teachers', json={
        "name": "Emily Turner",
        "email": "emily.turner@example.com"
    })
    teacher_id = response.get_json()['teacher']['id']

    # Now retrieve the teacher
    response = client.get(f'/teachers/{teacher_id}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['name'] == "Emily Turner"
    assert json_data['email'] == "emily.turner@example.com"


def test_retrieve_teacher_with_invalid_id(client):
    """
    Test case for retrieving a teacher using an ID that does not exist.
    
    Expected Outcome: 
    Status code 404, error message indicating the teacher was not found.
    """
    response = client.get('/teachers/99999')  # Assuming this ID does not exist
    assert response.status_code == 404
    json_data = response.get_json()
    assert "error" in json_data
    assert json_data['error']['message'] == "Teacher not found."