```python
import json
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from your_application import app, db, Course  # Adjust import based on your structure
from your_application.validators import validate_student_enrollment  # Adjust import based on your structure

# Reinitialize the Flask application and SQLAlchemy for testing
@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables for testing
        yield client  # This will run the tests

@pytest.fixture(scope='module')
def valid_course():
    """Create a valid course for testing."""
    course = Course(name='Test Course', level='Beginner')
    db.session.add(course)
    db.session.commit()
    return course

@pytest.fixture(scope='module')
def valid_student():
    """Create a valid student for testing."""
    # Assuming a Student model exists
    student = Student(name='Test Student')  # Adjust based on actual student fields
    db.session.add(student)
    db.session.commit()
    return student

def test_enroll_student_with_valid_ids(test_client, valid_student, valid_course):
    """Test student enrollment with valid IDs."""
    response = test_client.post(f'/students/{valid_student.id}/enroll', 
                                 json={"course_id": valid_course.id})
    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "Enrollment successful."}

def test_enroll_student_with_invalid_student_id(test_client, valid_course):
    """Test enrollment with an invalid student ID."""
    response = test_client.post('/students/999/enroll', 
                                 json={"course_id": valid_course.id})
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": {"code": "E001", "message": "Invalid student ID."}}

def test_enroll_student_with_invalid_course_id(test_client, valid_student):
    """Test enrollment with an invalid course ID."""
    response = test_client.post(f'/students/{valid_student.id}/enroll', 
                                 json={"course_id": 999})
    assert response.status_code == 404
    assert json.loads(response.data) == {"error": {"code": "E002", "message": "Invalid course ID."}}

def test_retrieve_student_courses(test_client, valid_student, valid_course):
    """Test retrieval of courses for a specific student."""
    test_client.post(f'/students/{valid_student.id}/enroll', 
                     json={"course_id": valid_course.id})  # Enroll the student first
    
    response = test_client.get(f'/students/{valid_student.id}/courses')
    assert response.status_code == 200
    courses = json.loads(response.data)
    assert len(courses) > 0
    assert courses[0]['id'] == valid_course.id
    assert courses[0]['name'] == valid_course.name

def test_enrollment_error_messages(test_client):
    """Test that appropriate error messages are returned for invalid enrollment."""
    invalid_cases = [
        ('students/invalid_id/enroll', {"course_id": "valid_course_id"}, 
         {"error": {"code": "E001", "message": "Invalid student ID."}}),
        ('students/valid_student_id/enroll', {"course_id": "invalid_id"}, 
         {"error": {"code": "E002", "message": "Invalid course ID."}}),
    ]
    
    for path, json_data, expected_error in invalid_cases:
        response = test_client.post(path, json=json_data)
        assert response.status_code == 404
        assert json.loads(response.data) == expected_error
```