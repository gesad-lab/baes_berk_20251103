```python
import pytest
from app import create_app, db
from models.teacher import Teacher
from models.student import Student  # Assuming Student is an existing model
from models.course import Course      # Assuming Course is an existing model

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')  # Use appropriate config for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
            yield client
            db.drop_all()  # Clean up after tests

def test_assign_teacher_to_course(test_client):
    # Scenario: Successful assignment of a teacher to a course
    # Assuming the data is already present in the database for this test
    response = test_client.post('/courses/1/assign-teacher', json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json['teacher_id'] == 1
    assert response.json['id'] == 1  # Verify the updated course ID also

def test_assign_teacher_with_invalid_teacher_id(test_client):
    # Scenario: Attempt to assign a teacher using an invalid teacher ID
    response = test_client.post('/courses/1/assign-teacher', json={"teacher_id": 999})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E002", "message": "Teacher ID does not exist."}}

def test_assign_teacher_with_invalid_course_id(test_client):
    # Scenario: Attempt to assign a teacher to a non-existent course
    response = test_client.post('/courses/999/assign-teacher', json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json == {"error": {"code": "E003", "message": "Course ID does not exist."}}

def test_data_integrity_after_assignment(test_client):
    # Scenario: Validate integrity of existing data after assignment
    # Ensure any necessary data is pre-populated in the test database
    teacher = Teacher(name="Test Teacher", email="teacher@test.com")
    db.session.add(teacher)
    db.session.commit()
    
    course = Course(name="Test Course", level="Beginner")
    db.session.add(course)
    db.session.commit()

    # Assign the teacher to the course
    test_client.post(f'/courses/{course.id}/assign-teacher', json={"teacher_id": teacher.id})

    # Check if the teacher assignment didn't affect other data
    all_teachers = Teacher.query.all()
    assert len(all_teachers) == 1  # Ensure teacher remains intact
    assert all_teachers[0].name == "Test Teacher"

    all_courses = Course.query.all()
    assert len(all_courses) == 1  # Ensure course remains intact
    assert all_courses[0].name == "Test Course"
```