```python
# tests/api/test_student_course_api.py

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from src.models.student import Student
from src.models.course import Course
from src.models.student_courses import StudentCourses
from src.services.student_course_service import associate_student_with_course, get_courses_for_student
from src.validation.student_course_validation import validate_course_association

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['TESTING'] = True
db = SQLAlchemy(app)

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the in-memory database
            # Add sample data
            student = Student(id="1", name="John Doe")
            course = Course(id="101", name="Mathematics")
            db.session.add(student)
            db.session.add(course)
            db.session.commit()
        yield client
        db.drop_all()  # Cleanup after tests

def test_associate_student_with_course(client):
    """
    Test to ensure that a student can be associated with a course.
    """
    response = client.post('/students/1/courses', json={"course_id": "101"})
    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == {"message": "Successfully associated student with course."}

def test_get_courses_for_student(client):
    """
    Test to ensure that all courses for a student can be retrieved.
    """
    client.post('/students/1/courses', json={"course_id": "101"})  # Associate course first
    response = client.get('/students/1/courses')
    assert response.status_code == HTTPStatus.OK
    courses = response.get_json()
    assert isinstance(courses, list)  # Should be a list
    assert len(courses) > 0  # Should contain the associated course

def test_associate_student_with_invalid_course(client):
    """
    Test to check error handling when associating a student with an invalid course.
    """
    response = client.post('/students/1/courses', json={"course_id": "999"})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json()["error"]["message"] == "Course not found."

def test_course_association_validation(client):
    """
    Test that validation is performed on course association.
    """
    with pytest.raises(ValidationError):
        validate_course_association({"course_id": None})  # Should raise validation error
```