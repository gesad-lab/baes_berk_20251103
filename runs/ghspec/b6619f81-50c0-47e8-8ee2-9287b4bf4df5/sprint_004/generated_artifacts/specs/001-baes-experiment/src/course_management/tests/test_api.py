```python
import pytest
from flask import Flask
from src.models import Student, Course  # Import the Student and Course models
from src.repositories import StudentCoursesRepository  # Assuming a repository for student course operations
from sqlalchemy.exc import IntegrityError

# Create a Flask application context for testing
@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    # Add additional app configurations if needed
    return app

@pytest.fixture
def client(app):
    """A test client for the Flask application."""
    return app.test_client()

@pytest.fixture
def student_repository():
    """Fixture for creating a student repository for testing."""
    return StudentCoursesRepository()

@pytest.fixture
def new_student(db_session):
    """Fixture for a new student with valid attributes."""
    student = Student(name="John Doe", email="johndoe@example.com")
    db_session.add(student)
    db_session.commit()
    return student

@pytest.fixture
def new_course(db_session):
    """Fixture for a new course with valid attributes."""
    course = Course(name="Introduction to Programming")
    db_session.add(course)
    db_session.commit()
    return course

def test_enroll_student_in_course(client, new_student, new_course):
    """Test that a student can enroll in a course."""
    response = client.post(f'/students/{new_student.id}/enroll', json={
        'course_ids': [new_course.id]
    })
    assert response.status_code == 200
    assert b"Successfully enrolled" in response.data  # Assure response message

def test_get_student_courses(client, new_student, new_course):
    """Test that retrieving a student's courses returns the correct data."""
    client.post(f'/students/{new_student.id}/enroll', json={
        'course_ids': [new_course.id]
    })
    
    response = client.get(f'/students/{new_student.id}/courses')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['courses'] == [{'id': new_course.id, 'name': new_course.name}]

def test_update_student_course_enrollment(client, new_student, new_course):
    """Test updating a student's course enrollment."""
    # Enroll student in a course
    client.post(f'/students/{new_student.id}/enroll', json={
        'course_ids': [new_course.id]
    })

    # Update enrollment by adding another course
    new_course2 = Course(name="Data Structures")
    client.post(f'/students/{new_student.id}/enroll', json={
        'course_ids': [new_course.id, new_course2.id]
    })
    
    response = client.get(f'/students/{new_student.id}/courses')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data['courses']) == 2

def test_enroll_student_invalid_course(client, new_student):
    """Test handling of invalid course enrollment."""
    response = client.post(f'/students/{new_student.id}/enroll', json={
        'course_ids': [999]  # Non-existing course ID
    })
    assert response.status_code == 400  # Bad Request
    assert b"Invalid course ID" in response.data  # Ensure error message is returned
```