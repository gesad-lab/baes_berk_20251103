```python
import pytest
import json

# Constants for API testing
BASE_URL = "http://localhost:5000/students"


@pytest.fixture
def student_data():
    """Provides valid student data for creating a new student."""
    return {
        "name": "John Doe"
    }


@pytest.fixture
def invalid_student_data():
    """Provides invalid student data for testing error handling."""
    return {
        "name": ""  # Invalid because the name is empty
    }


def test_create_student(client, student_data):
    """
    Test case for creating a new student.

    User sends a POST request with valid student data,
    and the application responds with the created student's data.
    """
    response = client.post(BASE_URL, json=student_data)
    assert response.status_code == 201  # Check for created status
    assert "name" in response.json  # Check response contains the name
    assert response.json["name"] == student_data["name"]  # Verify student name


def test_fetch_student(client, student_data):
    """
    Test case for fetching a student by ID.

    User sends a GET request with a valid student ID,
    and the application responds with the student's name.
    """
    create_response = client.post(BASE_URL, json=student_data)
    student_id = create_response.json["id"]  # Get the ID of the created student

    response = client.get(f"{BASE_URL}/{student_id}")
    assert response.status_code == 200  # Check for success status
    assert response.json["name"] == student_data["name"]  # Verify the fetched name


def test_update_student(client, student_data):
    """
    Test case for updating a student's name.

    User sends a PUT request with a valid student ID and new name,
    and the application responds with the updated student data.
    """
    create_response = client.post(BASE_URL, json=student_data)
    student_id = create_response.json["id"]  # Get the ID of the created student
    updated_data = {"name": "Jane Doe"}  # New name to update

    response = client.put(f"{BASE_URL}/{student_id}", json=updated_data)
    assert response.status_code == 200  # Check for success status
    assert response.json["name"] == updated_data["name"]  # Verify updated name


def test_delete_student(client, student_data):
    """
    Test case for deleting a student by ID.

    User sends a DELETE request with a valid student ID,
    and the application responds with a confirmation message.
    """
    create_response = client.post(BASE_URL, json=student_data)
    student_id = create_response.json["id"]  # Get the ID of the created student

    response = client.delete(f"{BASE_URL}/{student_id}")
    assert response.status_code == 200  # Check for success status
    assert response.json["message"] == "Student deleted successfully."


def test_create_student_invalid_data(client, invalid_student_data):
    """
    Test case for creating a student with invalid data.

    User sends a POST request without a valid name,
    and the application responds with an appropriate error message.
    """
    response = client.post(BASE_URL, json=invalid_student_data)
    assert response.status_code == 400  # Check for bad request status
    assert response.json == {
        "error": {
            "code": "E001",
            "message": "Invalid input. Name is required.",
            "details": {}
        }
    }


def test_fetch_student_not_found(client):
    """
    Test case for fetching a student that does not exist.

    User sends a GET request with an invalid student ID,
    and the application responds with an appropriate error message.
    """
    response = client.get(f"{BASE_URL}/999999")  # Non-existent ID
    assert response.status_code == 404  # Check for not found status
    assert response.json == {
        "error": {
            "code": "E002",
            "message": "Student not found.",
            "details": {}
        }
    }
```