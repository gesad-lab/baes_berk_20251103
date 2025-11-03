import pytest
from flask import json
from app import app, db
from models import Student, Course, StudentCourse

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client
        with app.app_context():
            db.drop_all()  # Cleanup after tests

def test_associate_student_with_courses(client):
    """Test associating a student with courses."""
    # Setup: Create a student and a few courses
    student = Student(name='John Doe')
    course1 = Course(title='Mathematics')
    course2 = Course(title='History')

    with app.app_context():
        db.session.add(student)
        db.session.add(course1)
        db.session.add(course2)
        db.session.commit()

        # Associate courses with the student
        student_course1 = StudentCourse(student_id=student.id, course_id=course1.id)
        student_course2 = StudentCourse(student_id=student.id, course_id=course2.id)
        db.session.add(student_course1)
        db.session.add(student_course2)
        db.session.commit()

    # Verify that the student has courses associated
    response = client.get(f'/students/{student.id}/courses')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2  # Should have two courses
    assert course1.title in [course['title'] for course in data]
    assert course2.title in [course['title'] for course in data]

def test_retrieve_students_courses(client):
    """Test retrieving all courses associated with a student."""
    student = Student(name='Jane Doe')
    course = Course(title='Biology')

    with app.app_context():
        db.session.add(student)
        db.session.add(course)
        db.session.commit()
        
        # Associate the course with the student
        student_course = StudentCourse(student_id=student.id, course_id=course.id)
        db.session.add(student_course)
        db.session.commit()

    # Retrieve courses for the student
    response = client.get(f'/students/{student.id}/courses')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1  # Should have one course
    assert data[0]['title'] == course.title

def test_student_data_integrity(client):
    """Test that student data remains intact after associations."""
    student = Student(name='Michael Smith')
    
    with app.app_context():
        db.session.add(student)
        db.session.commit()
        
        # Associate a course
        course = Course(title='Physics')
        student_course = StudentCourse(student_id=student.id, course_id=course.id)
        db.session.add(course)
        db.session.add(student_course)
        db.session.commit()
    
    # Verify that original student data is unchanged
    fetched_student = Student.query.get(student.id)
    assert fetched_student.name == 'Michael Smith'

def test_database_migration_verification(client):
    """Test to verify database migration structure."""
    # Here we would run checks specific to migrations, for this example,
    # it suffices to check if new tables exist.
    with app.app_context():
        assert 'student_courses' in db.engine.table_names()  # Check if table exists
        assert 'students' in db.engine.table_names()  # Ensure core tables are still there
        assert 'courses' in db.engine.table_names()  # Ensure courses table is still intact