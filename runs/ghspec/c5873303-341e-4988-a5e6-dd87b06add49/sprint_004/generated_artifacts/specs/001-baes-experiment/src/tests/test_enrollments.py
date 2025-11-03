```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Student, Course, StudentCourse
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
def create_courses(db_session):
    """Fixture that creates initial courses for tests."""
    course1 = Course(name="Math 101")
    course2 = Course(name="History 201")
    db_session.add(course1)
    db_session.add(course2)
    db_session.commit()
    return course1, course2

@pytest.fixture(scope="module")
def create_student(db_session):
    """Fixture that creates an initial student for tests."""
    student = Student(name="John Doe")
    db_session.add(student)
    db_session.commit()
    return student

def test_enroll_student_in_course(create_student, create_courses, db_session):
    """Test for enrolling a student in a course."""
    
    student = create_student
    course1, course2 = create_courses
    
    # Enroll the student in the first course
    response = client.post(f"/enrollments/{student.id}/", json={"course_id": course1.id})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully enrolled in course."}
    
    # Verify the enrollment in the database
    enrollment = db_session.query(StudentCourse).filter_by(student_id=student.id, course_id=course1.id).first()
    assert enrollment is not None

def test_enroll_student_in_non_existent_course(create_student, db_session):
    """Test for handling enrollment in a non-existent course."""
    
    student = create_student
    
    # Attempt to enroll in a non-existent course
    response = client.post(f"/enrollments/{student.id}/", json={"course_id": 99999})
    
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found."}}

def test_get_student_courses(create_student, create_courses, db_session):
    """Test for retrieving the list of courses a student is enrolled in."""
    
    student = create_student
    course1, course2 = create_courses
    
    # Enroll the student in the first course
    client.post(f"/enrollments/{student.id}/", json={"course_id": course1.id})
    
    # Fetch enrolled courses for the student
    response = client.get(f"/enrollments/{student.id}/courses")
    
    assert response.status_code == 200
    assert response.json() == {"courses": [{"id": course1.id, "name": course1.name}]}

def test_enroll_student_in_multiple_courses(create_student, create_courses, db_session):
    """Test for enrolling a student in multiple courses."""
    
    student = create_student
    course1, course2 = create_courses
    
    # Enroll the student in both courses
    client.post(f"/enrollments/{student.id}/", json={"course_id": course1.id})
    client.post(f"/enrollments/{student.id}/", json={"course_id": course2.id})
    
    # Fetch enrolled courses for the student
    response = client.get(f"/enrollments/{student.id}/courses")
    
    assert response.status_code == 200
    assert response.json() == {
        "courses": [
            {"id": course1.id, "name": course1.name},
            {"id": course2.id, "name": course2.name}
        ]
    }
```