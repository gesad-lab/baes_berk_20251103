```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from models.course import Course
from models.teacher import Teacher
from database import get_db, init_db
from services.course import CourseService

# Initialize the FastAPI app and the test client
app = FastAPI()

# Dependency override for testing
@app.on_event("startup")
def startup():
    init_db()

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Set up and teardown the test database for integration tests."""
    with get_db() as db:
        # Create test data: a course and a teacher
        test_teacher = Teacher(name="Test Teacher", email="teacher@example.com")
        test_course = Course(title="Test Course")

        # Add and commit the teacher and the course to the database for testing
        db.add(test_teacher)
        db.add(test_course)
        db.commit()
        db.refresh(test_teacher)
        db.refresh(test_course)

        yield db
        
        # Clean up test data after tests are done
        db.delete(test_teacher)
        db.delete(test_course)
        db.commit()

def test_assign_teacher_to_course(client, setup_database):
    """Test assigning a teacher to a course."""
    response = client.post("/courses/assign-teacher", json={
        "course_id": 1,
        "teacher_id": 1
    })
    
    # Verify response status code and content
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully."}

def test_remove_teacher_from_course(client, setup_database):
    """Test removing a teacher from a course."""
    response = client.post("/courses/remove-teacher", json={
        "course_id": 1,
        "teacher_id": 1
    })
    
    # Verify response status code and content
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher removed from course successfully."}
```