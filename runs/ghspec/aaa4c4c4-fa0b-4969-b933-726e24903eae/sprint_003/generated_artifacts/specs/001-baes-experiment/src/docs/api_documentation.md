---
# Updated Integration Tests for Course API
File: tests/integration/test_course_integration.py

import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py

# Initialize the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the database for Course tests."""
    # Usually includes creating a test database or migrating the schema.
    pass

@pytest.fixture(scope="module")
def create_course():
    """Fixture to create a course for testing purposes."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201  # Ensure the course is created successfully
    return response.json()  # Return the created course details

def test_create_course_success(setup_database):
    """Test creating a valid course should return the course details."""
    response = client.post("/courses", json={"name": "Science", "level": "Advanced"})
    assert response.status_code == 201
    assert "id" in response.json()  # Ensure the returned course has an ID
    assert response.json()["name"] == "Science"
    assert response.json()["level"] == "Advanced"

def test_create_course_missing_name(setup_database):
    """Test creating a course without a name should return an error."""
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400  # Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Course name is required."}}

def test_create_course_missing_level(setup_database):
    """Test creating a course without a level should return an error."""
    response = client.post("/courses", json={"name": "Physics"})
    assert response.status_code == 400  # Bad Request
    assert response.json() == {"error": {"code": "E002", "message": "Course level is required."}}

def test_get_course_success(create_course):
    """Test retrieving an existing course should return its details."""
    course_id = create_course["id"]
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json() == create_course  # Check the returned data matches what we created

def test_get_non_existent_course():
    """Test retrieving a non-existent course should return a 404 error."""
    response = client.get("/courses/9999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Course not found."}}
   
def test_integration_with_students(setup_database, create_course):
    """Test that student records remain untouched during course integration."""
    # Implementation of this test would require ensuring that creating or retrieving courses does not affect student records
    pass
