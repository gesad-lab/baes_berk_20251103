import pytest
import requests

BASE_URL = "http://localhost:5000/api/v1/students"

@pytest.fixture(scope="module")
def student_data():
    """Fixture to provide example student data for tests."""
    return {
        "name": "John Doe"
    }


def test_create_student(student_data):
    """Test creating a new student record."""
    response = requests.post(BASE_URL, json=student_data)
    assert response.status_code == 201
    assert "id" in response.json()


def test_retrieve_students():
    """Test retrieving all student records."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_student(student_data):
    """Test updating an existing student record."""
    # First create a student
    response = requests.post(BASE_URL, json=student_data)
    student_id = response.json()["id"]
    
    # Update the student's name
    updated_data = {"name": "Jane Doe"}
    update_response = requests.put(f"{BASE_URL}/{student_id}", json=updated_data)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Jane Doe"


def test_delete_student():
    """Test deleting a student record."""
    # Create a student first to delete
    student_data = {"name": "To Be Deleted"}
    response = requests.post(BASE_URL, json=student_data)
    student_id = response.json()["id"]
    
    # Delete the student
    delete_response = requests.delete(f"{BASE_URL}/{student_id}")
    assert delete_response.status_code == 204
    
    # Verify the student is deleted
    get_response = requests.get(f"{BASE_URL}/{student_id}")
    assert get_response.status_code == 404


if __name__ == "__main__":
    pytest.main()