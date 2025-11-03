```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.student import Student
from src.models.course import Course  # Importing the Course model

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})

    with app.app_context():
        # Create the database and tables for Student and Course
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture for providing a test client instance."""
    return app.test_client()

@pytest.fixture
def setup_data(app):
    """Fixture to setup initial data for testing."""
    with app.app_context():
        # Create test course and student entries in the database
        course1 = Course(name="Math 101")
        course2 = Course(name="Science 101")
        student = Student(name="John Doe")

        db.session.add(course1)
        db.session.add(course2)
        db.session.add(student)
        db.session.commit()

        return student, [course1, course2]

def test_retrieve_student_details_with_courses(client, setup_data):
    """Test case for retrieving student details along with associated courses."""
    student, courses = setup_data

    # Associate the courses with the student
    response = client.post(f'/students/{student.id}/courses', 
                           data=json.dumps({"course_ids": [courses[0].id, courses[1].id]}),
                           content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == "Courses assigned successfully"

    # Retrieve the student's details
    response = client.get(f'/students/{student.id}')
    assert response.status_code == 200
    data = response.json
    assert data['id'] == student.id
    assert data['name'] == student.name
    assert len(data['courses']) == 2  # Two courses should be returned
    assert any(course['name'] == "Math 101" for course in data['courses'])
    assert any(course['name'] == "Science 101" for course in data['courses'])

def test_retrieve_student_details_no_courses(client, setup_data):
    """Test case for retrieving student details when no courses are assigned."""
    student, _ = setup_data

    # Retrieve the student's details
    response = client.get(f'/students/{student.id}')
    assert response.status_code == 200
    data = response.json
    assert data['id'] == student.id
    assert data['name'] == student.name
    assert len(data['courses']) == 0  # No courses should be returned

def test_assign_invalid_course(client, setup_data):
    """Test case for attempting to assign an invalid course to a student."""
    student, _ = setup_data

    # Attempt to assign an invalid course ID
    invalid_course_id = 9999
    response = client.post(f'/students/{student.id}/courses', 
                           data=json.dumps({"course_ids": [invalid_course_id]}),
                           content_type='application/json')
    assert response.status_code == 400  # Bad request due to invalid course
    assert response.json['error']['code'] == 'E001'
    assert response.json['error']['message'] == "Invalid course ID"

def test_assign_courses_no_student(client):
    """Test case for attempting to assign courses when no student is selected."""
    invalid_student_id = 9999
    response = client.post(f'/students/{invalid_student_id}/courses', 
                           data=json.dumps({"course_ids": [1, 2]}),
                           content_type='application/json')
    assert response.status_code == 404  # Not found because student does not exist
    assert response.json['error']['code'] == 'E002'
    assert response.json['error']['message'] == "Student not found"
```