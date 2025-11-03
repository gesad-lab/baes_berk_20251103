```python
# tests/test_course.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.main import app
from src.database.database import get_db
from src.models.course import Course
from src.models.teacher import Teacher
from src.schemas.course import CourseResponse
from src.schemas.teacher import TeacherResponse

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    # Dependency override for the database session
    from src.database.database import SessionLocal
    yield SessionLocal()

def test_assign_teacher_to_course(db):
    """Test assigning a teacher to a course."""
    # Create a teacher instance for assignment
    teacher = Teacher(name="John Doe")
    db.add(teacher)
    db.commit()
    db.refresh(teacher)

    # Create a course instance
    course = Course(name="Math 101")
    db.add(course)
    db.commit()
    db.refresh(course)

    # Assign the teacher to the course
    response = client.patch(f"/courses/{course.id}", json={"teacher_id": teacher.id})
    
    assert response.status_code == 200
    updated_course = response.json()
    assert updated_course["teacher_id"] == teacher.id
    assert updated_course["teacher_name"] == teacher.name  # Assuming teacher_name is included in response

def test_get_course_with_teacher(db):
    """Test retrieving course information with teacher details."""
    # Create a teacher and a course as done in the previous test
    teacher = Teacher(name="Jane Smith")
    db.add(teacher)
    db.commit()
    db.refresh(teacher)

    course = Course(name="Science 101", teacher_id=teacher.id)
    db.add(course)
    db.commit()
    db.refresh(course)

    # Retrieve the course
    response = client.get(f"/courses/{course.id}")
    
    assert response.status_code == 200
    retrieved_course = response.json()
    assert retrieved_course["id"] == course.id
    assert retrieved_course["teacher_id"] == teacher.id
    assert retrieved_course["teacher_name"] == teacher.name

def test_list_all_courses_with_teachers(db):
    """Test listing all courses with associated teacher information."""
    # Create teachers and courses
    teacher1 = Teacher(name="Alice Johnson")
    teacher2 = Teacher(name="Bob Brown")
    db.add(teacher1)
    db.add(teacher2)
    db.commit()
    
    course1 = Course(name="History 101", teacher_id=teacher1.id)
    course2 = Course(name="Art 101", teacher_id=teacher2.id)
    db.add(course1)
    db.add(course2)
    db.commit()

    # List all courses
    response = client.get("/courses")
    
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) == 2
    assert any(course["teacher_name"] == teacher1.name for course in courses)
    assert any(course["teacher_name"] == teacher2.name for course in courses)

def test_assign_teacher_with_invalid_id(db):
    """Test handling assignment of a teacher with an invalid ID."""
    # Create a course instance
    course = Course(name="Math 201")
    db.add(course)
    db.commit()
    db.refresh(course)

    # Attempt to assign a nonexistent teacher id
    response = client.patch(f"/courses/{course.id}", json={"teacher_id": 999})
    
    assert response.status_code == 400
    assert response.json() == {"error": {
        "code": "E001", 
        "message": "Invalid teacher ID provided.", 
        "details": {}
    }}
```