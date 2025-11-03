```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Teacher, Course  # Import relevant models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base  # Assuming there's a database module for the database setup

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_integration_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database and tables
@pytest.fixture(scope="module")
def test_db():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()  # Provide the session to test
    Base.metadata.drop_all(bind=engine)  # Cleanup after tests

@pytest.fixture(scope="module")
def client():
    # Use the test database for the FastAPI test client
    app.dependency_overrides[get_db] = lambda: TestingSessionLocal()
    with TestClient(app) as c:
        yield c

def test_assign_teacher_to_course(client, test_db):
    # Arrange: Create a Teacher and a Course
    teacher = Teacher(name="John Doe")
    course = Course(title="Math 101")
    test_db.add(teacher)
    test_db.add(course)
    test_db.commit()

    # Action: Assign the teacher to the course
    response = client.post(f"/courses/{course.id}/assign_teacher", json={"teacher_id": teacher.id})

    # Assert: Check that the assignment was successful
    assert response.status_code == 200
    assert response.json() == {"msg": "Teacher assigned successfully"}

def test_retrieve_course_with_teacher(client, test_db):
    # Arrange: Use the existing course and teacher from the previous test
    course = test_db.query(Course).first()
    
    # Action: Retrieve the course details
    response = client.get(f"/courses/{course.id}")

    # Assert: Check that the response includes the correct teacher assignment
    assert response.status_code == 200
    assert response.json()["teacher_id"] == course.teacher_id  # Assuming teacher_id is stored in the course

def test_assign_teacher_to_non_existent_course(client, test_db):
    # Action: Attempt to assign a teacher to a non-existent course
    response = client.post("/courses/999/assign_teacher", json={"teacher_id": 1})  # Non-existent course ID

    # Assert: Check that the response indicates the course was not found
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}
```