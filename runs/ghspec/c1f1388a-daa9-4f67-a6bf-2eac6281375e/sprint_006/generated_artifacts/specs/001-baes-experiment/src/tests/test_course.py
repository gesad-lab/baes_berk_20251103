```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.database import init_db, get_db
from src.models.course import Course  # Import the Course model
from src.models.teacher import Teacher  # Import the Teacher model
from sqlalchemy.orm import Session

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def db():
    # Initialize the database and create a new session for testing
    db = get_db()
    yield db
    db.close()

@pytest.fixture(scope="module")
def setup_data(db: Session):
    # Create dummy data for teachers and courses for testing
    teacher = Teacher(name="Test Teacher")
    db.add(teacher)
    db.commit()
    db.refresh(teacher)

    course = Course(title="Test Course", description="A course for testing")
    db.add(course)
    db.commit()
    db.refresh(course)
    
    return teacher, course

def test_assign_teacher_to_course(test_client, setup_data):
    teacher, course = setup_data
    response = test_client.post(f"/courses/{course.id}/assign_teacher", json={"teacher_id": teacher.id})
    
    assert response.status_code == 200
    # Validating the course now references the specified teacher
    updated_course = test_client.get(f"/courses/{course.id}").json()
    assert updated_course['teacher_id'] == teacher.id

def test_retrieve_courses_for_teacher(test_client, setup_data):
    teacher, _ = setup_data
    response = test_client.get(f"/teachers/{teacher.id}/courses")
    
    assert response.status_code == 200
    # Check that the response contains the course associated with the teacher
    courses = response.json()
    assert len(courses) > 0
    assert all(course['teacher_id'] == teacher.id for course in courses)

def test_assign_teacher_with_invalid_id(test_client, setup_data):
    _, course = setup_data
    response = test_client.post(f"/courses/{course.id}/assign_teacher", json={"teacher_id": 9999})  # Non-existent teacher ID
    
    assert response.status_code == 404
    # Check for the appropriate error message
    assert response.json() == {"error": {"code": "E001", "message": "Teacher does not exist", "details": {}}}
```