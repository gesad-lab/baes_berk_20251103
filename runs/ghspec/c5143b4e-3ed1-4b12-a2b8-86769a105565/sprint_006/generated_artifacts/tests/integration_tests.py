```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models import Base, Teacher, Course  # Importing Course model
from src.database import get_db

# Set up test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # Using in-memory SQLite for tests
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
@pytest.fixture(scope="module")
def db_setup():
    # Create the tables in the database
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Dependency override for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def test_client(db_setup):  # Ensure the database setup is ready
    yield TestClient(app)

def test_assign_teacher_to_course_success(test_client):
    # First, create a teacher and a course for testing
    teacher_data = {"name": "John Doe"}
    course_data = {"title": "Mathematics 101", "description": "Basic Math Course"}
    
    # Post teacher
    teacher_response = test_client.post("/teachers", json=teacher_data)
    assert teacher_response.status_code == 201
    teacher_id = teacher_response.json()["id"]
    
    # Post course
    course_response = test_client.post("/courses", json=course_data)
    assert course_response.status_code == 201
    course_id = course_response.json()["id"]
    
    # Assign teacher to course
    response = test_client.put(f"/courses/{course_id}/assignTeacher", json={"teacherId": teacher_id})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == teacher_id

def test_assign_teacher_invalid_course(test_client):
    response = test_client.put("/courses/invalid_course_id/assignTeacher", json={"teacherId": "teacher_id"})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E001"

def test_remove_teacher_from_course_success(test_client):
    # Assuming teacher and course are already created and assigned
    response = test_client.delete("/courses/course_id/removeTeacher")
    assert response.status_code == 200
    assert response.json()["teacher_id"] is None
```