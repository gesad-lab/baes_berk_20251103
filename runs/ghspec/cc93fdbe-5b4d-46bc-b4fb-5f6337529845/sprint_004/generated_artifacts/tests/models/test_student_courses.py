import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Base, StudentCourses  # Import the StudentCourses model

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database for isolated tests
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_db():
    """Set up the database for testing."""
    Base.metadata.create_all(bind=engine)  # Create the test database schema
    yield    
    Base.metadata.drop_all(bind=engine)  # Tear down database after tests

def test_student_courses_creation_success(setup_db):
    """Test successful creation of a StudentCourses entry."""
    # Create a student and a course for testing
    client.post("/students", json={"name": "John Doe"})  # Sample student creation
    client.post("/courses", json={"name": "Math 101", "level": "Beginner"})  # Sample course creation

    response = client.post("/student_courses", json={"student_id": 1, "course_id": 1})  # Adjust based on actual IDs
    assert response.status_code == 201
    assert response.json() == {"student_id": 1, "course_id": 1}

def test_student_courses_creation_invalid_student(setup_db):
    """Test creating StudentCourses entry with an invalid student ID."""
    # Attempt to add a course with a non-existent student ID
    response = client.post("/student_courses", json={"student_id": 999, "course_id": 1})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid student ID"}}  # Adjust based on actual error response

def test_student_courses_creation_invalid_course(setup_db):
    """Test creating StudentCourses entry with an invalid course ID."""
    # Attempt to add a course with a non-existent course ID
    response = client.post("/student_courses", json={"student_id": 1, "course_id": 999})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid course ID"}}  # Adjust based on actual error response

def test_student_courses_creation_missing_parameters(setup_db):
    """Test creating StudentCourses entry with missing parameters."""
    response = client.post("/student_courses", json={"student_id": 1})  # Missing course_id
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "course_id"], "msg": "field required", "type": "value_error.missing"}]}  # Adjust based on actual error response