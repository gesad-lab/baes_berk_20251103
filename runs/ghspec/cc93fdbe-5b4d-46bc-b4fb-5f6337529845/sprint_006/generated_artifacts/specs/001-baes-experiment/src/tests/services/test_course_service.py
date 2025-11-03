```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Base, Course, Teacher  # Importing Course and Teacher models

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database for isolated tests
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database schema for tests
@pytest.fixture(scope="module")
def setup_database():
    # Create the database tables before tests
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

def test_assign_teacher_success(setup_database):
    # Arrange: Create a course and a teacher in the database
    with SessionLocal() as session:
        teacher = Teacher(name="John Doe")
        session.add(teacher)
        session.commit()
        course = Course(title="Math 101", teacher_id=None)  # Initially no teacher assigned
        session.add(course)
        session.commit()
        session.refresh(course)

    # Act: Assign the teacher to the course using the API
    response = client.patch(f"/courses/{course.id}", json={"teacher_id": teacher.id})

    # Assert: Check if the response is successful and the teacher_id is updated
    assert response.status_code == 200
    assert response.json()["teacher_id"] == teacher.id

def test_assign_teacher_invalid_course_id(setup_database):
    # Act: Attempt to assign a teacher to a non-existent course ID
    response = client.patch("/courses/999", json={"teacher_id": 1})  # Assuming teacher_id 1 is valid
    # Assert: Verify that the system returns the expected error message
    assert response.status_code == 404
    assert response.json()["detail"] == "Course not found"

def test_assign_teacher_invalid_teacher_id(setup_database):
    # Arrange: Create a course in the database
    course = Course(title="Math 101")
    with SessionLocal() as session:
        session.add(course)
        session.commit()
        session.refresh(course)

    # Act: Attempt to assign a non-existent teacher ID
    response = client.patch(f"/courses/{course.id}", json={"teacher_id": 999})

    # Assert: Verify that the system returns the expected error message
    assert response.status_code == 400
    assert response.json()["detail"] == "Teacher not found"
```