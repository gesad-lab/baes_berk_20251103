```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, StudentCourses  # Ensure all necessary models are imported
from your_app import app  # Adjust the import based on your application structure
from fastapi.testclient import TestClient

# Setup for SQLite in-memory database for testing
@pytest.fixture(scope='module')
def test_database():
    # Create a new SQLite database (in-memory)
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create all tables
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Dependency override for testing
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    yield  # this will run the tests

    # Cleanup
    Base.metadata.drop_all(engine)


@pytest.fixture(scope='module')
def test_client():
    with TestClient(app) as client:
        yield client


def test_enroll_student_in_course(test_client, test_database):
    # Create a student and a course to enroll them
    student = Student(name="Test Student")
    course = Course(name="Test Course")
    
    db = next(test_database)
    db.add(student)
    db.add(course)
    db.commit()
    
    # Enroll the student in the course
    response = test_client.post(f"/students/{student.id}/enroll", json={"course_id": course.id})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Student successfully enrolled in the course."}


def test_retrieve_student_courses(test_client, test_database):
    student = Student(name="Another Test Student")
    course1 = Course(name="Course One")
    course2 = Course(name="Course Two")
    
    db = next(test_database)
    db.add(student)
    db.add(course1)
    db.add(course2)
    db.flush()  # Ensure IDs are generated
    
    # Enroll student in both courses
    db.add(StudentCourses(student_id=student.id, course_id=course1.id))
    db.add(StudentCourses(student_id=student.id, course_id=course2.id))
    db.commit()

    # Retrieve the student's courses
    response = test_client.get(f"/students/{student.id}/courses")
    
    assert response.status_code == 200
    assert len(response.json()) == 2  # Verify that two courses are returned
    assert {'id': course1.id, 'name': course1.name} in response.json()
    assert {'id': course2.id, 'name': course2.name} in response.json()


def test_enroll_student_invalid(test_client, test_database):
    # Attempt to enroll a student with a non-existing course
    response = test_client.post("/students/999/enroll", json={"course_id": 999})
    
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid student or course ID."}}


def test_enroll_student_nonexistent_student(test_client, test_database):
    # Attempt to enroll with a nonexistent student ID
    course = Course(name="Valid Course")
    
    db = next(test_database)
    db.add(course)
    db.commit()
    
    response = test_client.post("/students/999/enroll", json={"course_id": course.id})
    
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid student or course ID."}}
```