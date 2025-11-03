# tests/test_course.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Course, Teacher
from app.database import engine
from sqlalchemy.orm import Session
from app.schemas import CourseCreate


# Set up the test database
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema
    from app.models import Base
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def test_teacher(test_db):
    # Create a teacher for testing
    teacher = Teacher(name="John Doe")
    with Session(engine) as session:
        session.add(teacher)
        session.commit()
        session.refresh(teacher)
    return teacher


@pytest.fixture(scope="module")
def test_course(test_db, test_teacher):
    # Create a course for testing
    course_data = CourseCreate(name="Mathematics", teacher_id=test_teacher.id)
    with Session(engine) as session:
        course = Course(**course_data.dict())
        session.add(course)
        session.commit()
        session.refresh(course)
    return course


def test_create_course(client, test_teacher):
    # Test creating a new course
    response = client.post(
        "/courses/",
        json={"name": "Physics", "teacher_id": test_teacher.id}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Physics"
    assert response.json()["teacher_id"] == test_teacher.id


def test_get_course(client, test_course):
    # Test retrieving a course
    response = client.get(f"/courses/{test_course.id}")
    assert response.status_code == 200
    assert response.json()["name"] == test_course.name
    assert response.json()["teacher_id"] == test_course.teacher_id


def test_assign_teacher_to_course(client, test_course, test_teacher):
    # Test assigning a teacher to an existing course
    response = client.put(
        f"/courses/{test_course.id}/assign_teacher",
        json={"teacher_id": test_teacher.id}
    )
    assert response.status_code == 200
    assert response.json()["teacher_id"] == test_teacher.id


def test_get_courses_with_teacher(client):
    # Test retrieving all courses with teacher details
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of courses
    assert all("teacher_id" in course for course in response.json())  # Ensure teacher_id is included


def test_create_course_invalid_teacher(client):
    # Test creating a course with an invalid teacher id
    response = client.post(
        "/courses/",
        json={"name": "Chemistry", "teacher_id": 999}  # Assuming this ID does not exist
    )
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"  # Assuming this error code exists
    assert "invalid teacher id" in response.json()["error"]["message"]  # Expect invalid message