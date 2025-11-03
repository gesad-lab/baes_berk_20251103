```python
import pytest
from flask import json
from app import create_app, db  # Assuming create_app sets up the Flask app and db is the SQLAlchemy instance
from app.models import Student, Course  # Importing the Student and Course models for testing

@pytest.fixture
def client():
    app = create_app({'TESTING': True})  # Create a test instance of the application
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables for testing
        yield client

@pytest.fixture
def sample_student(client):
    # Create a sample student and commit to the database
    student = Student(name="John Doe", email="john.doe@example.com")
    db.session.add(student)
    db.session.commit()
    return student

@pytest.fixture
def sample_course(client):
    # Create a sample course and commit to the database
    course = Course(name="Introduction to Testing", level="Beginner")
    db.session.add(course)
    db.session.commit()
    return course

def test_get_enrolled_courses(client, sample_student, sample_course):
    # Enroll the student in the sample course
    sample_student.courses.append(sample_course)
    db.session.commit()

    # Make a GET request to retrieve enrolled courses
    response = client.get(f"/students/{sample_student.id}/courses")
    assert response.status_code == 200
    data = json.loads(response.data)
    
    # Check that the returned data contains the enrolled course
    assert len(data) == 1
    assert data[0]["id"] == sample_course.id
    assert data[0]["name"] == sample_course.name

def test_enroll_student_course(client, sample_student, sample_course):
    # Prepare the request payload
    payload = {"courseId": sample_course.id}
    
    # Make a POST request to enroll the student in the course
    response = client.post(f"/students/{sample_student.id}/courses", json=payload)
    assert response.status_code == 201
    data = json.loads(response.data)

    # Verify student data after enrollment
    assert data["id"] == sample_student.id
    assert sample_course.id in data["course_ids"]

def test_enroll_student_invalid_course(client, sample_student):
    # Attempt to enroll the student in a non-existent course
    payload = {"courseId": 9999}  # Non-existent course ID
    response = client.post(f"/students/{sample_student.id}/courses", json=payload)
    assert response.status_code == 404
    error_data = json.loads(response.data)
    assert error_data["error"]["code"] == "E002"
    assert error_data["error"]["message"] == "Course does not exist."

def test_preserve_student_records(client, sample_student):
    # Fetch the student to verify existing records are intact
    response = client.get(f"/students/{sample_student.id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    
    # Validate that the retrieved student data matches what's in the database
    assert data["id"] == sample_student.id
    assert data["name"] == sample_student.name
    assert data["email"] == sample_student.email
```