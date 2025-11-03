```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Base, Course  # Assuming the new Course model is in models.py

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_db():
    # Create the database schema
    Base.metadata.create_all(bind=engine)  
    # Optionally, prepopulate with test data if needed
    yield
    # Tear down the database
    Base.metadata.drop_all(bind=engine)

def test_create_course_success(setup_db):
    """Test successful creation of a course."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_retrieve_course_information(setup_db):
    """Test retrieval of an existing course's details."""
    # First, create a course to retrieve
    client.post("/courses", json={"name": "Science", "level": "Intermediate"})
    response = client.get("/courses/1")  # Assuming this is the ID of the course created
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Science"
    assert response.json()["level"] == "Intermediate"

def test_handle_missing_course_inputs(setup_db):
    """Test handling of missing inputs when creating a course."""
    response = client.post("/courses", json={"name": "Literature"})
    assert response.status_code == 422  # HTTP status code for unprocessable entity
    assert "level" in response.json()["detail"][0]["loc"]

    response = client.post("/courses", json={"level": "Advanced"})
    assert response.status_code == 422
    assert "name" in response.json()["detail"][0]["loc"]

def test_database_migration(setup_db):
    """Test that the database migration preserves existing data."""
    # Assume there are already existing students in the database, and check their integrity
    # Create a sample student before the migration check if needed
    # This function can be tailored based on how existing student data is setup
    response = client.post("/students", json={"name": "John Doe", "age": 20})  
    assert response.status_code == 201

    # Verify that student data persists
    student_response = client.get("/students/1")  # Assuming this is the ID of the student created
    assert student_response.status_code == 200
    assert student_response.json()["name"] == "John Doe"
```
