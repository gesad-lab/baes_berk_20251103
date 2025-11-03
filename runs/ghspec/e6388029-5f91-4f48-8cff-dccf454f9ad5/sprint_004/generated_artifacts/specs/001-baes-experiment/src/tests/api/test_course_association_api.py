```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.models import Student, Course, StudentCourses  # Import models for integration testing

# Configure the SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def test_client():
    """Fixture to create a testing client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

@pytest.fixture()
def init_db():
    """Fixture to initialize the database for tests."""
    # Create the schema and add test data here before each test
    from src.database import Base
    Base.metadata.create_all(bind=engine)

    # Add sample students and courses to database
    with TestingSessionLocal() as session:
        student = Student(id=1, name="Test Student")
        course1 = Course(id=1, title="Test Course 1")
        course2 = Course(id=2, title="Test Course 2")
        session.add(student)
        session.add(course1)
        session.add(course2)
        session.commit()
        
    yield
    
    # Cleanup after tests
    with TestingSessionLocal() as session:
        session.query(Student).delete()
        session.query(Course).delete()
        session.commit()
    
    Base.metadata.drop_all(bind=engine)

def test_associate_student_with_courses(init_db, test_client):
    """Test associating a student with valid course IDs."""
    response = test_client.post("/students/1/courses", json={"course_ids": [1, 2]})
    assert response.status_code == 201
    assert response.json() == {"message": "Courses associated successfully"}

def test_associate_student_with_invalid_courses(init_db, test_client):
    """Test associating a student with invalid course IDs."""
    response = test_client.post("/students/1/courses", json={"course_ids": [99]})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid course IDs", "details": {}}}

def test_retrieve_student_courses(init_db, test_client):
    """Test retrieving a student record and their associated courses."""
    test_client.post("/students/1/courses", json={"course_ids": [1]})
    response = test_client.get("/students/1")
    assert response.status_code == 200
    assert response.json()["courses"] == [1]  # Expecting the list of course IDs

def test_remove_course_association(init_db, test_client):
    """Test removing a course association from a student."""
    test_client.post("/students/1/courses", json={"course_ids": [1]})
    response = test_client.delete("/students/1/courses/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Course association removed"}

    # Verify the course was removed
    response = test_client.get("/students/1")
    assert response.json()["courses"] == []

def test_existing_data_intact(init_db, test_client):
    """Test that existing student and course data remains intact."""
    student_response = test_client.get("/students/1")
    course1_response = test_client.get("/courses/1")
    course2_response = test_client.get("/courses/2")

    assert student_response.status_code == 200
    assert course1_response.status_code == 200
    assert course2_response.status_code == 200
    
    assert student_response.json()["name"] == "Test Student"
    assert course1_response.json()["title"] == "Test Course 1"
    assert course2_response.json()["title"] == "Test Course 2"
```