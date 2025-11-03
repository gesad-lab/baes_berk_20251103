```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Base, Course, Teacher  # Importing necessary models

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database for integration tests
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test setup to create a course and a teacher before running tests
@pytest.fixture(scope="module")
def setup_database():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    # Create a test teacher
    with SessionLocal() as session:
        test_teacher = Teacher(name="Test Teacher")
        session.add(test_teacher)
        session.commit()

        # Create a test course
        test_course = Course(name="Test Course", teacher_id=None)  # Initially, no teacher assigned
        session.add(test_course)
        session.commit()

        yield test_course, test_teacher.id  # yield course and teacher_id for tests

    # Drop the database tables after testing
    Base.metadata.drop_all(bind=engine)

def test_update_course_teacher_api(setup_database):
    test_course, teacher_id = setup_database
    
    # Send PATCH request to assign a teacher to the course
    response = client.patch(f"/courses/{test_course.id}", json={"teacher_id": teacher_id})
    
    assert response.status_code == 200  # Check for success status
    assert response.json()["teacher_id"] == teacher_id  # Ensure the response contains the correct teacher_id

def test_update_course_teacher_invalid_id():
    # Send PATCH request with an invalid course ID
    response = client.patch("/courses/9999", json={"teacher_id": 1})
    
    assert response.status_code == 404  # Check for not found status
    assert response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}  # Check error response format

def test_update_course_teacher_missing_teacher_id(setup_database):
    test_course, _ = setup_database
    
    # Send PATCH request without teacher_id
    response = client.patch(f"/courses/{test_course.id}", json={})
    
    assert response.status_code == 422  # Check for unprocessable entity due to validation
    assert "detail" in response.json()  # Check if detail key exists for validation errors
```