```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Teacher, Course
from src.database import get_db
from sqlalchemy.orm import sessionmaker

# Test client for the FastAPI application
client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    """Fixture that sets up a database session for testing."""
    db = get_db()
    yield db
    db.rollback()
    db.close()

@pytest.fixture(scope="module")
def create_teacher(db_session):
    """Fixture to create a teacher in the database for testing."""
    teacher = Teacher(name="John Doe")
    db_session.add(teacher)
    db_session.commit()
    db_session.refresh(teacher)
    return teacher

@pytest.fixture(scope="module")
def create_course(db_session):
    """Fixture to create a course in the database for testing."""
    course = Course(name="Math 101", level="Beginner")
    db_session.add(course)
    db_session.commit()
    db_session.refresh(course)
    return course

def test_successful_teacher_assignment(db_session, create_teacher, create_course):
    """Test that an admin can successfully assign a teacher to a course."""
    response = client.post(f"/courses/{create_course.id}/assign_teacher", json={"teacher_id": create_teacher.id})
    assert response.status_code == 200  # Check for successful response
    assert response.json() == {"message": "Teacher assigned successfully"}
    
    # Verify that the relationship is reflected in the database
    updated_course = db_session.query(Course).filter(Course.id == create_course.id).first()
    assert updated_course.teacher_id == create_teacher.id  # Check that teacher_id is correctly set

def test_assign_teacher_to_nonexistent_course(db_session, create_teacher):
    """Test handling of assigning a teacher to a non-existent course."""
    response = client.post("/courses/999/assign_teacher", json={"teacher_id": create_teacher.id})
    assert response.status_code == 404  # Expecting a not found error
    assert response.json() == {"detail": "Course not found"}  # Check the error message

def test_retrieve_course_with_teacher_details(db_session, create_teacher, create_course):
    """Test retrieving course information including teacher details."""
    # First, assign the teacher to the course
    client.post(f"/courses/{create_course.id}/assign_teacher", json={"teacher_id": create_teacher.id})
    
    # Now retrieve the course details
    response = client.get(f"/courses/{create_course.id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": create_course.id,
        "name": "Math 101",
        "level": "Beginner",
        "teacher": {
            "id": create_teacher.id,
            "name": "John Doe"
        }
    }  # Check that the correct course details with teacher are returned
```