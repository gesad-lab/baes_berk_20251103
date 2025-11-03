```python
import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import the Course model from app/models.py
from app.models import Course, Teacher  # Assume Teacher model exists

# Create the test client
@pytest.fixture
def client():
    db.create_all()  # Initialize the in-memory database
    # Create test data
    teacher = Teacher(name="John Doe", email="john.doe@example.com")
    course = Course(title="Math 101", teacher_id=None)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()
    app_context = app.app_context()
    app_context.push()
    yield app.test_client()
    app_context.pop()

def test_assign_teacher_to_course(client):
    # Test assigning a teacher to a course successfully
    response = client.post('/courses/1/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 200
    assert response.json == {'success': True}

def test_assign_teacher_to_non_existent_course(client):
    # Test case for assigning a teacher to a non-existent course
    response = client.post('/courses/999/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 404  # Expecting a 404 Not Found
    assert response.json == {'error': {'code': 'E001', 'message': 'Course not found', 'details': {}}}

def test_get_non_existent_course_details(client):
    # Test case for retrieving details for a non-existent course
    response = client.get('/courses/999')
    assert response.status_code == 404  # Expecting a 404 Not Found
    assert response.json == {'error': {'code': 'E001', 'message': 'Course not found', 'details': {}}}

def test_list_courses_for_non_existent_teacher(client):
    # Test case for listing courses for a non-existent teacher
    response = client.get('/teachers/999/courses')
    assert response.status_code == 404  # Expecting a 404 Not Found
    assert response.json == {'error': {'code': 'E001', 'message': 'Teacher not found', 'details': {}}}
```