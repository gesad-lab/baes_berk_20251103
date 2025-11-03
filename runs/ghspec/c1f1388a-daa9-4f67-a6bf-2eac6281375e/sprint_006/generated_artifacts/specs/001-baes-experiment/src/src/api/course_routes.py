```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db.database import init_db, get_db
from src.models.course import Course  # Import the Course model
from src.models.teacher import Teacher  # Import the Teacher model
from sqlalchemy.orm import Session
from fastapi import HTTPException

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def db_session():
    # Setup database connection and session
    db = next(get_db())
    init_db(db)
    yield db
    # Cleanup when done
    db.query(Course).delete()
    db.query(Teacher).delete()
    db.commit()

def create_teacher(db: Session, teacher_id: int):
    # Helper function to create a teacher for testing
    teacher = Teacher(id=teacher_id, name=f'Teacher {teacher_id}')
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

def create_course(db: Session, course_id: int, teacher_id: int):
    # Helper function to create a course for testing
    course = Course(id=course_id, title=f'Course {course_id}', teacher_id=teacher_id)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def test_retrieve_courses_for_teacher(test_client, db_session):
    # Arrange
    teacher = create_teacher(db_session, teacher_id=1)
    course1 = create_course(db_session, course_id=1, teacher_id=teacher.id)
    course2 = create_course(db_session, course_id=2, teacher_id=teacher.id)

    # Act: Send GET request to retrieve courses for the teacher
    response = test_client.get(f'/teachers/{teacher.id}/courses')

    # Assert
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) == 2
    assert courses[0]['id'] == course1.id
    assert courses[1]['id'] == course2.id

def test_retrieve_courses_for_nonexistent_teacher(test_client):
    # Act: Send GET request to retrieve courses for a nonexistent teacher
    response = test_client.get('/teachers/999/courses')

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Teacher not found"}
```