```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Course
from app.database import engine

# Set up the test database for course entity tests
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema, including the Course table
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)

# Test client instance for making API requests
@pytest.fixture(scope='module')
def client(test_db):
    return TestClient(app)

def test_create_course(client):
    # Valid course data for testing
    course_data = {
        "name": "Introduction to Programming",
        "level": "undergraduate"  # Assuming this is a valid level in the system
    }
    
    response = client.post("/api/courses", json=course_data)
    
    # Verify creation response
    assert response.status_code == 201
    assert response.json()["name"] == course_data["name"]
    assert response.json()["level"] == course_data["level"]

def test_create_course_invalid_data(client):
    # Invalid course data (missing name)
    invalid_course_data = {
        "level": "undergraduate"
    }
    
    response = client.post("/api/courses", json=invalid_course_data)
    
    # Expecting a bad request due to input validation
    assert response.status_code == 400
    assert "error" in response.json()
    
def test_create_course_duplicate(client):
    # Valid course data for creating a duplicate
    course_data = {
        "name": "Introduction to Programming",
        "level": "undergraduate"
    }
    
    # Create the course the first time
    client.post("/api/courses", json=course_data)
    # Try to create the same course again
    response = client.post("/api/courses", json=course_data)
    
    # Expecting a conflict due to duplicate course
    assert response.status_code == 409
    assert "error" in response.json()
```