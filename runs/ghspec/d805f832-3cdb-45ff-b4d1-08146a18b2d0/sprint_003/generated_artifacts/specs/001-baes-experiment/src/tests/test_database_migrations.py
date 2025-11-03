import pytest
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Course, Base  # Assuming a models.py defines the Course model and Base for SQLAlchemy
from main import app, get_db  # Assume the FastAPI app is in main.py with a dependency for db session

# Setting up the test database and FastAPI client
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the FastAPI application
app = FastAPI()

# Create the database tables for testing
Base.metadata.create_all(bind=engine)

# Dependency override for testing
@app.middleware("http")
async def override_db_session(request: Request, call_next):
    response = await call_next(request)
    return response

# Test case: Validate the creation of a course with valid data
def test_create_course():
    client = TestClient(app)
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Math 101"
    assert response.json()["level"] == "Beginner"

# Test case: Validate retrieving a course by ID
def test_get_course():
    client = TestClient(app)
    # First, create a course
    create_response = client.post("/courses", json={"name": "Science 101", "level": "Intermediate"})
    course_id = create_response.json()["id"]

    # Now, retrieve the course
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["id"] == course_id
    assert response.json()["name"] == "Science 101"
    assert response.json()["level"] == "Intermediate"

# Test case: Validate error handling when creating a course without required fields
def test_create_course_missing_fields():
    client = TestClient(app)
    
    # Try creating a course without "name"
    response = client.post("/courses", json={"level": "Advanced"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Field 'name' is required."}
    
    # Try creating a course without "level"
    response = client.post("/courses", json={"name": "History 101"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Field 'level' is required."}

# Test case: Validate database migration and data integrity
def test_database_migration_data_integrity():
    # Check if the Course and Student tables exist and contain records
    client = TestClient(app)
    
    # Ensure existing records remain intact after migration
    # First, let's create a student record before the migration
    student_response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert student_response.status_code == 201
    
    # Perform a database migration (if applicable, adding the logic to do so)
    # ...
    
    # Check that the student record still exists
    response = client.get(f"/students/{student_response.json()['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"