```python
import pytest
from app import create_app, db
from models.teacher import Teacher
from models.course import Course

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()  # Create the database and tables
        yield app.test_client()
        db.drop_all()  # Clean up after tests

def test_create_teacher(client):
    # Test creating a teacher with valid data
    response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json['id'] is not None

def test_assign_teacher_to_course(client):
    # Setup: Create a course and a teacher
    teacher_response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    course_response = client.post('/courses', json={"name": "Math 101", "level": "Beginner"})

    teacher_id = teacher_response.json['id']
    course_id = course_response.json['id']
    
    # Scenario: Successful assignment
    response = client.post(f'/courses/{course_id}/assign-teacher', json={"teacher_id": teacher_id})
    assert response.status_code == 200
    assert response.json['teacher_id'] == teacher_id

def test_assign_teacher_with_invalid_teacher_id(client):
    # Setup: Create a course
    course_response = client.post('/courses', json={"name": "Math 101", "level": "Beginner"})
    course_id = course_response.json['id']
    
    # Scenario: Attempt to assign an invalid teacher ID
    response = client.post(f'/courses/{course_id}/assign-teacher', json={"teacher_id": 999})  # Non-existent ID
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E002", "message": "Teacher ID does not exist."}}

def test_assign_teacher_with_invalid_course_id(client):
    # Scenario: Attempt to assign a teacher to a non-existent course
    response = client.post('/courses/999/assign-teacher', json={"teacher_id": 1})  # Assuming 1 is a valid teacher ID
    assert response.status_code == 404
    assert response.json == {"error": {"code": "E003", "message": "Course ID does not exist."}}
```