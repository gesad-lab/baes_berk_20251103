```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from api.courses import router as course_router
from database.db import init_db

# Set up FastAPI app for testing
app = FastAPI()
app.include_router(course_router)

@pytest.fixture(scope="module")
def client():
    """Create a test client for the FastAPI app."""
    init_db()  # Initialize the database
    yield TestClient(app)  # Provide the test client to the tests

def test_create_course_with_valid_data(client):
    """Test creating a course with valid name and level."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Advanced"})
    assert response.status_code == 201
    assert response.json()['name'] == "Mathematics"
    assert response.json()['level'] == "Advanced"

def test_create_course_without_name(client):
    """Test creating a course without a name field."""
    response = client.post("/courses", json={"level": "Advanced"})
    assert response.status_code == 400
    assert "Course name is required" in response.json()['detail']

def test_create_course_without_level(client):
    """Test creating a course without a level field."""
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert "Course level is required" in response.json()['detail']

def test_create_course_with_empty_fields(client):
    """Test creating a course with empty fields."""
    response = client.post("/courses", json={"name": "", "level": ""})
    assert response.status_code == 400
    assert "Course name cannot be empty" in response.json()['detail']
    assert "Course level cannot be empty" in response.json()['detail']

def test_create_course_with_invalid_data_type(client):
    """Test creating a course with invalid data types."""
    response = client.post("/courses", json={"name": 123, "level": 456})
    assert response.status_code == 400
    assert "Course name must be a string" in response.json()['detail']
    assert "Course level must be a string" in response.json()['detail']
```