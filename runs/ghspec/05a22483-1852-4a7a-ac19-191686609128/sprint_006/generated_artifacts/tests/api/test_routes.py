```python
import pytest
from flask import json
from your_app import create_app, db  # make sure to replace with actual import paths
from your_app.models import Course, Teacher  # include the new Course model

@pytest.fixture
def client():
    app = create_app('testing')  # use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create the database schema
            yield client  # yield the test client
            db.drop_all()  # cleanup after tests

@pytest.fixture
def sample_teacher(client):
    """Create a sample teacher for testing."""
    teacher = Teacher(name="Jane Smith", email="jane@example.com")
    db.session.add(teacher)
    db.session.commit()
    return teacher

@pytest.fixture
def sample_course(client, sample_teacher):
    """Create a sample course for testing with an assigned teacher."""
    course = Course(title="Introduction to Testing", teacher_id=sample_teacher.id)
    db.session.add(course)
    db.session.commit()
    return course

def test_assign_teacher_to_course(client, sample_course, sample_teacher):
    """Test the API endpoint for assigning a teacher to a course."""
    response = client.post(f'/courses/{sample_course.id}/assign_teacher', 
                           data=json.dumps({'teacher_id': sample_teacher.id}),
                           content_type='application/json')
    
    assert response.status_code == 200  # Check for successful response
    assert response.json['message'] == 'Teacher assigned successfully'  # Check message
    
    # Validate that the teacher is now assigned in the database
    updated_course = Course.query.get(sample_course.id)
    assert updated_course.teacher_id == sample_teacher.id

def test_get_course_details(client, sample_course):
    """Test the API endpoint for retrieving course details."""
    response = client.get(f'/courses/{sample_course.id}')
    
    assert response.status_code == 200  # Check for successful response
    assert response.json['id'] == sample_course.id  # Check course ID
    assert response.json['teacher_id'] == sample_course.teacher_id  # Check teacher ID assignment
    assert response.json['title'] == sample_course.title  # Check course title
```