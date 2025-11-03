import pytest
from flask import Flask, jsonify, request
from src.api import create_app
from src.models.student_course import StudentCourses  # Import the new StudentCourses model
from src.models.course import Course
from src.models.student import Student  # Assuming there's a Student model already defined
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def app():
    # Set up the Flask app for testing
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    # Initialize DB
    with app.app_context():
        init_db()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_student_enrollment(client):
    """Test that a student can be enrolled in a course successfully."""
    # Add a student and a course to the database
    with client.application.app_context():
        student = Student(name="John Doe")
        course = Course(name="Biology 101", level="Undergraduate")
        client.application.session.add(student)
        client.application.session.add(course)
        client.application.session.commit()

    # Enroll the student in the course
    response = client.post(f"/students/{student.id}/enroll", json={"course_id": course.id})
    assert response.status_code == 200
    assert b"successfully enrolled" in response.data

def test_student_enrollment_non_existent_course(client):
    """Test that enrolling a student in a non-existent course returns an error."""
    student = Student(name="Jane Doe")
    
    with client.application.app_context():
        client.application.session.add(student)
        client.application.session.commit()

    # Try enrolling in a non-existent course
    response = client.post(f"/students/{student.id}/enroll", json={"course_id": 999})
    assert response.status_code == 404
    assert b"Course not found" in response.data

def test_get_student_courses(client):
    """Test that the list of courses for a student can be retrieved successfully."""
    # Set up data
    with client.application.app_context():
        student = Student(name="Alice Smith")
        course_one = Course(name="Mathematics", level="Undergraduate")
        course_two = Course(name="Physics", level="Undergraduate")
        
        client.application.session.add(student)
        client.application.session.add(course_one)
        client.application.session.add(course_two)
        client.application.session.commit()

        # Enroll student in courses
        enrollment_one = StudentCourses(student_id=student.id, course_id=course_one.id)
        enrollment_two = StudentCourses(student_id=student.id, course_id=course_two.id)
        client.application.session.add(enrollment_one)
        client.application.session.add(enrollment_two)
        client.application.session.commit()

    # Retrieve courses for the student
    response = client.get(f"/students/{student.id}/courses")
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 2  # Expecting two courses
    assert any(course['course_name'] == "Mathematics" for course in json_data)
    assert any(course['course_name'] == "Physics" for course in json_data)

def test_enrollment_already_exists(client):
    """Test that enrolling a student in an already enrolled course returns an error."""
    # Setup student and course
    with client.application.app_context():
        student = Student(name="Bob Brown")
        course = Course(name="Chemistry", level="Undergraduate")
        client.application.session.add(student)
        client.application.session.add(course)
        client.application.session.commit()

        # Enroll student in course
        client.application.session.add(StudentCourses(student_id=student.id, course_id=course.id))
        client.application.session.commit()

    # Attempt to enroll again in the same course
    response = client.post(f"/students/{student.id}/enroll", json={"course_id": course.id})
    assert response.status_code == 400
    assert b"Already enrolled in the course" in response.data