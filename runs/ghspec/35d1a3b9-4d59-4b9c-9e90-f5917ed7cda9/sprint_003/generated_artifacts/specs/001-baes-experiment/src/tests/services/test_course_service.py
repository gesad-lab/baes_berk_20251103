```python
import pytest
from fastapi.testclient import TestClient
from src.services.course_service import create_course, get_courses
from src.repository import models, create_db

# Setup for tests
@pytest.fixture(scope="module")
def client():
    # Create an instance of the TestClient
    app = create_db()  # Assuming create_db initializes and sets up the FastAPI app
    yield TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Initialize the database schema and data before tests
    models.Base.metadata.create_all(bind=models.engine)  # Create all tables
    yield  # This will allow the tests to run
    models.Base.metadata.drop_all(bind=models.engine)  # Tear down after tests

def test_create_course():
    """Test the creation of a new course with valid data."""
    response = client.post("/courses/", json={"name": "Mathematics 101", "level": "Beginner"})
    assert response.status_code == 201  # Check if the status is Created
    assert response.json() == {"message": "Course created successfully."}

def test_create_course_with_missing_name():
    """Test the creation of a course with missing name."""
    response = client.post("/courses/", json={"level": "Intermediate"})
    assert response.status_code == 400  # Check for Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Course name is required."}}

def test_create_course_with_invalid_level():
    """Test the creation of a course with invalid level."""
    response = client.post("/courses/", json={"name": "Physics 101", "level": "Unknown"})
    assert response.status_code == 400  # Check for Bad Request
    assert response.json() == {"error": {"code": "E002", "message": "Invalid course level."}}

def test_get_courses():
    """Test retrieving all courses."""
    # First, create a couple of courses
    client.post("/courses/", json={"name": "Chemistry 101", "level": "Beginner"})
    client.post("/courses/", json={"name": "Biology 101", "level": "Intermediate"})

    response = client.get("/courses/")
    assert response.status_code == 200  # Check if the status is OK
    courses = response.json()
    assert len(courses) == 2  # Ensure we have two courses
    assert courses[0]["name"] in ["Chemistry 101", "Biology 101"]
    assert courses[1]["name"] in ["Chemistry 101", "Biology 101"]
```