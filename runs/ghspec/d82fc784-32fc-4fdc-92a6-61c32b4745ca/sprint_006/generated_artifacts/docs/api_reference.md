```python
import pytest
from app import create_app, db
from app.models import Teacher, Student, Course  # Import necessary models
import json

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables for testing
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after tests

@pytest.fixture
def add_sample_data():
    """Fixture to add sample data for integration tests."""
    teacher = Teacher(name='Sample Teacher')
    student = Student(name='Sample Student')
    course = Course(title='Sample Course', teacher=teacher)

    db.session.add(teacher)
    db.session.add(student)
    db.session.add(course)
    db.session.commit()

    return {
        'teacher': teacher,
        'student': student,
        'course': course
    }

def test_get_courses(client, add_sample_data):
    """Test retrieving the list of courses."""
    response = client.get('/api/v1/courses')
    assert response.status_code == 200
    assert isinstance(json.loads(response.data), list)  # Expecting a list of courses

def test_create_course(client):
    """Test creating a new course."""
    response = client.post('/api/v1/courses', json={
        'title': 'New Course',
        'teacher_id': 1  # Assuming there's a teacher with ID 1
    })

    assert response.status_code == 201
    response_json = json.loads(response.data)
    assert response_json['title'] == 'New Course'

def test_teacher_course_relationship(client, add_sample_data):
    """Test that courses are linked to the correct teacher."""
    response = client.get(f'/api/v1/teachers/{add_sample_data["teacher"].id}/courses')
    
    assert response.status_code == 200
    response_json = json.loads(response.data)

    # Check that the teacher's courses include our sample course
    assert any(course['title'] == add_sample_data['course'].title for course in response_json)
```