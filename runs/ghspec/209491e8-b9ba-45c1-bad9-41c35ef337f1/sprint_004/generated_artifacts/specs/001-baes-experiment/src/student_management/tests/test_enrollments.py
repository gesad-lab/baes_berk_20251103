```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Student, Course, StudentCourse

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Setup the database for testing by creating sample student and course records."""
    student = Student(name="John Doe", email="john@example.com")
    course = Course(title="Mathematics 101")
    
    # Add the student and course to the database (assuming the session is available)
    session.add(student)
    session.add(course)
    session.commit()

    yield student, course  # provides the fixture value

    # Cleanup after tests
    session.delete(student)
    session.delete(course)
    session.commit()

def test_enroll_student_in_course(setup_database):
    student, course = setup_database
    response = client.post(f"/students/{student.id}/courses", json={"course_id": course.id})
    
    assert response.status_code == 201
    assert response.json() == {"message": "Enrollment successful"}

def test_enroll_student_in_invalid_course(setup_database):
    student, _ = setup_database
    response = client.post(f"/students/{student.id}/courses", json={"course_id": 999})  # Invalid course ID
    
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}

def test_enroll_invalid_student(setup_database):
    _, course = setup_database
    response = client.post("/students/999/courses", json={"course_id": course.id})  # Invalid student ID
    
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}

def test_enroll_student_without_course_id(setup_database):
    student, _ = setup_database
    response = client.post(f"/students/{student.id}/courses", json={})  # Missing course_id
    
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {"detail": [{"loc": ["body", "course_id"], "msg": "field required", "type": "value_error.missing"}]}
```