```python
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Course
from sqlalchemy.orm import Session
from database import get_db, Base, engine

# Create the test client used for sending requests to the application
client = TestClient(app)

# Dependency override for the database session
def override_get_db():
    db = Session(bind=engine)
    yield db
    db.close()

# Setup the test database and create the necessary tables
@pytest.fixture(scope="module", autouse=True)
def test_db():
    Base.metadata.create_all(engine)  # Create all tables
    yield
    Base.metadata.drop_all(engine)  # Clean up after tests are complete

# Test case for creating a course
def test_create_course():
    response = client.post("/courses/", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Mathematics"
    assert data["level"] == "Beginner"

    # Verify that the course can be retrieved
    course_response = client.get(f"/courses/{data['id']}")
    assert course_response.status_code == 200
    course_data = course_response.json()
    assert course_data["name"] == "Mathematics"
    assert course_data["level"] == "Beginner"

# Test case for attempting to create a course without required fields
def test_create_course_without_level():
    response = client.post("/courses/", json={"name": "Science"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "level"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

# Test case for attempting to create a course with an invalid level
def test_create_course_with_invalid_level():
    response = client.post("/courses/", json={"name": "History", "level": "UnknownLevel"})
    assert response.status_code == 400  # Bad Request
    assert response.json() == {
        "detail": "Invalid level provided"
    }
```