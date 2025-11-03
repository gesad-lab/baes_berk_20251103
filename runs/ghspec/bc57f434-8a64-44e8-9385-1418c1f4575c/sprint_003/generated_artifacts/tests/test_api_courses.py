```python
import pytest
from fastapi.testclient import TestClient
from your_application.api import app  # The FastAPI application instance
from your_application.models import Course  # Importing the Course model 

# Fixture to create a test client
@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_create_course_with_valid_data(test_client):
    """Test creating a course with valid name and level."""
    response = test_client.post("/courses", json={"name": "Calculus", "level": "Advanced"})
    assert response.status_code == 201  # HTTP status code for created
    assert response.json() == {"id": 1, "name": "Calculus", "level": "Advanced"}  # Assuming the response includes the created course

def test_get_course_with_valid_id(test_client):
    """Test retrieving a course using its ID."""
    response = test_client.get("/courses/1")  # Replace with actual ID after creation
    assert response.status_code == 200  # HTTP status code for success
    assert response.json() == {"id": 1, "name": "Calculus", "level": "Advanced"}  # Check if it returns the correct course

def test_create_course_without_name(test_client):
    """Test creating a course without a name should fail."""
    response = test_client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400  # HTTP status code for bad request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required.",
            "details": {}
        }
    }

def test_create_course_without_level(test_client):
    """Test creating a course without a level should fail."""
    response = test_client.post("/courses", json={"name": "Physics"})
    assert response.status_code == 400  # HTTP status code for bad request
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Level is required.",
            "details": {}
        }
    }

def test_create_course_with_invalid_data_type(test_client):
    """Test creating a course with invalid data types should fail."""
    response = test_client.post("/courses", json={"name": 123, "level": True})  # Invalid types
    assert response.status_code == 422  # HTTP status code for unprocessable entity
    assert "detail" in response.json()  # Specific error details should be present in the response
```