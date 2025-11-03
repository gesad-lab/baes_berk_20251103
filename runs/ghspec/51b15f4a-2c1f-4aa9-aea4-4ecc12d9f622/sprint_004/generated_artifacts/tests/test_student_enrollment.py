```python
import pytest
from app import create_app, db
from models.enrollment import Enrollment
from models.student import Student
from models.course import Course

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')  # Initialize app with testing configuration
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()  # Setup test database environment
        yield testing_client  # This is where the testing happens!
        db.drop_all()  # Teardown after tests

def test_enroll_student_success(test_client):
    """ Test case for successfully enrolling a student in a course. """
    # Create a student and a course to perform enrollment on
    new_student = Student(name='John Doe')
    new_course = Course(name='Mathematics', level='Beginner')
    
    with test_client.application.app_context():
        db.session.add(new_student)
        db.session.add(new_course)
        db.session.commit()
    
    response = test_client.post('/enroll', json={
        'student_id': new_student.id,
        'course_id': new_course.id
    })
    
    assert response.status_code == 201  # Check that the enrollment was created successfully
    assert response.json['message'] == 'Enrollment successful'  # Check for confirmation message

def test_enroll_student_invalid_student(test_client):
    """ Test case for attempting to enroll a non-existent student. """
    mock_course_id = 1  # Assume this course exists

    response = test_client.post('/enroll', json={
        'student_id': 99999,  # Non-existent student ID
        'course_id': mock_course_id
    })
    
    assert response.status_code == 400  # Expect bad request
    assert response.json['error']['code'] == 'E001'  # Custom error code for invalid student
    assert 'Student not found' in response.json['error']['message']  # Assert error message

def test_get_student_courses(test_client):
    """ Test case for retrieving a list of courses a student is enrolled in. """
    # Create a new student and course for enrollment
    new_student = Student(name='Jane Doe')
    new_course = Course(name='Physics', level='Intermediate')
    
    with test_client.application.app_context():
        db.session.add(new_student)
        db.session.add(new_course)
        db.session.commit()

        # Enroll student in the created course
        enrollment = Enrollment(student_id=new_student.id, course_id=new_course.id)
        db.session.add(enrollment)
        db.session.commit()
    
    # Now retrieve the courses for the student
    response = test_client.get(f'/students/{new_student.id}/courses')
    
    assert response.status_code == 200  # Check that the retrieval was successful
    assert len(response.json['courses']) == 1  # Student should be enrolled in one course
    assert response.json['courses'][0]['name'] == new_course.name  # Verify course name matches

def test_enroll_student_invalid_course(test_client):
    """ Test case for attempting to enroll a student in a non-existent course. """
    new_student = Student(name='Alice Smith')
    
    with test_client.application.app_context():
        db.session.add(new_student)
        db.session.commit()

    response = test_client.post('/enroll', json={
        'student_id': new_student.id,
        'course_id': 99999  # Non-existent course ID
    })
    
    assert response.status_code == 400  # Expect bad request
    assert response.json['error']['code'] == 'E002'  # Custom error code for invalid course
    assert 'Course not found' in response.json['error']['message']  # Assert error message
```