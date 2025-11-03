```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app import app
from src.db import get_db
from src.models import Base, Student, Course  # Importing required models for testing

# Setting up the test database in memory
@pytest.fixture(scope="module")
def test_db():
    # Create a new SQLite database in memory
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)  # Create all tables

    # Use a session for the test
    connection = engine.connect()
    transaction = connection.begin()
    testing_session = sessionmaker(bind=connection)()

    # Override the get_db dependency to use the testing session
    app.dependency_overrides[get_db] = lambda: testing_session

    yield testing_session  # This is where the tests will run

    testing_session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(test_db):
    # Create a TestClient using the FastAPI app
    with TestClient(app) as client:
        yield client

def test_associate_student_with_course(client, test_db):
    # Create a new student
    student = Student(name="John Doe")
    test_db.add(student)
    test_db.commit()
    test_db.refresh(student)  # Refresh to get the new student ID

    # Create a new course
    course = Course(name="Math 101")
    test_db.add(course)
    test_db.commit()
    test_db.refresh(course)  # Refresh to get the new course ID

    # Associate the student with the course
    response = client.post(f"/students/{student.id}/courses/{course.id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Course associated successfully"}

def test_get_student_courses(client, test_db):
    # Create a new student
    student = Student(name="Jane Doe")
    test_db.add(student)
    test_db.commit()
    test_db.refresh(student)

    # Create a new course
    course = Course(name="Science 101")
    test_db.add(course)
    test_db.commit()
    test_db.refresh(course)

    # Associate the student with the course
    client.post(f"/students/{student.id}/courses/{course.id}")

    # Retrieve the student's courses
    response = client.get(f"/students/{student.id}/courses")
    assert response.status_code == 200
    assert len(response.json()) == 1  # Verify one course is returned
    assert response.json()[0]["name"] == "Science 101"

def test_associate_student_invalid_course(client, test_db):
    # Create a new student
    student = Student(name="Alice")
    test_db.add(student)
    test_db.commit()
    test_db.refresh(student)

    # Attempt to associate the student with a non-existing course
    response = client.post(f"/students/{student.id}/courses/999")
    assert response.status_code == 404  # Check for not found
    assert response.json() == {"error": {"code": "E002", "message": "Invalid course ID", "details": {}}}
```