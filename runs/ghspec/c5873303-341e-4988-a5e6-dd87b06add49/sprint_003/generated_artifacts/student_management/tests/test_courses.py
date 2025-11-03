```python
from fastapi import status
from fastapi.testclient import TestClient
import pytest
from src.main import app
from src.models import Course  # Import the Course model
from sqlalchemy.orm import Session

client = TestClient(app)

@pytest.fixture
def test_db_session():
    # Assume this fixture provides a test database session
    pass

def test_create_course_with_valid_data(test_db_session: Session):
    """Test successful creation of a course with valid data."""
    response = client.post(
        "/courses",
        json={"name": "Mathematics", "level": "Intermediate"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.json()
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Intermediate"


def test_retrieve_all_courses(test_db_session: Session):
    """Test retrieval of all courses."""
    # Create a course to ensure there's at least one in the database
    client.post(
        "/courses",
        json={"name": "Biology", "level": "Beginner"},
    )

    response = client.get("/courses")
    assert response.status_code == status.HTTP_200_OK
    courses = response.json()
    assert isinstance(courses, list)
    assert len(courses) > 0
    for course in courses:
        assert "id" in course
        assert "name" in course
        assert "level" in course


def test_create_course_missing_fields(test_db_session: Session):
    """Test that creating a course without required fields fails."""
    response = client.post("/courses", json={"name": "Chemistry"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"

    response = client.post("/courses", json={"level": "Advanced"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == "field required"
```