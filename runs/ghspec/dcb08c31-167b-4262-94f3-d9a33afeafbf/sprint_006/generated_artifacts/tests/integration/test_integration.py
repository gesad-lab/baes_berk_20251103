```python
import json
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.teacher import Teacher  # Assuming Teacher model is defined in models.teacher
from models.course import Course  # Assuming Course model is defined in models.course

# Initialize the Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
db = SQLAlchemy(app)

@pytest.fixture
def client():
    """Fixture for creating a test client."""
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_database():
    """Fixture to initialize the in-memory database and create test data."""
    db.create_all()
    
    # Create a Teacher and a Course for tests
    teacher = Teacher(name="John Doe", email="john@example.com")
    db.session.add(teacher)
    db.session.commit()
    
    course = Course(title="Math 101", description="Basic Mathematics", teacher_id=None)
    db.session.add(course)
    db.session.commit()
    
    yield db  # This yields the database session to the tests

    db.drop_all()  # Cleanup after tests

def test_assign_teacher_to_course(client, init_database):
    """Test assigning a teacher to a course successfully."""
    # Get the course and teacher from the initialized data
    course = Course.query.first()
    teacher = Teacher.query.first()
    
    # Assign the teacher to the course
    response = client.patch(f'/courses/{course.id}', json={'teacher_id': teacher.id})
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['teacher_id'] == teacher.id  # Check if the course has the correct teacher assigned
    assert data['teacher']['name'] == teacher.name  # Check the teacher's name is included in the response

def test_teacher_assignment_invalid_id(client, init_database):
    """Test assigning a teacher to a course with an invalid teacher ID."""
    course = Course.query.first()
    
    # Try to assign a non-existing teacher
    response = client.patch(f'/courses/{course.id}', json={'teacher_id': 9999})
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Confirm the error code for invalid teacher
    assert data['error']['message'] == 'Teacher not found'  # Check the error message

def test_get_course_information(client, init_database):
    """Test retrieving course information including assigned teacher details."""
    course = Course.query.first()
    teacher = Teacher.query.first()
    
    # Assign teacher to the course first
    course.teacher_id = teacher.id
    db.session.commit()
    
    # Retrieve course details
    response = client.get(f'/courses/{course.id}')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['teacher_id'] == teacher.id  # Check if the correct teacher is associated with the course
    assert data['teacher']['email'] == teacher.email  # Ensure the teacher's email is returned
```