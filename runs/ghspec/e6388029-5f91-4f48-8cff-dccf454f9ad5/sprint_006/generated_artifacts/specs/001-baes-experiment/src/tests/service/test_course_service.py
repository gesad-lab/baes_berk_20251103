```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.models import Course, Teacher  # Import the necessary models
from src.database import get_db

# Configure the SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override for testing
@app.on_event("startup")
def startup():
    # Create the database tables for testing
    from src.database import Base
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
def shutdown():
    # Drop all tables after tests
    from src.database import Base
    Base.metadata.drop_all(bind=engine)

# Dependency override for database session in tests
@pytest.fixture(scope="module")
def test_client():
    app.dependency_overrides[get_db] = lambda: TestingSessionLocal()
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def create_data(test_client):
    # Create a course and a teacher for testing
    teacher = Teacher(name="Test Teacher", email="teacher@example.com")
    course = Course(name="Test Course")
    
    with TestingSessionLocal() as db:
        db.add(teacher)
        db.add(course)
        db.commit()
        db.refresh(teacher)
        db.refresh(course)

    return teacher.id, course.id

def test_assign_teacher_to_course(test_client, create_data):
    teacher_id, course_id = create_data
    response = test_client.patch(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})
    assert response.status_code == 204  # No content indicates success

def test_assign_non_existing_teacher(test_client, create_data):
    teacher_id, course_id = create_data
    response = test_client.patch(f"/courses/{course_id}/assign-teacher", json={"teacher_id": 999})  # Non-existing ID
    assert response.status_code == 400
    assert response.json() == {"detail": "Teacher not found"}

def test_retrieve_course_with_teacher(test_client, create_data):
    teacher_id, course_id = create_data
    test_client.patch(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})  # Assign the teacher
    response = test_client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["teacher_id"] == teacher_id  # Check correct teacher assigned

def test_existing_student_and_course_records_intact(test_client, create_data):
    # Assuming existing records are created and we validate their integrity post-operation
    student_response = test_client.get("/students")  # Fetch existing students list
    initial_student_count = len(student_response.json())
    
    teacher_id, course_id = create_data
    test_client.patch(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})
    
    student_response_after = test_client.get("/students")  # Fetch again
    assert len(student_response_after.json()) == initial_student_count  # Ensure count unchanged

def test_assign_multiple_teachers_to_course(test_client, create_data):
    teacher_id_1, course_id = create_data
    # Create another teacher
    second_teacher = Teacher(name="Second Teacher", email="second@example.com")
    
    with TestingSessionLocal() as db:
        db.add(second_teacher)
        db.commit()
        db.refresh(second_teacher)
    
    response = test_client.patch(f"/courses/{course_id}/assign-teacher", json={"teacher_id": second_teacher.id})
    assert response.status_code == 400
    assert response.json() == {"detail": "Each course can only have one assigned teacher"}
```