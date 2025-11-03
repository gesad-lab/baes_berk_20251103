from fastapi.testclient import TestClient
import pytest
from src.api.course import router as course_router  # Importing the course router
from models.course import Course  # Assuming Course is defined in models
from sqlalchemy.orm import Session
from database import get_db  # Assuming this is how we get a database session

# Create a FastAPI app instance and include the course router
app = FastAPI()
app.include_router(course_router)

# Fixture for the test client
@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

# Test scenario: Create a course
def test_create_course(test_client: TestClient):
    response = test_client.post("/courses", json={"name": "Mathematics", "level": "Introductory"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Mathematics"
    assert data["level"] == "Introductory"

# Test scenario: Retrieve courses
def test_retrieve_courses(test_client: TestClient):
    response = test_client.get("/courses")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Response should be a list
    assert len(data) > 0  # Assuming at least one course exists

# Test scenario: Error handling on missing fields
def test_create_course_missing_fields(test_client: TestClient):
    response = test_client.post("/courses", json={})
    assert response.status_code == 422  # Unprocessable Entity status code
    assert "detail" in response.json()  # Error details should be present

# Test scenario: Error handling on validation
def test_create_course_validation_error(test_client: TestClient):
    response = test_client.post("/courses", json={"name": 123, "level": "Beginner"})
    assert response.status_code == 422  # Unprocessable Entity status code
    assert "detail" in response.json()  # Error details for validation issues should be present