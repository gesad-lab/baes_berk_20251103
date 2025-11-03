```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    # Code for creating the test database schema can be added here.
    yield
    # Code for tearing down the database can be added here.

def test_create_course_success(setup_db):
    """Test successful creation of a course."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_retrieve_course_success(setup_db):
    """Test retrieval of existing course details by ID."""
    response = client.get("/courses/1")  # Assuming a course with ID 1 exists
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] is not None
    assert response.json()["level"] is not None

def test_create_course_missing_name(setup_db):
    """Test creating a course without a name."""
    response = client.post("/courses", json={"level": "Intermediate"})
    assert response.status_code == 400  # Expecting bad request
    assert response.json() == {"error": {"code": "E001", "message": "Course name is required.", "details": {}}}

def test_create_course_missing_level(setup_db):
    """Test creating a course without a level."""
    response = client.post("/courses", json={"name": "Science"})
    assert response.status_code == 400  # Expecting bad request
    assert response.json() == {"error": {"code": "E002", "message": "Course level is required.", "details": {}}}

def test_database_migration(setup_db):
    """Test that the new Course table is created and existing Students remain unchanged."""
    # Here you will need some logic to verify the integrity of the database
    pass  # Placeholder for actual migration testing logic
```