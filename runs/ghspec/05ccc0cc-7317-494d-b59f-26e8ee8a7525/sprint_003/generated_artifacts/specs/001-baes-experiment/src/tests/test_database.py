```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Course
from app.database import engine

# Set up the test database
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)

# Test client instance for making API requests
@pytest.fixture(scope='module')
def client(test_db):
    return TestClient(app)

def test_create_course(client):
    """Test creating a course with valid data."""
    response = client.post("/courses/", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json() == {"message": "Course created successfully", "course": {"name": "Math 101", "level": "Beginner"}}

def test_create_course_without_name(client):
    """Test creating a course without a name results in an error."""
    response = client.post("/courses/", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Course name is required", "details": {}}}

def test_create_course_without_level(client):
    """Test creating a course without a level results in an error."""
    response = client.post("/courses/", json={"name": "Math 101"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Course level is required", "details": {}}}

def test_get_courses(client):
    """Test retrieving all courses returns correct data."""
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Check if the response is a list
```
