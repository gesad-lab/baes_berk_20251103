```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db
from sqlalchemy.exc import IntegrityError
from src.models.course import Course
from src.models.teacher import Teacher

# Setup for testing
DATABASE_URL = "postgresql://user:password@localhost/test_db"

# Create a new database engine for testing
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a TestClient instance
client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

def test_assign_teacher_to_course(test_db):
    # Step 1: Create a teacher
    teacher_data = {"name": "John Doe", "email": "john.doe@example.com"}
    response = client.post("/teachers/", json=teacher_data)
    assert response.status_code == 201
    teacher_id = response.json()["id"]

    # Step 2: Create a course
    course_data = {"name": "Biology 101", "description": "Introductory Biology"}
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 201
    course_id = response.json()["id"]

    # Step 3: Assign the teacher to the course
    assignment_data = {"teacherId": teacher_id}
    response = client.post(f"/courses/{course_id}/assign-teacher", json=assignment_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully.", "courseId": course_id, "teacherId": teacher_id}

    # Step 4: Retrieve the course to verify assignment
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["teacher_id"] == teacher_id
    assert response.json()["teacher"]["name"] == "John Doe"
    assert response.json()["teacher"]["email"] == "john.doe@example.com"

def test_assign_teacher_invalid_course(test_db):
    assignment_data = {"teacherId": 1}  # Assuming teacher with ID 1 exists
    response = client.post("/courses/999/assign-teacher", json=assignment_data)  # Invalid course ID
    assert response.status_code == 404
    assert response.json() == {"detail": "Course not found."}

def test_assign_teacher_invalid_teacher(test_db):
    # Step 1: Create a course
    course_data = {"name": "Physics 101", "description": "Introductory Physics"}
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 201
    course_id = response.json()["id"]

    # Step 2: Attempt to assign a non-existing teacher
    assignment_data = {"teacherId": 999}  # Invalid teacher ID
    response = client.post(f"/courses/{course_id}/assign-teacher", json=assignment_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Teacher not found."}
```