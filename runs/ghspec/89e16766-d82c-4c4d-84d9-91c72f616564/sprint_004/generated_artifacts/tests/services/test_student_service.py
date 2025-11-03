```python
import pytest
from flask import json
from app import create_app, db
from app.models import Student, Course, StudentCourse  # Assuming there is a StudentCourse model for the association

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables for testing purposes
            yield client
            db.drop_all()  # Cleanup after tests

def test_associate_courses_to_student(test_client):
    # Setup: Create a student and some courses for testing
    student = Student(name='Test Student')
    db.session.add(student)
    db.session.commit()

    course1 = Course(name='Course 1')
    course2 = Course(name='Course 2')
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    # Test associating courses with the student
    response = test_client.post('/api/students/associate_courses', 
                                 data=json.dumps({
                                     'student_id': student.id,
                                     'course_ids': [course1.id, course2.id]
                                 }), 
                                 content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert 'student' in data
    assert len(data['student']['courses']) == 2  # Check if two courses are associated

def test_retrieve_student_with_courses(test_client):
    # Setup: Create a new student with associated courses
    student = Student(name='Another Test Student')
    db.session.add(student)
    db.session.commit()

    course1 = Course(name='Course A')
    course2 = Course(name='Course B')
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    # Associate courses
    db.session.add(StudentCourse(student_id=student.id, course_id=course1.id))
    db.session.add(StudentCourse(student_id=student.id, course_id=course2.id))
    db.session.commit()

    # Test retrieving the student with associated courses
    response = test_client.get(f'/api/students/{student.id}')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == student.id
    assert len(data['courses']) == 2  # Check if two courses are returned

def test_associate_courses_invalid_student(test_client):
    # Test attempting to associate courses with a non-existent student
    response = test_client.post('/api/students/associate_courses', 
                                 data=json.dumps({
                                     'student_id': 9999,  # Non-existent student ID
                                     'course_ids': [1, 2]
                                 }), 
                                 content_type='application/json')
    
    assert response.status_code == 400  # Expect 400 Bad Request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E001'  # Check for specific error code
    assert 'Invalid student ID' in data['error']['message']

def test_associate_courses_invalid_course(test_client):
    # Setup: Create a student for testing
    student = Student(name='Sample Student')
    db.session.add(student)
    db.session.commit()

    # Attempt to associate a non-existent course
    response = test_client.post('/api/students/associate_courses', 
                                 data=json.dumps({
                                     'student_id': student.id,
                                     'course_ids': [9999]  # Non-existent course ID
                                 }), 
                                 content_type='application/json')
    
    assert response.status_code == 400  # Expect 400 Bad Request
    data = json.loads(response.data)
    assert data['error']['code'] == 'E002'  # Check for specific error code
    assert 'Invalid course ID' in data['error']['message']
```