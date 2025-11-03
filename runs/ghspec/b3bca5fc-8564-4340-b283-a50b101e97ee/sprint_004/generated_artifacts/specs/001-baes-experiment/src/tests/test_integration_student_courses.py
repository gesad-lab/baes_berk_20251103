import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Student, Course  # Import the relevant models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base  # Assuming there's a database module for the database setup

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create a test client
client = TestClient(app)

# Create the database tables for testing
@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    # Setup initial data (students and courses)
    with TestingSessionLocal() as db:
        student = Student(name="Test Student")
        course = Course(name="Test Course")
        db.add(student)
        db.add(course)
        db.commit()
        db.refresh(student)
        db.refresh(course)
        yield
    Base.metadata.drop_all(bind=engine)

def test_enroll_student():
    # Arrange
    student_data = {"student_id": 1, "course_id": 1}  # Assuming IDs are auto-incrementing and starting from 1

    # Act
    response = client.post("/enroll_student", json=student_data)  # Adjust endpoint as necessary

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Student enrolled successfully"}

def test_get_enrolled_courses():
    # Arrange
    enrollment_data = {"student_id": 1}  # Assuming student with ID 1 is enrolled in at least one course
    client.post("/enroll_student", json={"student_id": 1, "course_id": 1})  # Ensure student is enrolled

    # Act
    response = client.get("/student_courses", params=enrollment_data)  # Adjust endpoint as necessary

    # Assert
    assert response.status_code == 200
    assert "courses" in response.json()
    assert len(response.json()["courses"]) > 0  # Ensure there are enrolled courses

def test_enroll_invalid_course():
    # Arrange
    invalid_enrollment_data = {"student_id": 1, "course_id": 9999}  # Assuming 9999 doesn't exist

    # Act
    response = client.post("/enroll_student", json=invalid_enrollment_data)

    # Assert
    assert response.status_code == 400  # Assuming bad request for invalid course
    assert response.json() == {"error": {"code": "E001", "message": "Invalid course ID"}}  # Adjust as per error handling

def test_get_courses_for_non_enrolled_student():
    # Arrange
    non_enrolled_data = {"student_id": 2}  # Assuming student with ID 2 has no enrollments

    # Act
    response = client.get("/student_courses", params=non_enrolled_data)

    # Assert
    assert response.status_code == 200
    assert response.json() == {"courses": []}  # Expecting an empty list for non-enrolled student