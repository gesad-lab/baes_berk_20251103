```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app import app
from src.db import get_db
from src.models import Base, Student, Course  # Import new Course model

# Setting up the test database in memory
@pytest.fixture(scope="module")
def test_db():
    # Create a new SQLite database in memory
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)  # Create all tables (Student, Course)

    # Create a new session for testing
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    yield TestingSessionLocal()  # Provide the session to the test functions

    # Cleanup after tests
    Base.metadata.drop_all(bind=engine)

# Create a TestClient instance for testing FastAPI endpoints
@pytest.fixture(scope="module")
def client(test_db):
    app.dependency_overrides[get_db] = lambda: test_db
    with TestClient(app) as c:
        yield c  # Provide the client to the test functions

# Test Case: Create a New Course
def test_create_course(client):
    response = client.post("/courses/", json={"name": "Mathematics", "level": "Advanced"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Mathematics"
    assert data["level"] == "Advanced"

# Test Case: Retrieve Course Information
def test_get_course(client):
    # First, create a course to retrieve
    create_response = client.post("/courses/", json={"name": "Physics", "level": "Intermediate"})
    course_id = create_response.json()["id"]
    
    response = client.get(f"/courses/{course_id}/")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == course_id
    assert data["name"] == "Physics"
    assert data["level"] == "Intermediate"

# Test Case: Error Handling for Missing Fields
def test_create_course_missing_fields(client):
    response = client.post("/courses/", json={"name": ""})  # Missing level
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "level"], "msg": "field required", "type": "value_error.missing"}]}

    response = client.post("/courses/", json={"level": ""})  # Missing name
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"}]}

# Test Case: Database Migration Integrity
def test_student_records_unchanged(client):
    # First, insert a Student record before adding Course table
    response = client.post("/students/", json={"name": "John Doe", "age": 20})  # Assuming this endpoint exists
    student_id = response.json()["id"]
    
    # Create a new course
    client.post("/courses/", json={"name": "Chemistry", "level": "Beginner"})
    
    # Fetch the existing student and check if the record is unchanged
    response = client.get(f"/students/{student_id}/")  # Assuming this endpoint exists
    assert response.status_code == 200
    student_data = response.json()
    assert student_data["id"] == student_id
    assert student_data["name"] == "John Doe"
    assert student_data["age"] == 20  # Verify no change
```