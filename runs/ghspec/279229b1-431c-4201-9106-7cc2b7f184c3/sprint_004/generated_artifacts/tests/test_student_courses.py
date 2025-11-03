```python
import pytest
import json
from your_app_name import create_app, db  # Adjust according to your application structure
from your_app_name.models import Course  # Import existing Course model
from your_app_name.models import Student  # Assuming Student model exists
from your_app_name.models import StudentCourse  # Import relationship model if it exists

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests
    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.drop_all()  # Clean up after tests

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def setup_data(app):
    """Set up dummy data for testing."""
    with app.app_context():
        course1 = Course(name='Mathematics', level='Beginner')
        course2 = Course(name='Science', level='Intermediate')
        student = Student(name='John Doe')

        # Add and commit to the database
        db.session.add(course1)
        db.session.add(course2)
        db.session.add(student)
        db.session.commit()
        
        return student, [course1.id, course2.id]

def test_add_student_courses(client, setup_data):
    student, course_ids = setup_data
    # Associate student with courses
    response = client.post(f'/students/{student.id}/courses', json={'course_ids': course_ids})
    
    assert response.status_code == 200  # Ensure the request was successful

def test_get_student_courses(client, setup_data):
    student, course_ids = setup_data
    # Retrieve associated courses for the student
    response = client.get(f'/students/{student.id}/courses')
    
    assert isinstance(response.json, list)  # Ensure the response is a list
    assert len(response.json) == len(course_ids)  # Ensure it matches expected course count

def test_add_student_courses_invalid_course(client, setup_data):
    student, _ = setup_data
    # Attempt to add a non-existent course to the student
    response = client.post(f'/students/{student.id}/courses', json={'course_ids': [999]})
    
    assert response.status_code == 400  # Expecting a bad request due to invalid course ID
    assert response.json['error']['code'] == 'E001'  # Check for the specific error code
```