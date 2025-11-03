```python
import json
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.teacher import Teacher  # Assuming Teacher model is defined in models.teacher
from models.course import Course  # Assuming Course model is defined in models.course

# Initialize the Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
db = SQLAlchemy(app)

@pytest.fixture
def client():
    """A test client for the Flask app."""
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_database():
    """Initialize the database with sample data for testing."""
    db.create_all()
    
    # Adding a sample teacher
    teacher = Teacher(name='John Doe', email='john.doe@example.com')
    db.session.add(teacher)
    
    # Adding a sample course
    course = Course(teacher_id=teacher.id)
    db.session.add(course)
    
    db.session.commit()
    yield db  # This allows the test to use the db instance

    db.drop_all()  # Clean up after tests are executed

def test_assign_teacher_to_course(client, init_database):
    """Test assigning a teacher to a course."""
    # Assuming the course id is 1 and the teacher id is 1
    new_teacher_id = 1
    
    # Making a PATCH request to assign the teacher to the course
    response = client.patch('/courses/1', json={'teacher_id': new_teacher_id})
    
    # Assertions to verify the teacher is assigned correctly
    assert response.status_code == 200  # Ensure success status code
    data = json.loads(response.data)
    assert data['teacher_id'] == new_teacher_id  # Check if the teacher_id is set correctly

def test_assign_teacher_invalid_id(client, init_database):
    """Test assigning a teacher with an invalid ID returns an error."""
    # Making a PATCH request with an invalid teacher id (e.g., non-existent ID)
    response = client.patch('/courses/1', json={'teacher_id': 999})  # Assuming 999 doesn't exist
    
    # Assertions to verify the error response
    assert response.status_code == 404  # Ensure not found status code
    error_data = json.loads(response.data)
    assert error_data['error']['code'] == 'E001'  # Check for specific error code
    assert error_data['error']['message'] == 'Teacher not found.'  # Check for specific error message
```