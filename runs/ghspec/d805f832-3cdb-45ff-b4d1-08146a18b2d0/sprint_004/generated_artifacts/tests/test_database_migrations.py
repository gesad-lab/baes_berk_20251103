```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Course, Student, StudentCourse, Base  # Assuming models are defined in models.py
from main import app, get_db  # Assume the FastAPI app and db session dependency are in main.py

# SQLite database connection settings for testing
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a fixture for the test client
@pytest.fixture(scope="module")
def test_client():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    # Create a new FastAPI TestClient
    with TestClient(app) as client:
        yield client
        
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

# Helper function to create a sample course
def create_course(db, name="Sample Course", level="Beginner"):
    course = Course(name=name, level=level)
    db.add(course)
    db.commit()
    return course

# Helper function to create a sample student
def create_student(db, name="Sample Student"):
    student = Student(name=name)
    db.add(student)
    db.commit()
    return student

# Test case to confirm the correct course data is returned for existing associations
def test_retrieve_students_courses(test_client):
    # Step 1: Setup the database session
    db = TestingSessionLocal()
    
    # Step 2: Create a sample course and student
    course = create_course(db)
    student = create_student(db)

    # Step 3: Associate the course with the student
    response = test_client.post(f"/students/{student.id}/courses", json={"course_id": course.id})
    
    # Step 4: Verify that the response indicates successful association
    assert response.status_code == 200
    response_data = response.json()
    assert "message" in response_data
    assert response_data["message"] == "Course associated successfully."

    # Step 5: Retrieve the student's courses
    retrieval_response = test_client.get(f"/students/{student.id}/courses")

    # Step 6: Validate the response contains the correct course data
    assert retrieval_response.status_code == 200
    courses_data = retrieval_response.json()
    assert len(courses_data) == 1
    assert courses_data[0]["id"] == course.id
    assert courses_data[0]["name"] == course.name

    db.close()
```