```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.models import Course, Teacher  # Import Course and Teacher models
from src.database import get_db

# Configure the SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def init_database():
    # Create the database tables
    from src.models import Base
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

def test_assign_teacher_to_course(test_client, init_database):
    # Given an existing course and teacher
    course = Course(id=1, name="Test Course", teacher_id=None)
    teacher = Teacher(id=1, name="Test Teacher", email="teacher@example.com")
    
    # Add course and teacher to the database
    with TestingSessionLocal() as db:
        db.add(course)
        db.add(teacher)
        db.commit()

    # When assigning the teacher to the course
    response = test_client.patch("/courses/1/assign-teacher", json={"teacher_id": 1})
    
    # Then expect a 204 No Content response
    assert response.status_code == 204

def test_assign_non_existing_teacher(test_client, init_database):
    # Given an existing course
    course = Course(id=2, name="Test Course 2", teacher_id=None)
    
    # Add course to the database
    with TestingSessionLocal() as db:
        db.add(course)
        db.commit()

    # When attempting to assign a non-existing teacher
    response = test_client.patch("/courses/2/assign-teacher", json={"teacher_id": 99})
    
    # Then expect a 400 Bad Request response
    assert response.status_code == 400
    assert response.json() == {"detail": "Teacher not found"}

def test_retrieve_course_and_check_teacher(test_client, init_database):
    # Given an existing course with a teacher assigned
    course = Course(id=3, name="Test Course 3", teacher_id=1)
    teacher = Teacher(id=1, name="Test Teacher", email="teacher@example.com")

    # Add course and teacher to the database
    with TestingSessionLocal() as db:
        db.add(course)
        db.add(teacher)
        db.commit()

    # When retrieving the course
    response = test_client.get("/courses/3")
    
    # Then expect a 200 OK response with correct teacher info
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_student_and_course_records_intact(test_client, init_database):
    # Given existing student and course records
    # This simulates the previous state of the database
    course = Course(id=4, name="Test Course 4", teacher_id=None)
    
    # Add course to the database
    with TestingSessionLocal() as db:
        db.add(course)
        db.commit()
    
    # Verify that the existing students and their records are intact
    # This can be expanded based on actual student model and its attributes
    response = test_client.get("/students")
    assert response.status_code == 200
    # Check the length or attributes of existing students (assuming a list exists)

def test_assign_multiple_teachers_to_course(test_client, init_database):
    # Given an existing course
    course = Course(id=5, name="Test Course 5", teacher_id=None)
    
    # Add course to the database
    with TestingSessionLocal() as db:
        db.add(course)
        db.commit()

    # When trying to assign a different teacher after a first assignment
    # First assignment
    response_first_assign = test_client.patch("/courses/5/assign-teacher", json={"teacher_id": 1})
    assert response_first_assign.status_code == 204

    # Second assignment attempt
    response_second_assign = test_client.patch("/courses/5/assign-teacher", json={"teacher_id": 2})
    
    # Then expect a 400 Bad Request response
    assert response_second_assign.status_code == 400
    assert response_second_assign.json() == {"detail": "Each course can only have one assigned teacher"}
```