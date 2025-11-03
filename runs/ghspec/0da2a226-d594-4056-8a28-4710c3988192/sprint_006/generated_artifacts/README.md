```python
# tests/test_course.py
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Course, Teacher
from sqlalchemy.orm import Session
from database import get_db, Base, engine

# Create the test client used for sending requests to the application
client = TestClient(app)

# Dependency override for the database session
def override_get_db():
    db = Session(bind=engine)
    yield db
    db.close()

# Setup the test database and create the necessary tables
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Create the tables in the test database
    Base.metadata.create_all(bind=engine)
    yield  # This is where the testing will happen
    # Teardown: drop the tables after tests
    Base.metadata.drop_all(bind=engine)

# Test case for creating a course with an assigned teacher
def test_create_course_with_teacher(setup_database):
    # First, create a Teacher instance in the database
    teacher = Teacher(name="John Doe")

    with Session(bind=engine) as session:
        session.add(teacher)
        session.commit()
        session.refresh(teacher)  # Refresh to get the teacher ID

    # Now, create a Course and associate it with the Teacher
    response = client.post("/courses/", json={"title": "Mathematics", "teacher_id": teacher.id})

    # Assert that the response is successful and contains the correct data
    assert response.status_code == 201
    assert response.json() == {
        "id": response.json()["id"],  # Validate that the ID matches
        "title": "Mathematics",
        "teacher_id": teacher.id
    }

# Test case for retrieving a course and ensuring it includes teacher information
def test_get_course_with_teacher(setup_database):
    # Create a Teacher first
    teacher = Teacher(name="Jane Smith")
    with Session(bind=engine) as session:
        session.add(teacher)
        session.commit()
        session.refresh(teacher)

    # Create a Course associated with the Teacher
    course = Course(title="Science", teacher_id=teacher.id)
    with Session(bind=engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)

    # Retrieve the Course by its ID
    response = client.get(f"/courses/{course.id}")

    # Assert that the course is returned correctly with teacher information
    assert response.status_code == 200
    assert response.json() == {
        "id": course.id,
        "title": "Science",
        "teacher_id": teacher.id
    }

# Test case for creating a course without a teacher
def test_create_course_without_teacher(setup_database):
    # Create a Course without an associated Teacher
    response = client.post("/courses/", json={"title": "History", "teacher_id": None})

    # Assert that the response is successful and contains the correct data
    assert response.status_code == 201
    assert response.json() == {
        "id": response.json()["id"],  # Validate that the ID matches
        "title": "History",
        "teacher_id": None
    }
```