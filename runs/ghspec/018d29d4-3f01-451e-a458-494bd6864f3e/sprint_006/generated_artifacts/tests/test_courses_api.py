```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assume FastAPI app is instantiated in a file named main.py
from models import Course, Teacher  # Import the Course and Teacher models

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    """Setup the database before each test case."""
    # Prepare a clean state for the tests - this would typically setup tables etc.
    pass  # Implement your actual test DB setup logic here

def test_assign_teacher_to_course_valid():
    """Test assigning a teacher to a valid course."""
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200  # Ensure the request is successful
    assert response.json().get("message") == "Teacher assigned successfully"  # Check success message

def test_get_course_details_with_teacher():
    """Test retrieval of course details with an assigned teacher."""
    response = client.get("/courses/1")  # Assume course ID 1 has a teacher assigned
    assert response.status_code == 200  # Ensure the request is successful
    assert "teacher" in response.json()  # Ensure teacher info is included
    assert response.json()["teacher"]["name"] == "John Doe"  # Replace with expected teacher name

def test_course_without_assigned_teacher():
    """Test retrieval of course details that has no assigned teacher."""
    response = client.get("/courses/2")  # Assume course ID 2 has no teacher assigned
    assert response.status_code == 200  # Ensure the request is successful
    assert response.json()["message"] == "No teacher assigned"  # Check the absence note

def test_assign_teacher_to_invalid_course():
    """Test the response when assigning a teacher to a non-existing course."""
    response = client.post("/courses/999/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 404  # Ensure the request fails with 404
    assert response.json().get("error").get("code") == "E404"  # Validate the error code
    assert response.json().get("error").get("message") == "Course not found"  # Validate error message
```