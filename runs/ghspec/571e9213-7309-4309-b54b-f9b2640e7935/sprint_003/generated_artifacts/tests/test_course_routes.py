```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py
from models import Course  # Assuming your Course model is defined here
from sqlalchemy.exc import IntegrityError

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up and tear down the database for integration tests.
    This should create a fresh database before tests and drop it after.
    """
    # Code to set up the database should go here
    # e.g., creating tables and adding mock data. This could utilize Alembic migrations if necessary.
    pass

@pytest.fixture
def create_course():
    """
    Fixture to create a course for testing. The created course must have
    valid attributes including name and level.
    """
    valid_course_data = {"name": "Mathematics", "level": "Beginner"}
    response = client.post("/courses", json=valid_course_data)
    assert response.status_code == 201  # Checking for successful creation
    return response.json()  # Return the created course data for further tests

def test_create_course(create_course):
    """
    Test the creation of a course.
    """
    valid_course_data = {"name": "Science", "level": "Intermediate"}
    response = client.post("/courses", json=valid_course_data)
    assert response.status_code == 201
    assert response.json()["name"] == valid_course_data["name"]
    assert response.json()["level"] == valid_course_data["level"]

def test_create_course_missing_name():
    """
    Test creating a course with missing name.
    """
    invalid_course_data = {"level": "Advanced"}  # Missing name
    response = client.post("/courses", json=invalid_course_data)
    assert response.status_code == 422  # Unprocessable entity for validation errors
    assert "name" in response.json()["detail"][0]["loc"]  # Check for validation error in response

def test_create_course_missing_level():
    """
    Test creating a course with missing level.
    """
    invalid_course_data = {"name": "History"}  # Missing level
    response = client.post("/courses", json=invalid_course_data)
    assert response.status_code == 422  # Unprocessable entity for validation errors
    assert "level" in response.json()["detail"][0]["loc"]  # Check for validation error in response

def test_get_course_by_id(create_course):
    """
    Test retrieving a course by its ID.
    """
    course_id = create_course["id"]
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["id"] == course_id

def test_get_course_not_found():
    """
    Test retrieving a course that does not exist.
    """
    response = client.get("/courses/99999")  # Non-existing ID
    assert response.status_code == 404  # Not found status for invalid course ID
```
