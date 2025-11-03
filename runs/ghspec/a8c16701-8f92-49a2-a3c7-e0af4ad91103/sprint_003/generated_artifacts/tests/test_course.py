```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app import app
from src.models import Base, Course

# Setting up the test database in memory
@pytest.fixture(scope="module")
def test_db():
    # Create a new SQLite database in memory
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    yield  # This is where the tests will run

    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client(test_db):
    # Create a TestClient for the FastAPI app
    with TestClient(app) as client:
        yield client

def test_create_course(client):
    """Test the creation of a new course."""
    response = client.post(
        "/courses/",
        json={"name": "Mathematics", "level": "Beginner"}
    )
    assert response.status_code == 201
    course = response.json()
    assert "id" in course
    assert course["name"] == "Mathematics"
    assert course["level"] == "Beginner"

def test_retrieve_course(client):
    """Test retrieving the created course using its ID."""
    # First create a new course to retrieve
    create_response = client.post(
        "/courses/",
        json={"name": "Science", "level": "Intermediate"}
    )
    course_id = create_response.json()["id"]

    retrieve_response = client.get(f"/courses/{course_id}")
    assert retrieve_response.status_code == 200
    course = retrieve_response.json()
    assert course["id"] == course_id
    assert course["name"] == "Science"
    assert course["level"] == "Intermediate"

def test_create_course_without_fields(client):
    """Test error handling for creating a course without required fields."""
    response = client.post("/courses/", json={})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "field required",
                "type": "value_error.missing"
            },
            {
                "loc": ["body", "level"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_database_migration_integrity(client):
    """Test that existing data in Student entity remains unaffected."""
    # Assuming there's a pre-existing Student entity
    response = client.get("/students/")
    # Validate that the student data still exists (Implementation depends on the actual endpoints and structure)
    assert response.status_code == 200
    students = response.json()
    assert len(students) > 0  # Check that there are students in the response
```