import pytest
from flask import json
from app import create_app, db
from app.models import Student, StudentCourse

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables for testing purposes
            yield client
            db.drop_all()  # Cleanup after tests

def test_associate_student_with_courses(test_client):
    # Test associating a student with courses
    response = test_client.post('/students/1/courses', json={
        'course_ids': [1, 2]
    })
    assert response.status_code == 200
    assert response.json['message'] == "Student associated with courses successfully."

def test_get_student_with_courses(test_client):
    # Test retrieving a student along with their associated courses
    response = test_client.get('/students/1')  # Assuming the first student fetches
    assert response.status_code == 200
    assert 'courses' in response.json  # Check if the response includes course information

def test_associate_student_with_invalid_course(test_client):
    # Test response for associating a student with a non-existent course
    response = test_client.post('/students/1/courses', json={
        'course_ids': [999]  # Assuming 999 is an invalid course ID
    })
    assert response.status_code == 400  # Expecting a bad request status code
    assert response.json['error']['code'] == "E001"  # Example error code
    assert "Invalid course ID" in response.json['error']['message']  # Expect an appropriate message

def test_get_non_existent_student(test_client):
    # Test response for retrieving a non-existent student
    response = test_client.get('/students/999')  # Assuming 999 is an invalid student ID
    assert response.status_code == 404  # Expecting not found status code
    assert response.json['error']['code'] == "E002"  # Example error code
    assert "Student not found" in response.json['error']['message']  # Expect an appropriate message