```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assume FastAPI app is instantiated in a file named main.py
from models import Course  # Import the Course model

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    """Setup the database before each test case."""
    # Normally you would set up the database, handle migrations, etc.
    # This may include creating the necessary tables and a clean state for every test
    pass  # Replace with actual setup code as needed

def test_assign_teacher_to_course_valid():
    """Test assigning a teacher to a valid course."""
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    # Optionally include more assertions to check the state after assignment

def test_get_course_details_with_teacher():
    """Test retrieving course details with an assigned teacher."""
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()  # Ensure teacher info is included
    assert response.json()["teacher"] == "Expected Teacher Name"  # Replace with actual expected name

def test_get_course_without_assigned_teacher():
    """Test that a course without an assigned teacher returns appropriate message."""
    response = client.get("/courses/2")  # Assuming course ID 2 has no assigned teacher
    assert response.status_code == 200
    assert "No teacher assigned" in response.json()["message"]  # Ensure the message is returned correctly

def test_assign_teacher_to_invalid_course():
    """Test the response when assigning a teacher to an invalid course ID."""
    response = client.post("/courses/999/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 404  # Confirm course does not exist
    assert response.json() == {"detail": "Course not found"}  # Expected response structure
```