```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.course import Course
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create the database tables
    yield
    Base.metadata.drop_all(bind=engine)    # Drop the database tables after tests

def test_create_course_valid():
    """Scenario 1: Create a Course"""
    response = client.post("/courses/", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json() == {
        "name": "Mathematics",
        "level": "Beginner",
        "id": response.json()["id"]  # Expect the response to include an id
    }

def test_get_course_by_id():
    """Scenario 2: Retrieve a Course by ID"""
    # First create a course
    create_response = client.post("/courses/", json={"name": "Science", "level": "Intermediate"})
    course_id = create_response.json()["id"]

    # Now retrieve the same course by ID
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Science",
        "level": "Intermediate",
        "id": course_id
    }

def test_update_course():
    """Scenario 3: Update a Course"""
    # Create a course to be updated
    create_response = client.post("/courses/", json={"name": "History", "level": "Advanced"})
    course_id = create_response.json()["id"]

    # Update the course
    update_response = client.put(f"/courses/{course_id}", json={"name": "History", "level": "Expert"})
    assert update_response.status_code == 200
    assert update_response.json() == {
        "name": "History",
        "level": "Expert",
        "id": course_id
    }

def test_create_course_missing_fields():
    """Scenario 4: Handle Missing Required Fields"""
    # Test missing name
    response = client.post("/courses/", json={"level": "Intermediate"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Missing required field: name", "details": {}}}

    # Test missing level
    response = client.post("/courses/", json={"name": "Geography"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Missing required field: level", "details": {}}}
```