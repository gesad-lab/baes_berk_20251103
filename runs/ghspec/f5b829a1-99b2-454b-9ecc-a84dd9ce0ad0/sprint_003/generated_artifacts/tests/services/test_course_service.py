```python
import pytest
from fastapi.testclient import TestClient
from src.services.course_service import CourseService
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the in-memory database for testing."""
    # Setup logic to create required tables and seed initial data if necessary
    yield
    # Cleanup logic if necessary

def test_create_course_success(setup_database):
    """Test creating a course with valid name and level."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_create_course_missing_name(setup_database):
    """Test creating a course without a name returns an error."""
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Name field is required."}

def test_create_course_missing_level(setup_database):
    """Test creating a course without a level returns an error."""
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Level field is required."}

def test_retrieve_course_success(setup_database):
    """Test retrieving an existing course by ID."""
    # Assume a course with ID 1 exists from the setup; adjust if necessary
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_retrieve_non_existent_course(setup_database):
    """Test retrieving a non-existent course ID returns a 404."""
    response = client.get("/courses/999")  # Assuming this ID does not exist
    assert response.status_code == 404
    assert response.json() == {"detail": "Course not found."}
```