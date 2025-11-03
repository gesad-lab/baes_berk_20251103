```python
import pytest
from fastapi.testclient import TestClient
from src.api.course_api import app  # Import the FastAPI app for the Course API
from src.models.course import Course  # Import the Course model
from src.services.course_service import create_course, get_all_courses  # Import course services
from sqlalchemy.exc import IntegrityError

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Set up the database for testing."""
    # Setup logic (e.g., create tables, insert initial data)
    # This should include creating a Course table and cleaning up after tests

def test_create_course_success(setup_database):
    """Test the creation of a course with valid data."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201  # Check for created status code
    assert response.json() == {"name": "Mathematics", "level": "Beginner"}

def test_create_course_missing_level(setup_database):
    """Test attempting to create a course with a missing level."""
    response = client.post("/courses", json={"name": "Physics"})  # Missing 'level'
    assert response.status_code == 400  # Check for bad request due to validation
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Level is required",
            "details": {}
        }
    }

def test_get_all_courses(setup_database):
    """Test retrieving all courses."""
    response = client.get("/courses")
    assert response.status_code == 200  # Check for successful retrieval
    assert isinstance(response.json(), list)  # Should return a list
    # Optional: Further assertions to check specific course data can be added here
```