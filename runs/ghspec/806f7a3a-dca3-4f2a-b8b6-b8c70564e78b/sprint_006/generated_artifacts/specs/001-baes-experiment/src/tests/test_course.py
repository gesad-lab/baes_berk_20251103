```python
import pytest
from flask import json
from app import create_app, db
from models.course import Course  # Import the Course model
from models.teacher import Teacher  # Import the Teacher model
from routes.course_routes import course_bp  # Import the course routes

@pytest.fixture
def client():
    app = create_app('testing')  # Use a separate testing configuration
    app.register_blueprint(course_bp)  # Register the course routes
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_database():
    """Fixture to set up the database for testing."""
    db.create_all()  # Create the tables
    teacher = Teacher(first_name="John", last_name="Doe", email="john.doe@example.com")
    course = Course(title="Mathematics 101")
    db.session.add(teacher)  # Add a teacher
    db.session.add(course)  # Add a course
    db.session.commit()  # Commit the session

    yield db  # Return the database session for use in tests

    db.drop_all()  # Drop tables after tests

def test_add_teacher_to_course(client, init_database):
    """Test the API endpoint to add a teacher to a course."""
    # Retrieve the ID of the added teacher and course
    teacher = Teacher.query.first()
    course = Course.query.first()

    # Create a request payload to assign a teacher to a course
    response = client.put(f'/courses/{course.id}/assign_teacher', 
                          data=json.dumps({'teacher_id': teacher.id}),
                          content_type='application/json')

    assert response.status_code == 200  # Check if the status code is OK
    assert response.json['message'] == 'Teacher assigned to course successfully.'
    
    # Verify that the course now has the teacher_id set
    course.refresh()  # Refresh course instance from the database
    assert course.teacher_id == teacher.id  # Confirm teacher_id is updated

def test_get_course_details(client, init_database):
    """Test the API endpoint to retrieve course details including the teacher info."""
    teacher = Teacher.query.first()  # Get the first teacher
    course = Course.query.first()  # Get the first course
    # Assign teacher to the course
    course.teacher_id = teacher.id
    db.session.commit()

    response = client.get(f'/courses/{course.id}')

    assert response.status_code == 200  # Check if the status code is OK
    assert response.json['title'] == course.title  # Verify course title
    assert response.json['teacher'] == {'name': f"{teacher.first_name} {teacher.last_name}", 
                                         'email': teacher.email}  # Verify teacher details

def test_assign_teacher_invalid_id(client, init_database):
    """Test assigning a teacher with an invalid ID."""
    course = Course.query.first()
    # Attempt to assign a non-existent teacher
    response = client.put(f'/courses/{course.id}/assign_teacher', 
                          data=json.dumps({'teacher_id': 9999}),  # An ID that doesn't exist
                          content_type='application/json')

    assert response.status_code == 404  # Expect a Not Found error
    assert response.json['error']['code'] == 'E002'  # Check error code
    assert response.json['error']['message'] == 'Teacher not found.'  # Check error message
```