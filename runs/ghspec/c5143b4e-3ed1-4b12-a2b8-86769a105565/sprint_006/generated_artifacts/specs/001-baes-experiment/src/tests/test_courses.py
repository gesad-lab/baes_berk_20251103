```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.schemas import Course, Teacher
from sqlalchemy.orm import Session
from src.database import get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    yield client

@pytest.fixture(scope="module")
def db_session():
    # Setup code for creating a test database session or use test DB functionalities
    with get_db() as db:  # Assuming get_db handles session creation
        yield db

@pytest.fixture(scope="function")
def create_course(db_session: Session):
    # Create a sample course for testing
    new_course = Course(name="Test Course", teacher_id=None)
    db_session.add(new_course)
    db_session.commit()
    return new_course

@pytest.fixture(scope="function")
def create_teacher(db_session: Session):
    # Create a sample teacher for testing
    new_teacher = Teacher(name="Test Teacher")
    db_session.add(new_teacher)
    db_session.commit()
    return new_teacher

def test_remove_teacher_from_course(test_client, create_course, create_teacher):
    # First, assign a teacher to the course
    assign_response = test_client.put(f"/courses/{create_course.id}/assignTeacher", json={"teacherId": create_teacher.id})
    assert assign_response.status_code == 200
    assert assign_response.json()["teacher_id"] == create_teacher.id
    
    # Now, remove the teacher from the course
    remove_response = test_client.delete(f"/courses/{create_course.id}/removeTeacher")
    assert remove_response.status_code == 200
    assert remove_response.json()["teacher_id"] is None  # Assuming teacher_id is set to None upon removal

def test_remove_teacher_invalid_course_id(test_client):
    # Attempt to remove a teacher from an invalid course ID
    remove_response = test_client.delete("/courses/99999/removeTeacher")  # Assuming 99999 does not exist
    assert remove_response.status_code == 404
    assert remove_response.json() == {"error": {"code": "E001", "message": "Course not found."}}

def test_remove_teacher_no_teacher_assigned(test_client, create_course):
    # Attempt to remove a teacher when none is assigned
    remove_response = test_client.delete(f"/courses/{create_course.id}/removeTeacher")
    assert remove_response.status_code == 400  # Assuming it returns a bad request error
    assert remove_response.json() == {"error": {"code": "E002", "message": "No teacher assigned to this course."}}
```