```python
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Student, Course, Enrollment
from sqlalchemy.orm import Session
from database import get_db, Base, engine

# Create the test client used for sending requests to the application
client = TestClient(app)

# Dependency override for the database session
def override_get_db():
    db = Session(bind=engine)
    yield db
    db.close()

# Setup the test database and create the necessary tables
@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Add sample data for testing
@pytest.fixture(scope="module")
def sample_data(setup_database):
    with Session(bind=engine) as db:
        student = Student(name="John Doe")
        course1 = Course(name="Math 101", level="Beginner")
        course2 = Course(name="History 201", level="Intermediate")
        
        db.add(student)
        db.add(course1)
        db.add(course2)
        db.commit()

        yield {
            "student": student,
            "course1": course1,
            "course2": course2
        }

def test_enroll_student_in_course(sample_data):
    student_id = sample_data['student'].id
    course_id = sample_data['course1'].id
    response = client.post(f"/enroll/{student_id}/course/{course_id}")

    assert response.status_code == 200
    assert response.json() == {"message": "Enrollment successful"}
    
    # Verify that the student is enrolled in the course
    with Session(bind=engine) as db:
        student = db.query(Student).filter(Student.id == student_id).first()
        assert course_id in [course.id for course in student.enrolled_courses]

def test_retrieve_student_enrolled_courses(sample_data):
    student_id = sample_data['student'].id
    course_id = sample_data['course1'].id
    client.post(f"/enroll/{student_id}/course/{course_id}")

    response = client.get(f"/students/{student_id}/courses")

    assert response.status_code == 200
    courses = response.json()
    assert len(courses) == 1
    assert courses[0]['id'] == course_id
    assert courses[0]['name'] == "Math 101"
    assert courses[0]['level'] == "Beginner"

def test_enroll_student_in_invalid_course(sample_data):
    student_id = sample_data['student'].id
    invalid_course_id = 999  # Assuming this ID does not exist
    response = client.post(f"/enroll/{student_id}/course/{invalid_course_id}")

    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Invalid course ID"}}

def test_handle_enrollment_of_existing_course(sample_data):
    student_id = sample_data['student'].id
    course_id = sample_data['course1'].id
    client.post(f"/enroll/{student_id}/course/{course_id}")  # First enrollment

    response = client.post(f"/enroll/{student_id}/course/{course_id}")  # Second enrollment

    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E400", "message": "Student already enrolled in this course"}}
```