```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.api import app  # Assuming the FastAPI app is defined in src/api
from src.models import Base, Course, Student, StudentCourses  # Import required models for testing

DATABASE_URL = "sqlite:///./test.db"

# Create a new database engine for testing
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to override the default session
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Test client for making requests to the FastAPI app
client = TestClient(app)

# Adding setup for the database
@pytest.fixture(autouse=True)
def setup_database():
    # Create the database tables before each test
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after each test
    Base.metadata.drop_all(bind=engine)

def test_enroll_student_in_course():
    # Assume we have some predefined students and courses
    student_id = 1
    course_id = 1
    response = client.post(f"/students/{student_id}/courses", json={"course_id": course_id})
    assert response.status_code == 200
    assert response.json() == {"message": "Student successfully enrolled in course."}

def test_enroll_student_with_invalid_student_id():
    course_id = 1
    response = client.post("/students/999/courses", json={"course_id": course_id})  # Invalid student ID
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Invalid student ID."}}

def test_enroll_student_with_invalid_course_id():
    student_id = 1
    response = client.post(f"/students/{student_id}/courses", json={"course_id": 999})  # Invalid course ID
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Invalid course ID."}}

def test_retrieve_enrolled_courses_for_student():
    # First, enroll a student in a course
    student_id = 1
    course_id = 1
    client.post(f"/students/{student_id}/courses", json={"course_id": course_id})
    
    # Now, retrieve the courses for the student
    response = client.get(f"/students/{student_id}/courses")
    assert response.status_code == 200
    assert response.json() == [{"course_id": course_id}]  # Assuming a simple representation

# Additional tests can be included based on requirements
```