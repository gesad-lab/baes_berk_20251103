```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is initialized in `main.py`
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from models import Course, Student, Teacher  # Importing relevant models
from repository import assign_teacher_to_course, get_course_details  # Assume these functions exist
import json

# Initialize the test client
client = TestClient(app)

# Setup a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_db():
    # Create the database tables and return a session for tests
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_assign_teacher_to_course(test_db):
    """Test assigning a teacher to a course."""
    # Create mock data
    teacher = Teacher(name="John Doe")
    course = Course(name="Mathematics", teacher_id=None)
    test_db.add(teacher)
    test_db.add(course)
    test_db.commit()
    
    # Assign teacher to the course
    response = client.post(f"/courses/{course.id}/assign_teacher", json={"teacher_id": teacher.id})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully."}
    
    # Validate the assignment in the database
    updated_course = test_db.query(Course).filter(Course.id == course.id).first()
    assert updated_course.teacher_id == teacher.id

def test_get_course_details_with_teacher(test_db):
    """Test retrieving course details with associated teacher."""
    teacher = Teacher(name="Jane Smith")
    course = Course(name="Science", teacher_id=None)
    test_db.add(teacher)
    test_db.add(course)
    test_db.commit()
    
    # Assign teacher to the course
    course.teacher_id = teacher.id
    test_db.commit()

    # Retrieve the course details
    response = client.get(f"/courses/{course.id}")
    
    assert response.status_code == 200
    assert response.json() == {
        "id": course.id,
        "name": "Science",
        "teacher": {
            "id": teacher.id,
            "name": teacher.name
        }
    }

def test_assign_teacher_to_nonexistent_course():
    """Test assigning a teacher to a non-existent course."""
    response = client.post("/courses/999/assign_teacher", json={"teacher_id": 1})
    
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found."}}

def test_assign_nonexistent_teacher_to_course():
    """Test assigning a non-existent teacher to a course."""
    course = Course(name="History")
    with TestingSessionLocal() as db:
        db.add(course)
        db.commit()
    
    response = client.post(f"/courses/{course.id}/assign_teacher", json={"teacher_id": 999})
    
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Teacher not found."}}
```