```python
import pytest
from app import app  # Import the Flask app
from flask import json
from models.teacher import Teacher  # Import the Teacher model
from database import session  # Import the database session

@pytest.mark.integration
def test_get_teacher_with_valid_id(client):
    """
    Test case for retrieving a teacher's details by ID.
    Endpoint: GET /teachers/<teacher_id>
    Expected Outcome: 
      Status code 200, returns teacher details as JSON.
    """
    # Setup: Create a teacher entity to test retrieval
    new_teacher = Teacher(name="John Doe", email="john@example.com")
    session.add(new_teacher)
    session.commit()
    
    teacher_id = new_teacher.id  # Get the ID of the created teacher

    response = client.get(f'/teachers/{teacher_id}')  # Make a GET request

    # Assert the response
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['teacher'] == {
        "id": teacher_id,
        "name": "John Doe",
        "email": "john@example.com"
    }

@pytest.mark.integration
def test_get_teacher_with_invalid_id(client):
    """
    Test case for handling retrieval of a teacher with an invalid ID.
    Endpoint: GET /teachers/<teacher_id>
    Expected Outcome: 
      Status code 404, returns error message indicating teacher not found.
    """
    invalid_teacher_id = 999  # Assuming this ID does not exist

    response = client.get(f'/teachers/{invalid_teacher_id}')  # Make a GET request

    # Assert the response
    assert response.status_code == 404
    response_data = json.loads(response.data)
    assert response_data == {
        "error": {
            "code": "E404",
            "message": "Teacher not found."
        }
    }

@pytest.mark.integration
def test_get_teacher_without_id(client):
    """
    Test case for handling retrieval of a teacher without specifying an ID.
    Endpoint: GET /teachers/
    Expected Outcome: 
      Status code 405, because the endpoint does not support this method.
    """
    response = client.get('/teachers/')  # Make a GET request

    # Assert the response
    assert response.status_code == 405
```