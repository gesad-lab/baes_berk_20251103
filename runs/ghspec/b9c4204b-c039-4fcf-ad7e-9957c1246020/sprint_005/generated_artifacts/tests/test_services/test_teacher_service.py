```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Main FastAPI application
from src.models import Teacher  # Importing Teacher model for response validation

client = TestClient(app)

# Integration tests for the teacher API endpoints
@pytest.mark.integration
def test_get_teachers_returns_list_of_teachers():
    """Test retrieving a list of all teachers returns a proper JSON response"""
    
    # First, we can add some teachers to the database (assumed to be done elsewhere in setup)
    
    response = client.get("/teachers")  # Perform a GET request to the /teachers endpoint
    
    # Check the response status code
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
    # Check that the response is in JSON format
    assert response.headers["Content-Type"] == "application/json", "Response should be JSON format"
    
    # Parse the response body
    teachers = response.json()
    
    # Check if the response contains a list
    assert isinstance(teachers, list), "Response should be a list"
    
    # Optionally, check if the list contains expected fields
    if teachers:
        assert all("id" in teacher for teacher in teachers), "Each teacher should have an 'id' field"
        assert all("name" in teacher for teacher in teachers), "Each teacher should have a 'name' field"
        assert all("email" in teacher for teacher in teachers), "Each teacher should have an 'email' field"
    
    # Further tests can be added here for specific expected teachers, if known

@pytest.mark.integration
def test_get_teachers_empty_list_when_no_teachers_exist():
    """Test retrieving teachers when no teachers exist returns an empty list"""
    
    response = client.get("/teachers")  # Perform a GET request to the /teachers endpoint
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
    teachers = response.json()
    
    # Check that the response contains an empty list
    assert teachers == [], "Expected an empty list when no teachers exist"
```