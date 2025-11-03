import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Course  # Assuming a models.py defines the Course model and Base for SQLAlchemy
from main import app, get_db  # Assume the FastAPI app and db session dependency are in main.py

# SQLite database connection settings for testing
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override to use the test database session
app.dependency_overrides[get_db] = lambda: TestingSessionLocal()

# Setup the test database before tests are run
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the tables after tests are completed
    Base.metadata.drop_all(bind=engine)

# Test client for making requests to the FastAPI app
client = TestClient(app)

def test_create_course():
    """Test creating a course with valid fields."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Advanced"})
    assert response.status_code == 201  # Check for successful creation
    data = response.json()
    assert "id" in data
    assert data["name"] == "Mathematics"
    assert data["level"] == "Advanced"

def test_retrieve_course():
    """Test retrieving a course by ID."""
    response = client.post("/courses", json={"name": "Science", "level": "Intermediate"})
    created_course = response.json()
    
    course_id = created_course["id"]
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200  # Check for successful retrieval
    data = response.json()
    assert data["id"] == course_id
    assert data["name"] == "Science"
    assert data["level"] == "Intermediate"

def test_create_course_missing_fields():
    """Test creating a course with missing required fields."""
    response = client.post("/courses", json={"name": "History"})  # Missing level
    assert response.status_code == 422  # Check for validation error
    assert response.json() == {"detail": [{"loc": ["body", "level"], "msg": "field required", "type": "value_error.missing"}]} 

    response = client.post("/courses", json={"level": "Beginner"})  # Missing name
    assert response.status_code == 422  # Check for validation error
    assert response.json() == {"detail": [{"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"}]} 