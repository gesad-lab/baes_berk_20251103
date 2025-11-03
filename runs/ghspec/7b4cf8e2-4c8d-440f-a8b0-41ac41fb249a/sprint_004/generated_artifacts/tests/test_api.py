import pytest
from flask import json
from app import create_app, db
from models import Student, Course, StudentCourse

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests


@pytest.fixture(scope='function')
def initialized_database():
    with db.session.begin():
        test_student = Student(name="John Doe")
        test_course = Course(title="Math 101")
        db.session.add(test_student)
        db.session.add(test_course)
        db.session.commit()

        yield test_student, test_course

        db.session.query(StudentCourse).delete()  # Cleanup junction table
        db.session.query(Student).delete()  # Cleanup test student
        db.session.query(Course).delete()  # Cleanup test course
        db.session.commit()


def test_enroll_student_in_course(test_client, initialized_database):
    student, course = initialized_database

    response = test_client.post('/api/enroll', json={
        'student_id': student.id,
        'course_id': course.id
    })

    assert response.status_code == 200
    assert response.json['message'] == 'Enrollment successful'
    assert StudentCourse.query.count() == 1  # Check if enrollment is created


def test_enroll_student_in_course_invalid(test_client, initialized_database):
    student, _ = initialized_database

    # Attempt to enroll in a non-existent course
    response = test_client.post('/api/enroll', json={
        'student_id': student.id,
        'course_id': 9999  # Invalid course ID
    })

    assert response.status_code == 404
    assert response.json['error']['code'] == 'E404'
    assert response.json['error']['message'] == 'Course not found'


def test_enroll_student_already_enrolled(test_client, initialized_database):
    student, course = initialized_database

    # Enroll first time
    enroll_response = test_client.post('/api/enroll', json={
        'student_id': student.id,
        'course_id': course.id
    })
    assert enroll_response.status_code == 200

    # Try enrolling again in the same course
    enroll_response = test_client.post('/api/enroll', json={
        'student_id': student.id,
        'course_id': course.id
    })

    assert enroll_response.status_code == 400
    assert enroll_response.json['error']['code'] == 'E400'
    assert enroll_response.json['error']['message'] == 'Student already enrolled in this course'


def test_remove_student_from_course(test_client, initialized_database):
    student, course = initialized_database

    # Enroll the student first
    test_client.post('/api/enroll', json={
        'student_id': student.id,
        'course_id': course.id
    })

    # Now remove the student from the course
    response = test_client.post('/api/remove', json={
        'student_id': student.id,
        'course_id': course.id
    })

    assert response.status_code == 200
    assert response.json['message'] == 'Removal successful'
    assert StudentCourse.query.count() == 0  # Check if enrollment is deleted


def test_remove_student_from_course_not_enrolled(test_client, initialized_database):
    student, course = initialized_database

    # Attempt to remove a student not enrolled in any course
    response = test_client.post('/api/remove', json={
        'student_id': student.id,
        'course_id': course.id
    })

    assert response.status_code == 400
    assert response.json['error']['code'] == 'E400'
    assert response.json['error']['message'] == 'Student not enrolled in this course'