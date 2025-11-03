```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Teacher, Course
from src.database import get_db
from sqlalchemy.orm import sessionmaker

# Test client for the FastAPI application
client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    """Fixture that sets up a database session for testing."""
    db = get_db()
    yield db
    db.rollback()
    db.close()

@pytest.fixture(scope="module")
def create_teacher(db_session):
    """Fixture to create a teacher for testing."""
    teacher = Teacher(name="Test Teacher", email="teacher@example.com")
    db_session.add(teacher)
    db_session.commit()
    db_session.refresh(teacher)
    return teacher

@pytest.fixture(scope="module")
def create_course(db_session):
    """Fixture to create a course for testing."""
    course = Course(name="Test Course", level="Beginner")
    db_session.add(course)
    db_session.commit()
    db_session.refresh(course)
    return course

def test_assign_teacher_to_course(create_course, create_teacher):
    """Test assigning a teacher to a course successfully."""
    response = client.post(f"/courses/{create_course.id}/assign_teacher", json={"teacher_id": create_teacher.id})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully."}

def test_assign_nonexistent_teacher_to_course(create_course):
    """Test assigning a non-existent teacher to a course."""
    response = client.post(f"/courses/{create_course.id}/assign_teacher", json={"teacher_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Teacher not found."}}

def test_assign_teacher_to_nonexistent_course(create_teacher):
    """Test assigning a teacher to a non-existent course."""
    response = client.post(f"/courses/999/assign_teacher", json={"teacher_id": create_teacher.id})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Course not found."}}

def test_retrieve_course_with_teacher(create_course, create_teacher):
    """Test retrieving course information with assigned teacher details."""
    client.post(f"/courses/{create_course.id}/assign_teacher", json={"teacher_id": create_teacher.id})
    response = client.get(f"/courses/{create_course.id}")
    assert response.status_code == 200
    assert response.json()["teacher"]["name"] == create_teacher.name
    assert response.json()["teacher"]["email"] == create_teacher.email

def test_retrieve_nonexistent_course():
    """Test retrieving a non-existent course."""
    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Course not found."}}
```