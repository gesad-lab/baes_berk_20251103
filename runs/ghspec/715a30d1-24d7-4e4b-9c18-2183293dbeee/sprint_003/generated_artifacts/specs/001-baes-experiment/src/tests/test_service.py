```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is initialized in `main.py`
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from models import Course  # Assuming Course model has been defined
import json

# Initialize the test client
client = TestClient(app)

# Setup a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a new version of the database for testing
def setup_module(module):
    """Run once before all tests in the module to set up database"""
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    """Run once after all tests in the module to drop database"""
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db():
    """Create a new database session for a test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)

    yield session  # This is where the testing happens

    session.close()
    transaction.rollback()
    connection.close()

def test_create_course(db):
    """Test that a course can be created successfully"""
    response = client.post(
        "/courses/", 
        json={"name": "Test Course", "description": "A course for testing."}
    )
    
    assert response.status_code == 201  # Expecting a successful creation response
    created_course = response.json()
    assert created_course["name"] == "Test Course"
    assert created_course["description"] == "A course for testing."

def test_get_courses(db):
    """Test that courses can be retrieved"""
    # First create a course so that we have data to retrieve
    client.post(
        "/courses/", 
        json={"name": "Test Course", "description": "A course for testing."}
    )
    
    response = client.get("/courses/")
    
    assert response.status_code == 200  # Expecting a successful retrieval response
    courses = response.json()
    assert isinstance(courses, list)
    assert len(courses) > 0
    assert courses[0]["name"] == "Test Course"

def test_create_course_invalid_data(db):
    """Test invalid course creation"""
    response = client.post(
        "/courses/", 
        json={"name": "", "description": "Missing course name."}  # Invalid name
    )
    
    assert response.status_code == 422  # Expecting validation error
    assert "detail" in response.json()
```
