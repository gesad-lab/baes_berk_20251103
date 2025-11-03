```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the main FastAPI application is in src/main.py
from src.database import get_database  # Assuming there is a function to get the database

client = TestClient(app)

# Integration tests for the course API endpoints
@pytest.mark.integration
def test_create_course_with_valid_data():
    """Test creating a new course with valid data."""
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201  # Expecting a successful creation
    data = response.json()
    assert data["name"] == "Math 101"
    assert data["level"] == "Beginner"

@pytest.mark.integration
def test_list_courses():
    """Test retrieving the list of courses."""
    response = client.get("/courses")
    assert response.status_code == 200  # Expecting a successful retrieval
    data = response.json()
    assert isinstance(data, list)  # Expecting a JSON array
    # Additional checks can be added based on initial expected data

@pytest.mark.integration
def test_create_course_with_missing_level():
    """Test creating a new course with missing level field."""
    response = client.post("/courses", json={"name": "Science 101"})
    assert response.status_code == 400  # Expecting a bad request
    data = response.json()
    assert data["error"]["code"] == "E002"  # Assuming E002 for missing level
    assert "level field is required" in data["error"]["message"]

# Performance testing descriptions for /courses endpoints
def describe_courses_endpoints():
    """Overview of /courses API endpoints with example requests and responses."""
    
    ## 1. Create Course Endpoint
    """
    POST /courses
    Request Body:
    {
        "name": "Math 101",
        "level": "Beginner"
    }
    Successful Response:
    Status Code: 201 Created
    Response Body:
    {
        "name": "Math 101",
        "level": "Beginner"
    }
    """

    ## 2. List Courses Endpoint
    """
    GET /courses
    Successful Response:
    Status Code: 200 OK
    Response Body:
    [
        {
            "name": "Math 101",
            "level": "Beginner"
        },
        {
            "name": "Science 101",
            "level": "Intermediate"
        }
    ]
    """
```