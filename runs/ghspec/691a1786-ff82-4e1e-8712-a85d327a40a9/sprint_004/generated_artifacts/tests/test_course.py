import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse
from src.db.database import get_db
from sqlalchemy.orm import Session

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def test_db():
    # Setup code for initializing the database
    # Ideally, this would involve creating the test database,
    # including the necessary tables and records.
    db: Session = get_db()
    student = Student(id=1, name="John Doe")
    course = Course(id=1, title="Mathematics 101")
    
    # Assuming you have functions to add these objects to the database
    db.add(student)
    db.add(course)
    db.commit()
    yield db
    
    # Teardown code to clean up the database after tests
    db.delete(student)
    db.delete(course)
    db.commit()

def test_enroll_student_in_course(test_client, test_db):
    response = test_client.post(
        "/api/v1/enroll_student",
        json={"student_id": 1, "course_id": 1}
    )
    assert response.status_code == 200
    assert response.json()["courses"] == [{"course_id": 1, "title": "Mathematics 101"}]

def test_retrieve_student_courses(test_client, test_db):
    # First, enroll the student in a course
    test_client.post("/api/v1/enroll_student", json={"student_id": 1, "course_id": 1})
    
    response = test_client.get("/api/v1/student_courses/1")
    assert response.status_code == 200
    assert response.json() == [{"course_id": 1, "title": "Mathematics 101"}]

def test_remove_course_from_student(test_client, test_db):
    # First, enroll the student in a course
    test_client.post("/api/v1/enroll_student", json={"student_id": 1, "course_id": 1})
    
    response = test_client.delete(
        "/api/v1/remove_course",
        json={"student_id": 1, "course_id": 1}
    )
    assert response.status_code == 200
    assert response.json()["courses"] == []  # Assuming the student has no courses left

def test_retrieve_courses_for_non_existent_student(test_client):
    response = test_client.get("/api/v1/student_courses/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found"}} 

def test_remove_course_from_non_existent_student(test_client):
    response = test_client.delete(
        "/api/v1/remove_course",
        json={"student_id": 999, "course_id": 1}
    )
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found"}} 

def test_remove_non_existent_course_from_student(test_client, test_db):
    # First, enroll the student in a course
    test_client.post("/api/v1/enroll_student", json={"student_id": 1, "course_id": 1})
    
    response = test_client.delete(
        "/api/v1/remove_course",
        json={"student_id": 1, "course_id": 999}
    )
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}} 
