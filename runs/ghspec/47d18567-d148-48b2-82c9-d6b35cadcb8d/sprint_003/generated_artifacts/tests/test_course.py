```python
import json
import pytest
from fastapi.testclient import TestClient
from src.api.course import app  # Assuming 'app' is the FastAPI instance for course
from src.db.models import Course  # Import the Course model
from src.validations.course_validators import validate_course_input  # Import the validation function

client = TestClient(app)

@pytest.fixture
def valid_course():
    """Fixture to return valid course data."""
    return {"name": "Introduction to Programming", "level": "Beginner"}

@pytest.fixture
def invalid_course_missing_name():
    """Fixture to return course data missing the name field."""
    return {"level": "Beginner"}

@pytest.fixture
def invalid_course_missing_level():
    """Fixture to return course data missing the level field."""
    return {"name": "Introduction to Programming"}

def test_create_course_with_valid_data(valid_course):
    """Test that a course can be created successfully with valid data."""
    response = client.post("/courses", json=valid_course)
    assert response.status_code == 201  # Expecting successful creation
    data = response.json()
    assert data["name"] == valid_course["name"]
    assert data["level"] == valid_course["level"]

def test_create_course_missing_name(invalid_course_missing_name):
    """Test that creating a course without a name returns an error."""
    response = client.post("/courses", json=invalid_course_missing_name)
    assert response.status_code == 400  # Expecting a bad request error
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Course name is required.",
            "details": {}
        }
    }

def test_create_course_missing_level(invalid_course_missing_level):
    """Test that creating a course without a level returns an error."""
    response = client.post("/courses", json=invalid_course_missing_level)
    assert response.status_code == 400  # Expecting a bad request error
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Course level is required.",
            "details": {}
        }
    }
```