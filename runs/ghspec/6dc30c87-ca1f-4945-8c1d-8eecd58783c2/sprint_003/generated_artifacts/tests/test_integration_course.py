```python
import pytest
from fastapi.testclient import TestClient
from myapp.main import app  # Assuming that the FastAPI app is defined in myapp/main.py
from myapp.database import create_database_schema
from myapp.models import Course  # Assuming you have a Course model defined

# Create a TestClient for making requests to the FastAPI app
client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Fixture to set up the database schema on startup."""
    create_database_schema()  # Ensure the database schema is created for testing
    yield
    # Teardown logic can be added here if necessary

def test_retrieve_course_with_invalid_id():
    """Test retrieving a course with an invalid ID returns a 404 status and error message."""
    invalid_id = 999  # Assuming this ID does not exist
    response = client.get(f"/courses/{invalid_id}")
    
    assert response.status_code == 404  # Expecting 404 Not Found for invalid ID
    assert response.json() == {
        "error": {
            "code": "E404",
            "message": "Course not found",
            "details": {}
        }
    }

def test_retrieve_course_with_non_numeric_id():
    """Test retrieving a course with a non-numeric ID returns a 422 status and error message."""
    non_numeric_id = "abc"  # Invalid ID format
    response = client.get(f"/courses/{non_numeric_id}")
    
    assert response.status_code == 422  # Expecting 422 Unprocessable Entity for invalid format
    assert response.json() == {
        "error": {
            "code": "E422",
            "message": "Invalid course ID format",
            "details": {}
        }
    }
```