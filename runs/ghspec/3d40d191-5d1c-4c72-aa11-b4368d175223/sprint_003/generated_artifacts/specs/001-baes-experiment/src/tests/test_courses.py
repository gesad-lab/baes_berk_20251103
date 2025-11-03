```python
import pytest
from fastapi.testclient import TestClient
from src.api import app  # Import your FastAPI app instance

@pytest.fixture()
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

def test_create_course(client):
    """Test creating a course with valid name and level."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_create_course_missing_name(client):
    """Test creating a course without a name returns an error."""
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Name field is required."

def test_create_course_missing_level(client):
    """Test creating a course without a level returns an error."""
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Level field is required."

def test_retrieve_courses(client):
    """Test retrieving a list of courses."""
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list
```
