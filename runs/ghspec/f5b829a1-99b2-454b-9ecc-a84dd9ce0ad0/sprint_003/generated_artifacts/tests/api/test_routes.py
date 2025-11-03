```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app, get_db
from src.models import Base, Student, Course  # Ensure the Course model is imported
from src.services.course_service import CourseService  # Ensure the CourseService is imported

# Setup the test database and client
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the in-memory database for testing."""
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    # Here additional setup like populating the Student table might happen if needed

    yield  # This is where the testing occurs

    # Cleanup when done
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    """Fixture to provide a test client for FastAPI."""
    with TestClient(app) as c:
        yield c

def test_create_course_success(client, setup_database):
    """Test creating a course with valid data."""
    response = client.post("/courses", json={"name": "Math 101", "level": "beginner"})
    assert response.status_code == 201  # Check for successful creation
    assert response.json() == {"id": 1, "name": "Math 101", "level": "beginner"}  # Check course details

def test_get_course_by_id_success(client, setup_database):
    """Test retrieving a course by ID."""
    response = client.get("/courses/1")
    assert response.status_code == 200  # Check for successful retrieval
    assert response.json() == {"id": 1, "name": "Math 101", "level": "beginner"}  # Verify returned course data

def test_create_course_missing_name(client, setup_database):
    """Test error handling for missing course name."""
    response = client.post("/courses", json={"level": "beginner"})
    assert response.status_code == 400  # Check for bad request
    assert response.json() == {"error": {"code": "E001", "message": "Name field is required.", "details": {}}}

def test_create_course_missing_level(client, setup_database):
    """Test error handling for missing course level."""
    response = client.post("/courses", json={"name": "Math 101"})
    assert response.status_code == 400  # Check for bad request
    assert response.json() == {"error": {"code": "E001", "message": "Level field is required.", "details": {}}}

def test_create_course_with_empty_fields(client, setup_database):
    """Test error handling for empty course fields."""
    response = client.post("/courses", json={"name": "", "level": ""})
    assert response.status_code == 400  # Check for bad request
    assert response.json() == {"error": {"code": "E001", "message": "Name field is required.", "details": {}}}
```