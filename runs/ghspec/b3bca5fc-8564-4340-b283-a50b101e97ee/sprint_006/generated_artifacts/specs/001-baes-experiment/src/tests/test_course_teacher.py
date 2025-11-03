```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Teacher, Course  # Import the Teacher and Course models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base  # Assuming there's a database module for the database setup

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_course_teacher.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the test database structure
@pytest.fixture(scope="module")
def test_db():
    # Create the database
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()  # Provide the session to the test
    Base.metadata.drop_all(bind=engine)  # Clean up the database after tests

@pytest.fixture(scope="module")
def client(test_db):
    app.dependency_overrides[get_db] = lambda: test_db
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module")
def create_teacher(test_db):
    teacher = Teacher(name="Test Teacher")
    test_db.add(teacher)
    test_db.commit()
    test_db.refresh(teacher)
    return teacher

@pytest.fixture(scope="module")
def create_course(test_db):
    course = Course(title="Test Course")
    test_db.add(course)
    test_db.commit()
    test_db.refresh(course)
    return course

def test_assign_teacher_to_course(client, create_course, create_teacher):
    """ Test successful assignment of a Teacher to a Course """
    response = client.put(f"/courses/{create_course.id}/assign_teacher/{create_teacher.id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully"}

    # Verify the teacher was assigned
    course_response = client.get(f"/courses/{create_course.id}")
    assert course_response.status_code == 200
    assert course_response.json()["teacher_id"] == create_teacher.id

def test_retrieve_course_with_teacher(client, create_course, create_teacher):
    """ Test retrieval of Course information including Teacher details """
    client.put(f"/courses/{create_course.id}/assign_teacher/{create_teacher.id}")
    course_response = client.get(f"/courses/{create_course.id}")
    assert course_response.status_code == 200
    assert course_response.json()["teacher"]["name"] == create_teacher.name

def test_assign_teacher_to_nonexistent_course(client, create_teacher):
    """ Test response when attempting to assign a Teacher to a non-existent Course """
    response = client.put("/courses/999/assign_teacher/{}".format(create_teacher.id))
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}
```