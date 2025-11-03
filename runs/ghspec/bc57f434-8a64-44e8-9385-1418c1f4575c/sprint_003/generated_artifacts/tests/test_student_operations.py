```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py
from src.models import Course  # Assuming a Course model now exists in src/models.py
from src.database import SessionLocal  # Assuming a SessionLocal is defined for DB access

# Fixture to create a test client
@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

# Fixture to setup database for testing
@pytest.fixture(scope="module")
def setup_database():
    db = SessionLocal()  # Create a new test database session
    # Here we can add any setup logic for our course model if necessary
    yield db
    db.close()  # Ensure the DB session is closed after tests

def test_create_course_with_valid_data(test_client):
    """Test creating a course with valid name and level."""
    response = test_client.post("/courses", json={"name": "Intro to Programming", "level": "Beginner"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data  # Check that an ID is returned
    assert data["name"] == "Intro to Programming"
    assert data["level"] == "Beginner"

def test_get_course(test_client):
    """Test retrieving a course by ID."""
    # First, we will create a course to retrieve
    create_response = test_client.post("/courses", json={"name": "Data Science", "level": "Intermediate"})
    course_id = create_response.json()["id"]
    
    # Now retrieve the course
    response = test_client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == course_id
    assert data["name"] == "Data Science"
    assert data["level"] == "Intermediate"

def test_create_course_missing_name(test_client):
    """Test creating a course without a name returns error."""
    response = test_client.post("/courses", json={"level": "Advanced"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Field 'name' is required.",
            "details": {}
        }
    }

def test_create_course_missing_level(test_client):
    """Test creating a course without a level returns error."""
    response = test_client.post("/courses", json={"name": "Web Development"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Field 'level' is required.",
            "details": {}
        }
    }

def test_create_course_invalid_data_type(test_client):
    """Test creating a course with invalid data types returns error."""
    response = test_client.post("/courses", json={"name": 123, "level": True})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Invalid data type for fields.",
            "details": {}
        }
    }
```