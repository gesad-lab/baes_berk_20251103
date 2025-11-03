```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models import Student, Course  # Assuming Student and Course models are defined in src/models
from src.api.student_api import app  # Assuming the Flask app with the student API is initialized here

# Initialize Flask app and db for testing
@pytest.fixture(scope='module')
def test_client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()  # Create tables
    yield app.test_client()  # Create test client
    with app.app_context():
        db.drop_all()  # Drop tables after testing

# Fixture for creating a sample student
@pytest.fixture
def new_student():
    student = Student(name="John Doe", email="john@example.com")  # Create a new student
    return student

# Fixture for creating a sample course
@pytest.fixture
def new_course():
    course = Course(title="Mathematics 101", level="Beginner")  # Create a new course
    return course

# Test for creating a student
def test_create_student(test_client):
    response = test_client.post('/api/students', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json['name'] == "John Doe"

# Test for listing students
def test_get_students(test_client, new_student):
    with app.app_context():
        db.session.add(new_student)  # Add student to the database
        db.session.commit()
    
    response = test_client.get('/api/students')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == "John Doe"

# Test for course assignment to a student
def test_assign_course_to_student(test_client, new_student, new_course):
    with app.app_context():
        db.session.add(new_student)
        db.session.add(new_course)
        db.session.commit()
    
    response = test_client.post(f'/api/students/{new_student.id}/courses', json={"course_id": new_course.id})
    assert response.status_code == 200
    assert response.json['message'] == "Course assigned successfully"

# Test for getting courses assigned to a student
def test_get_courses_for_student(test_client, new_student, new_course):
    with app.app_context():
        db.session.add(new_student)
        db.session.add(new_course)
        db.session.commit()
        # Assign course
        test_client.post(f'/api/students/{new_student.id}/courses', json={"course_id": new_course.id})

    response = test_client.get(f'/api/students/{new_student.id}/courses')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['title'] == "Mathematics 101"

# Test for removing a course from a student
def test_remove_course_from_student(test_client, new_student, new_course):
    with app.app_context():
        db.session.add(new_student)
        db.session.add(new_course)
        db.session.commit()
        test_client.post(f'/api/students/{new_student.id}/courses', json={"course_id": new_course.id})

    response = test_client.delete(f'/api/students/{new_student.id}/courses/{new_course.id}')
    assert response.status_code == 200
    assert response.json['message'] == "Course removed successfully"
```