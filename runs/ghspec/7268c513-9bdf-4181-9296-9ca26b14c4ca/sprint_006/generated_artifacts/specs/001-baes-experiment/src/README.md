```python
# File: tests/test_course.py

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
        # Create a sample teacher and course for testing
        teacher = Teacher(name="John Doe", email="john.doe@example.com")
        db.session.add(teacher)
        course = Course(name="Math 101", level="Beginner")
        db.session.add(course)
        db.session.commit()
        yield app.test_client()
        db.drop_all()  # Clean up after tests

def test_assign_teacher_to_course(client):
    # Scenario: Successful assignment
    teacher = Teacher.query.first()
    course = Course.query.first()
    assignment_data = {"teacher_id": teacher.id}
    
    response = client.post(f"/courses/{course.id}/assign-teacher", json=assignment_data)
    
    assert response.status_code == 200
    assert response.json["teacher_id"] == teacher.id

def test_assign_teacher_with_invalid_id(client):
    # Scenario: Attempting to assign with a non-existent teacher ID
    course = Course.query.first()
    assignment_data = {"teacher_id": 999}  # Invalid teacher ID
    
    response = client.post(f"/courses/{course.id}/assign-teacher", json=assignment_data)
    
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E002", "message": "Teacher ID does not exist."}}

def test_assign_teacher_with_nonexistent_course(client):
    # Scenario: Attempting to assign a teacher to a non-existent course
    teacher = Teacher.query.first()
    assignment_data = {"teacher_id": teacher.id}
    
    response = client.post("/courses/999/assign-teacher", json=assignment_data)  # Invalid course ID
    
    assert response.status_code == 404
    assert response.json == {"error": {"code": "E003", "message": "Course ID does not exist."}}
```