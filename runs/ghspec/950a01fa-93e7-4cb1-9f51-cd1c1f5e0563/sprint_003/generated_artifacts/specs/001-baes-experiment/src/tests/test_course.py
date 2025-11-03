```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in src/main.py
from src.db import init_db, shutdown_db  # Assuming database initialization functions
from src.models import Course  # Assuming you have a Course model

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Set up the database for testing."""
    init_db()
    yield
    shutdown_db()

@pytest.fixture
def client():
    """Create a TestClient for testing purposes."""
    with TestClient(app) as client:
        yield client

def test_create_course_with_valid_data(client):
    """Test creating a Course with valid name and level."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Intermediate"})
    assert response.status_code == 201  # Expecting a 201 Created
    assert response.json() == {"name": "Mathematics", "level": "Intermediate", "id": response.json()["id"]}

def test_get_courses(client):
    """Test retrieving all Courses."""
    response = client.get("/courses")
    assert response.status_code == 200  # Expecting a 200 OK
    assert isinstance(response.json(), list)  # It should be a list
    # Confirm that the previously created course is included in the response
    assert any(course['name'] == "Mathematics" for course in response.json())

def test_create_course_without_name(client):
    """Test creating a Course without a name."""
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400  # Expecting a 400 Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Name is required", "details": {}}}

def test_create_course_without_level(client):
    """Test creating a Course without a level."""
    response = client.post("/courses", json={"name": "Science"})
    assert response.status_code == 400  # Expecting a 400 Bad Request
    assert response.json() == {"error": {"code": "E002", "message": "Level is required", "details": {}}}
```