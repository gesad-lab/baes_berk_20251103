```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is initialized in `main.py`
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from models import Course, Student, StudentCourse  # Assuming Student and StudentCourse models have been defined
import json

# Initialize the test client
client = TestClient(app)

# Setup a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    # Create a new database session for a test
    connection = engine.connect()
    transaction = connection.begin()

    # Create the tables
    Base.metadata.create_all(bind=engine)

    yield TestingSessionLocal()  # This will be the session used for tests

    # Rollback and close connections after tests
    transaction.rollback()
    connection.close()

def test_student_enrollment(db):
    # Create a student for testing
    new_student = Student(name="John Doe", email="john.doe@example.com")
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    # Create a course for testing
    new_course = Course(title="Biology 101", description="Intro to Biology")
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    # Enroll the student in the course
    enrollment_response = client.post(
        "/enroll",  # Assuming /enroll is the endpoint for enrolling students
        json={"student_id": new_student.id, "course_id": new_course.id}
    )
    
    # Check response status code
    assert enrollment_response.status_code == 200
    assert enrollment_response.json() == {"message": "Enrolled successfully"}

    # Check the database for enrollment
    enrollment = db.query(StudentCourse).filter_by(student_id=new_student.id, course_id=new_course.id).first()
    assert enrollment is not None

def test_enrollment_invalid_student(db):
    # Attempt to enroll in a course with an invalid student ID
    response = client.post(
        "/enroll",  # Assuming /enroll is the endpoint for enrolling students
        json={"student_id": 9999, "course_id": 1}  # Invalid student ID
    )
    
    # Check response status code
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Student not found"}}

def test_enrollment_invalid_course(db):
    # Create a student for testing
    new_student = Student(name="Jane Doe", email="jane.doe@example.com")
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    # Attempt to enroll in a non-existent course
    response = client.post(
        "/enroll",  # Assuming /enroll is the endpoint for enrolling students
        json={"student_id": new_student.id, "course_id": 9999}  # Invalid course ID
    )
    
    # Check response status code
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Course not found"}}
```