```python
import pytest
from flask import json
from src.app import create_app  # Import the Flask application factory
from src.models import db, Course, Teacher  # Import the Course and Teacher models for testing

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    # Set up the database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create database tables
        yield app.test_client()  # This provides access to the app's test client

# Test case to verify that an admin can successfully create a course with a teacher
def test_create_course_with_teacher(client):
    # Setup a teacher for association
    teacher = Teacher(name="John Doe")
    db.session.add(teacher)
    db.session.commit()

    # Create a course associated with the teacher
    course_data = {
        'title': 'Math 101',
        'description': 'Introduction to Mathematics',
        'teacher_id': teacher.id
    }
    response = client.post('/courses', data=json.dumps(course_data), content_type='application/json')
    
    assert response.status_code == 201  # Course should be created successfully
    assert response.json['message'] == 'Course created successfully'
    created_course = Course.query.filter_by(title='Math 101').first()
    assert created_course is not None
    assert created_course.teacher_id == teacher.id

# Test case to confirm that an admin can change the teacher for an existing course
def test_update_course_teacher(client):
    # Setup a teacher and a course
    teacher1 = Teacher(name="John Doe")
    teacher2 = Teacher(name="Jane Smith")
    db.session.add(teacher1)
    db.session.add(teacher2)
    db.session.commit()

    course = Course(title='Physics 101', teacher_id=teacher1.id)
    db.session.add(course)
    db.session.commit()

    # Update the course to assign it a different teacher
    update_data = {
        'teacher_id': teacher2.id
    }
    response = client.put(f'/courses/{course.id}', data=json.dumps(update_data), content_type='application/json')
    
    assert response.status_code == 200  # Update should succeed
    assert response.json['message'] == 'Course updated successfully'
    updated_course = Course.query.get(course.id)
    assert updated_course.teacher_id == teacher2.id

# Test case to check retrieval of course details including teacher info
def test_retrieve_course_with_teacher(client):
    # Setup a teacher and a course
    teacher = Teacher(name="John Doe")
    course = Course(title='History 101', teacher_id=None)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Assign the teacher to the course
    course.teacher_id = teacher.id
    db.session.commit()

    # Retrieve the course details
    response = client.get(f'/courses/{course.id}')
    
    assert response.status_code == 200  # Retrieval should succeed
    assert response.json['teacher']['name'] == teacher.name  # Teacher info should be accurate

# Test case to create a course without a teacher
def test_create_course_without_teacher(client):
    course_data = {
        'title': 'Biology 101',
        'description': 'Introduction to Biology',
        'teacher_id': None
    }
    response = client.post('/courses', data=json.dumps(course_data), content_type='application/json')
    
    assert response.status_code == 201  # Course should be created successfully
    assert response.json['message'] == 'Course created successfully'
    created_course = Course.query.filter_by(title='Biology 101').first()
    assert created_course is not None
    assert created_course.teacher_id is None  # Teacher ID should be None

# Test case to handle assigning a nonexistent teacher
def test_assign_nonexistent_teacher(client):
    course_data = {
        'title': 'Chemistry 101',
        'description': 'Introduction to Chemistry',
        'teacher_id': 9999  # Nonexistent teacher ID
    }
    response = client.post('/courses', data=json.dumps(course_data), content_type='application/json')
    
    assert response.status_code == 400  # Should fail due to nonexistent teacher ID
    assert response.json['error']['code'] == 'E001'  # Expecting specific error code
    assert 'Teacher does not exist' in response.json['error']['message']  # Check error message
```