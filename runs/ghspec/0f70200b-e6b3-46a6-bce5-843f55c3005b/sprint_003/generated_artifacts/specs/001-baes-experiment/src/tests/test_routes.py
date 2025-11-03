```python
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.models import Course

client = TestClient(app)

@pytest.fixture(scope="module")
def test_courses():
    """Setup test courses in the database before any tests run."""
    # Assume a setup function exists to clear and populate the database
    clear_and_seed_database_with_courses()
    yield
    # Tear down test database cleanup
    clear_test_database()

def test_create_course_success():
    """Test creating a course with valid data."""
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json()['name'] == "Math 101"
    assert response.json()['level'] == "Beginner"

def test_create_course_without_name():
    """Test creating a course without a name returns a validation error."""
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required.", "details": {}}}

def test_create_course_without_level():
    """Test creating a course without a level returns a validation error."""
    response = client.post("/courses", json={"name": "Math 101"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Level is required.", "details": {}}}

def test_retrieve_course_success():
    """Test retrieving a course by its ID."""
    # First create a course to retrieve
    create_response = client.post("/courses", json={"name": "Science 101", "level": "Intermediate"})
    course_id = create_response.json()['id']

    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()['name'] == "Science 101"
    assert response.json()['level'] == "Intermediate"

def test_retrieve_all_courses():
    """Test retrieving all courses from the database."""
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses
```