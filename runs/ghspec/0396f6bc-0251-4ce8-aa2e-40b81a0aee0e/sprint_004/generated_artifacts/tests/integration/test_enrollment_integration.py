```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from models import Base, Student, Course, StudentCourses  # Import models including StudentCourses
from your_app import app  # Import the FastAPI application

# Setup for SQLite in-memory database for testing
@pytest.fixture(scope='module')
def test_database():
    # Create a new SQLite database (in-memory)
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create all tables
    connection = engine.connect()
    
    # Create a new session
    session = sessionmaker(bind=engine)()
    
    yield session  # This will be the test session
    
    session.close()  # Cleanup the session
    connection.close()  # Close the connection


@pytest.fixture(scope='module')
def client(test_database):
    # Create a TestClient for the FastAPI app
    with TestClient(app) as client:
        yield client


def test_enroll_student(client, test_database):
    # Create a Student and Course for testing
    student_data = {"name": "John Doe", "email": "john.doe@example.com"}
    course_data = {"title": "Introduction to Python", "description": "Learn the basics of Python."}
    
    # Add a student to the database
    response = client.post("/students/", json=student_data)
    assert response.status_code == 201  # Check that student is created successfully
    
    # Add a course to the database
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 201  # Check that course is created successfully
    
    # Enroll the student in the course
    enroll_response = client.post("/enrollments/", json={"student_id": 1, "course_id": 1})  # Assuming IDs are 1
    assert enroll_response.status_code == 200  # Check successful enrollment
    assert enroll_response.json() == {"message": "Student enrolled successfully."}  # Validate response


def test_retrieve_courses(client, test_database):
    # Retrieve courses for a student
    response = client.get("/students/1/courses/")  # Assuming we're checking for student ID 1
    assert response.status_code == 200  # Check retrieval success
    assert isinstance(response.json(), list)  # Ensure the response is a list
```
