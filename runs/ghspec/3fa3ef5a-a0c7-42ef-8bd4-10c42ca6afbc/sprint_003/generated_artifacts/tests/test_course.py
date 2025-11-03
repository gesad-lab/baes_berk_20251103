import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming FastAPI app is created in main.py
from src.services.course_service import CourseService
from src.models.course import Course

client = TestClient(app)

@pytest.fixture
def create_course():
    """Fixture to create a course entry before tests."""
    course_data = {"name": "Mathematics", "level": "Beginner"}
    response = client.post("/courses", json=course_data)
    return response.json()

def test_create_course_success():
    """Test case for successful course creation."""
    response = client.post("/courses", json={"name": "Physics", "level": "Intermediate"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Physics"
    assert response.json()["level"] == "Intermediate"

def test_create_course_missing_fields():
    """Test case for course creation with missing fields."""
    response = client.post("/courses", json={"name": "Chemistry"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "level"], "msg": "field required", "type": "value_error.missing"}]}

def test_create_course_invalid_data_type():
    """Test case for course creation with invalid data types."""
    response = client.post("/courses", json={"name": 123, "level": "Advanced"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "name"], "msg": "str type expected", "type": "type_error.str"}]}

def test_retrieve_course_success(create_course):
    """Test case for successfully retrieving a course."""
    course_id = create_course["id"]
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json() == create_course

def test_retrieve_non_existent_course():
    """Test case for retrieving a non-existent course."""
    response = client.get("/courses/99999")  # Assuming this ID does not exist
    assert response.status_code == 404  # Not Found
    assert response.json() == {"detail": "Course not found."}

# You could add more tests here following the scenarios outlined in the specification.