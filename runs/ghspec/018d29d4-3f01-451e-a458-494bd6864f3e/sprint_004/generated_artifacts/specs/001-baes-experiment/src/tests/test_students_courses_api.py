```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assume FastAPI app is instantiated in a file named main.py

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    # Setup the database: create tables as necessary before tests
    # This would normally include dropping any existing tables and re-creating them
    pass  # Replace with actual setup code

def test_associate_student_with_valid_courses():
    """Test associating a student with valid course IDs."""
    response = client.post("/students/1/courses", json={"course_ids": [1, 2]})
    assert response.status_code == 200

def test_retrieve_student_courses():
    """Test retrieving courses associated with a student."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert "courses" in response.json()

def test_associate_student_with_invalid_courses():
    """Test associating a student with non-existing course IDs."""
    # Attempt to associate a student with invalid course IDs
    response = client.post("/students/1/courses", json={"course_ids": [999, 1000]})
    
    # Check if the system responds with a 400 Bad Request status
    assert response.status_code == 400
    
    # Validate the error response content to ensure it provides actionable feedback
    error_response = response.json()
    assert "error" in error_response
    assert error_response["error"]["code"] == "E001"  # Example error code for invalid course IDs
    assert "Invalid course IDs provided." in error_response["error"]["message"]  # Ensure the message is clear
```