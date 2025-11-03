```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.api import app  # Assuming the FastAPI app is defined in src/api
from src.models import Base, Course  # Importing the Course model for testing

DATABASE_URL = "sqlite:///./test.db"

# Create a new database engine for testing
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Set up the FastAPI app and the test client
@pytest.fixture(scope="module")
def client():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    # Drop the database tables after tests are completed
    Base.metadata.drop_all(bind=engine)

# Test Case: Successful creation of a course
def test_create_course_success(client):
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Mathematics", "level": "Beginner"}  # Adjust as per your API response format

# Test Case: Missing 'name' field
def test_create_course_missing_name(client):
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Missing 'name' field"}}  # Adjust the error message format as necessary

# Test Case: Missing 'level' field
def test_create_course_missing_level(client):
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Missing 'level' field"}}  # Adjust the error message format as necessary

# Test Case: Missing both fields
def test_create_course_missing_both(client):
    response = client.post("/courses", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E003", "message": "Missing 'name' and 'level' fields"}}  # Adjust the error message format as necessary

# Test Case: Successful retrieval of courses
def test_get_courses_success(client):
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses
```
