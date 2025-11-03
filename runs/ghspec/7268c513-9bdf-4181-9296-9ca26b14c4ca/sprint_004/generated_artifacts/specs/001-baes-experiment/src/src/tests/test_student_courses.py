import pytest
from flask import json
from app import create_app, db  # Importing the app factory and db instance
from app.models import Student, Course, StudentCourse  # Importing models required for testing

@pytest.fixture
def client():
    """Create a test instance of the application."""
    app = create_app({'TESTING': True})  # Create a test instance of the application
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables for testing
            # Seed the database with some test data
            course = Course(name="Test Course", level="Beginner")
            student = Student(name="Test Student", email="student@test.com")
            db.session.add(course)
            db.session.add(student)
            db.session.commit()
        yield client
        db.drop_all()  # Cleanup after tests

def test_enroll_student_course(client):
    """Test enrolling a student into a course."""
    # Assuming the test student has ID 1 and the test course has ID 1
    response = client.post('/students/1/courses', data=json.dumps({"courseId": 1}),
                           content_type='application/json')
    assert response.status_code == 201  # Check if the response status code is 201
    response_data = json.loads(response.data)
    assert response_data['id'] == 1
    assert response_data['name'] == "Test Student"
    assert response_data['course_ids'] == [1]  # Verify the course was enrolled

def test_enroll_student_course_no_course_id(client):
    """Test enrolling a student without providing a course ID."""
    response = client.post('/students/1/courses', data=json.dumps({}),
                           content_type='application/json')
    assert response.status_code == 400  # Check for bad request response
    assert json.loads(response.data) == {"error": {"code": "E001", "message": "Course ID is required."}}

def test_enroll_student_course_invalid_student(client):
    """Test enrolling a student that does not exist."""
    response = client.post('/students/999/courses', data=json.dumps({"courseId": 1}),
                           content_type='application/json')
    assert response.status_code == 404  # Check for not found response
    assert json.loads(response.data) == {"error": {"code": "E003", "message": "Student not found."}}

def test_enroll_student_course_invalid_course(client):
    """Test enrolling a student with a non-existent course."""
    response = client.post('/students/1/courses', data=json.dumps({"courseId": 999}),
                           content_type='application/json')
    assert response.status_code == 404  # Check for not found response
    assert json.loads(response.data) == {"error": {"code": "E002", "message": "Course does not exist."}}

def test_get_enrolled_courses(client):
    """Test retrieving courses a student is enrolled in."""
    # First enroll the student into the course
    client.post('/students/1/courses', data=json.dumps({"courseId": 1}),
                content_type='application/json')
    response = client.get('/students/1/courses')
    assert response.status_code == 200  # Check for success response
    enrolled_courses = json.loads(response.data)
    assert len(enrolled_courses) == 1  # Verify the student has one course
    assert enrolled_courses[0]['id'] == 1
    assert enrolled_courses[0]['name'] == "Test Course"
    assert enrolled_courses[0]['level'] == "Beginner"

def test_get_enrolled_courses_invalid_student(client):
    """Test retrieving courses for a student that does not exist."""
    response = client.get('/students/999/courses')
    assert response.status_code == 404  # Check for not found response
    assert json.loads(response.data) == {"error": {"code": "E003", "message": "Student not found."}}