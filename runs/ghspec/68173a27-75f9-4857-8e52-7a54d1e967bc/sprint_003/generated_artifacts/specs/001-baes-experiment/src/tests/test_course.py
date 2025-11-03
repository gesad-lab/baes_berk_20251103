import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.course import Course
from src.services.course_service import create_course
from src.repositories.course_repository import get_courses

client = TestClient(app)

# Sample test data for valid and invalid courses
valid_course_data = {
    "title": "Introduction to Python",
    "description": "A comprehensive course on Python programming."
}

invalid_course_data_no_title = {
    "description": "A comprehensive course on Python programming."
}

invalid_course_data_empty_title = {
    "title": "",
    "description": "A comprehensive course on Python programming."
}

@pytest.fixture
def setup_courses():
    # Setup: Clear existing courses data before each test
    yield  # This would be a good point to insert any pre-test setup code
    # Teardown: Clear courses data after tests (if needed)

def test_create_course_with_valid_data(setup_courses):
    response = client.post("/courses", json=valid_course_data)
    assert response.status_code == 201  # Check that the course is created successfully
    assert response.json() == {"title": "Introduction to Python", "description": "A comprehensive course on Python programming."}  # Adjust as per actual response structure

def test_create_course_with_missing_title(setup_courses):
    response = client.post("/courses", json=invalid_course_data_no_title)
    assert response.status_code == 422  # Unprocessable Entity expected due to missing title

def test_create_course_with_empty_title(setup_courses):
    response = client.post("/courses", json=invalid_course_data_empty_title)
    assert response.status_code == 422  # Unprocessable Entity expected due to empty title

def test_get_courses(setup_courses):
    # First create a course
    client.post("/courses", json=valid_course_data)
    
    # Now fetch the list of courses
    response = client.get("/courses")
    assert response.status_code == 200  # Check successful retrieval
    assert len(response.json()) > 0  # Ensure at least one course is returned

def test_get_course_detail(setup_courses):
    # Create a course to retrieve
    response = client.post("/courses", json=valid_course_data)
    course_id = response.json().get("id")

    # Fetch the detail of the created course
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200  # Check successful retrieval
    assert response.json()["title"] == valid_course_data["title"]
    assert response.json()["description"] == valid_course_data["description"]