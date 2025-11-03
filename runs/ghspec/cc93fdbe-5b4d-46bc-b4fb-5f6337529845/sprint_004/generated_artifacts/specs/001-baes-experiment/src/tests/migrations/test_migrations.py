```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Base, Student, Course, StudentCourse  # Assuming these models are defined in models.py

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database for migrations
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_db():
    # Create the database schema for testing
    Base.metadata.create_all(bind=engine)
    
    # Assuming we have some initial data to test with
    with SessionLocal() as session:
        # Create sample students and courses for testing
        student = Student(name="John Doe")
        course = Course(name="Mathematics")
        session.add(student)
        session.add(course)
        session.commit()

        # Assuming we need to save student and course IDs for future tests
        yield student.id, course.id

    Base.metadata.drop_all(bind=engine)  # Cleanup after tests

def test_create_student_course_relationship(setup_db):
    """Test successful assignment of a course to a student."""
    student_id, course_id = setup_db
    response = client.post(f"/students/{student_id}/courses", json={"course_id": course_id})
    
    assert response.status_code == 200
    assert response.json() == {"message": f"Course {course_id} assigned to student {student_id}"}

def test_retrieve_student_courses(setup_db):
    """Test retrieval of courses assigned to a specific student."""
    student_id, course_id = setup_db
    response = client.get(f"/students/{student_id}/courses")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Ensure the list is not empty
    assert response.json()[0]["id"] == course_id  # Check course ID is correct

def test_error_handling_invalid_course_id(setup_db):
    """Test error handling when assigning an invalid course ID."""
    student_id, _ = setup_db
    response = client.post(f"/students/{student_id}/courses", json={"course_id": 9999})  # Assuming 9999 does not exist
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid course ID."}

def test_database_migration(setup_db):
    """Test that the database migration creates the relationship table without data loss."""
    student_id, course_id = setup_db
    
    # Check if student and course exist
    with SessionLocal() as session:
        student = session.query(Student).filter(Student.id == student_id).first()
        course = session.query(Course).filter(Course.id == course_id).first()
        
        assert student is not None
        assert course is not None
        
        # Check if the student_courses relationship table is created
        relationship_exists = session.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='student_courses';").fetchone()
        
        assert relationship_exists is not None, "student_courses table does not exist"
```