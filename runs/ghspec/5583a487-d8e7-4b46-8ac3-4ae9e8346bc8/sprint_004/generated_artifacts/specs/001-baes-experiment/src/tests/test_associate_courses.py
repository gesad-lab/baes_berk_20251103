```python
import pytest
from flask import jsonify
from app import app, db, Course, Student  # Import the models from the main application

# Setup the Flask application for testing with an in-memory SQLite database
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
            # Populate dummy data for testing
            course1 = Course(id=1, name='Mathematics')
            course2 = Course(id=2, name='Science')
            student = Student(id=1, name='John Doe')
            db.session.add_all([course1, course2, student])
            db.session.commit()  # Commit changes to the in-memory database
        yield client  # Yield the test client to the tests

# Test case for associating courses with a student
def test_associate_courses(client):
    # Given one student and two courses
    student_id = 1
    course_ids = [1, 2]  # Courses to associate with the student

    # When I send a PUT request to associate courses
    response = client.put(f'/students/{student_id}/courses', json={'course_ids': course_ids})

    # Then the response should be 200 OK indicating success
    assert response.status_code == 200
    assert response.json == {'message': 'Courses associated successfully'}

    # Verify that courses are indeed associated
    student = Student.query.get(student_id)
    assert len(student.courses) == 2  # Check that two courses are associated

# Test case for invalid course association (no courses provided)
def test_associate_courses_no_courses(client):
    student_id = 1
    # When I send a PUT request with no course IDs
    response = client.put(f'/students/{student_id}/courses', json={'course_ids': []})

    # Then I should receive a 400 Bad Request
    assert response.status_code == 400
    assert response.json == {'error': {'code': 'E001', 'message': 'At least one course ID must be provided'}}

# Test case for retrieving a student including associated courses
def test_get_student_with_courses(client):
    student_id = 1
    course_ids = [1, 2]
    client.put(f'/students/{student_id}/courses', json={'course_ids': course_ids})

    # When I send a GET request for the student
    response = client.get(f'/students/{student_id}')

    # Then the response should be 200 OK and include student and associated course details
    assert response.status_code == 200
    assert response.json == {
        'id': student_id,
        'name': 'John Doe',
        'courses': [{'id': 1, 'name': 'Mathematics'}, {'id': 2, 'name': 'Science'}]
    }
```