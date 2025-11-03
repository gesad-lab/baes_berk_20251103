```python
import pytest
from flask import jsonify
from app import app, db, Student, Course, StudentCourse  # Import relevant models from the main application

# Setup the Flask application for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
            # Seed the database with initial data
            student = Student(name="John Doe")
            course = Course(title="Mathematics")
            db.session.add(student)
            db.session.add(course)
            db.session.commit()
        yield client
        with app.app_context():
            db.session.remove()  # Clean up session

def test_associate_courses_success(client):
    """Test associating courses to a student successfully."""
    response = client.put('/students/1/courses', json={"course_ids": [1]})  # Assuming course ID 1 exists
    assert response.status_code == 200
    assert response.json == {"message": "Courses associated successfully."}

def test_associate_courses_no_selection(client):
    """Test associating courses to a student with no courses selected."""
    response = client.put('/students/1/courses', json={"course_ids": []})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E001", "message": "Course IDs cannot be empty."}}

def test_get_student_with_courses(client):
    """Test retrieving a student record with associated courses."""
    client.put('/students/1/courses', json={"course_ids": [1]})  # Associate course first
    response = client.get('/students/1')
    assert response.status_code == 200
    assert "courses" in response.json  # Check if course details are included
    assert len(response.json['courses']) == 1  # Expecting one associated course

def test_db_initialization(client):
    """Test if the database schema initializes correctly with StudentCourse table."""
    with app.app_context():
        assert 'student_course' in db.engine.table_names()  # Check if the junction table exists
```