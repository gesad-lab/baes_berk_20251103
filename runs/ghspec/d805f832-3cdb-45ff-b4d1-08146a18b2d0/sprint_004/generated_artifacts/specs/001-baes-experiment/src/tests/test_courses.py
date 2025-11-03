```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Course, Student, StudentCourse  # Importing necessary models
from main import app, get_db  # Importing FastAPI app and database session dependency

# SQLite database connection settings for testing
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Setting up the database for testing
@pytest.fixture(scope="module")
def test_database():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client(test_database):
    # Create a TestClient for the FastAPI app
    with TestClient(app) as c:
        yield c

@pytest.fixture
def db_session():
    # Dependency to create a new database session for individual tests
    db = TestingSessionLocal()
    yield db
    db.close()

def test_associate_course_with_student(client, db_session):
    # Create test course and student
    test_course = Course(name="Test Course", level="Beginner")
    db_session.add(test_course)
    db_session.commit()

    test_student = Student(name="Test Student")
    db_session.add(test_student)
    db_session.commit()

    response = client.post(
        f"/students/{test_student.id}/courses",
        json={"course_id": test_course.id}
    )

    assert response.status_code == 201  # Expecting a success response
    assert "Course associated successfully" in response.json()  # Assuming the message is returned in response

    # Verify the updated list of courses for the student
    student_courses_response = client.get(f"/students/{test_student.id}/courses")
    assert student_courses_response.status_code == 200
    assert len(student_courses_response.json()["courses"]) == 1  # One course should be associated

def test_associate_non_existing_course(client, db_session):
    # Create a test student without courses
    test_student = Student(name="New Student")
    db_session.add(test_student)
    db_session.commit()

    # Attempt to associate a course that does not exist
    response = client.post(
        f"/students/{test_student.id}/courses",
        json={"course_id": 999}  # Non-existing course ID
    )

    assert response.status_code == 404  # Expecting not found response
    assert response.json()["detail"] == "Course not found."  # Check the error message
```