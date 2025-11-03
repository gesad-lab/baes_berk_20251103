```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Base, StudentCourses  # Assuming the StudentCourses model is in models.py

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_db():
    """Setup the test database schema."""
    # Create the database tables in the test database
    Base.metadata.create_all(bind=engine)
    
    yield
    
    # Drop the database tables after tests run
    Base.metadata.drop_all(bind=engine)

def test_create_student_course_success(setup_db):
    """Test successful creation of a student-course relationship."""
    # Precondition: Create a student and a course in the database
    response_student = client.post("/students", json={"name": "John Doe"})
    assert response_student.status_code == 201
    student_id = response_student.json()["id"]

    response_course = client.post("/courses", json={"name": "Mathematics"})
    assert response_course.status_code == 201
    course_id = response_course.json()["id"]

    # Test: Establishing student-course relationship
    response = client.post("/students/{}/courses/{}".format(student_id, course_id))
    assert response.status_code == 201
    assert response.json() == {"student_id": student_id, "course_id": course_id}

def test_create_student_course_invalid(setup_db):
    """Test failure case when trying to create a student-course relationship with invalid data."""
    # Attempting to create a relationship with non-existing IDs
    response = client.post("/students/{}/courses/{}".format(999, 999))  # Assuming 999 is invalid
    assert response.status_code == 404  # Expecting not found error

def test_get_student_courses_success(setup_db):
    """Test fetching courses for a specific student."""
    # Step 1: Create a student and a course
    response_student = client.post("/students", json={"name": "Jane Doe"})
    assert response_student.status_code == 201
    student_id = response_student.json()["id"]

    response_course = client.post("/courses", json={"name": "Physics"})
    assert response_course.status_code == 201
    course_id = response_course.json()["id"]

    # Step 2: Create relationship
    client.post("/students/{}/courses/{}".format(student_id, course_id))

    # Step 3: Get student courses
    response = client.get("/students/{}/courses".format(student_id))
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["course_id"] == course_id
```