import pytest
from flask import Flask, jsonify
from extensions import db
from models.course import Course  # Assuming this is where the Course model is located
from models.teacher import Teacher  # Assuming this is where the Teacher model is located
from api.routes.courses import courses_bp  # Assuming the courses API is set up in this module

@pytest.fixture
def app():
    """Create a new Flask application instance for testing."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
    app.register_blueprint(courses_bp)  # Register the courses API blueprint
    with app.app_context():
        db.create_all()  # Create database tables
    yield app

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

@pytest.fixture
def create_teacher():
    """Helper function to create a teacher in the in-memory database."""
    teacher = Teacher(name='John Doe', email='john.doe@example.com')
    db.session.add(teacher)
    db.session.commit()
    return teacher

@pytest.fixture
def create_course():
    """Helper function to create a course in the in-memory database."""
    course = Course()
    db.session.add(course)
    db.session.commit()
    return course

def test_assign_teacher_to_invalid_course(client, create_teacher):
    """Test error response when assigning a teacher to a non-existent course."""
    response = client.post('/courses/999/assign-teacher', json={"teacher_id": create_teacher.id})
    
    assert response.status_code == 400
    assert response.get_json() == {
        "error": {
            "code": "E001",
            "message": "Invalid Course ID or Teacher ID."
        }
    }

def test_assign_teacher_to_invalid_teacher(client, create_course):
    """Test error response when assigning an invalid teacher to a valid course."""
    response = client.post(f'/courses/{create_course.id}/assign-teacher', json={"teacher_id": 999})
    
    assert response.status_code == 400
    assert response.get_json() == {
        "error": {
            "code": "E001",
            "message": "Invalid Course ID or Teacher ID."
        }
    }

def test_assign_teacher_successfully(client, create_course, create_teacher):
    """Test successful assignment of a teacher to a course."""
    response = client.post(f'/courses/{create_course.id}/assign-teacher', json={"teacher_id": create_teacher.id})
    
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data["message"] == "Teacher assigned successfully."
    assert response_data["course"]["id"] == create_course.id
    assert response_data["course"]["assigned_teacher_id"] == create_teacher.id

def test_view_course_with_teacher(client, create_course, create_teacher):
    """Test viewing course details including assigned teacher."""
    client.post(f'/courses/{create_course.id}/assign-teacher', json={"teacher_id": create_teacher.id})
    
    response = client.get(f'/courses/{create_course.id}')
    
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data["id"] == create_course.id
    assert response_data["assigned_teacher_id"] == create_teacher.id
    # Check for other course details if needed
