```python
import pytest
import requests

BASE_URL = "http://localhost:5000"  # Change this to your application's URL if different

@pytest.fixture(scope="module")
def setup_database():
    """Setup and teardown the integration test database."""
    # Assuming reset_database function resets the database
    reset_database()  
    yield
    # Clean up database after tests run
    reset_database()


def test_create_student_valid(setup_database):
    """Test creating a new student with valid data."""
    response = requests.post(f"{BASE_URL}/students", json={"name": "John Doe"})
    assert response.status_code == 201  # Check for success response
    assert "id" in response.json()  # Ensure that an ID is returned
    assert response.json()["name"] == "John Doe"


def test_create_student_missing_name(setup_database):
    """Test creating a student without providing a name."""
    response = requests.post(f"{BASE_URL}/students", json={})
    assert response.status_code == 400  # Check for bad request response
    assert response.json() == {"error": {"code": "E001", "message": "Name field is required"}}  # Expected error


def test_retrieve_students(setup_database):
    """Test retrieving a list of students."""
    response = requests.get(f"{BASE_URL}/students")
    assert response.status_code == 200  # Check for success response
    assert isinstance(response.json(), list)  # Ensure the response is a list


def test_update_student_name(setup_database):
    """Test updating an existing student's name."""
    # First create a student to update
    create_response = requests.post(f"{BASE_URL}/students", json={"name": "Jane Doe"})
    student_id = create_response.json()["id"]

    # Now update the student's name
    update_response = requests.put(f"{BASE_URL}/students/{student_id}", json={"name": "Jane Smith"})
    assert update_response.status_code == 200  # Check for success response
    assert update_response.json()["message"] == "Student updated successfully"  # Expected success message

    # Verify that the name was updated
    verify_response = requests.get(f"{BASE_URL}/students/{student_id}")
    assert verify_response.json()["name"] == "Jane Smith"  # Ensure the name was updated


def test_delete_student(setup_database):
    """Test deleting a specific student by ID."""
    # First create a student to delete
    create_response = requests.post(f"{BASE_URL}/students", json={"name": "Mark Smith"})
    student_id = create_response.json()["id"]

    # Now delete the student
    delete_response = requests.delete(f"{BASE_URL}/students/{student_id}")
    assert delete_response.status_code == 200  # Check for success response
    assert delete_response.json()["message"] == "Student deleted successfully"  # Expected success message
    
    # Ensure the student has actually been deleted
    verify_response = requests.get(f"{BASE_URL}/students/{student_id}")
    assert verify_response.status_code == 404  # Check for not found response
```