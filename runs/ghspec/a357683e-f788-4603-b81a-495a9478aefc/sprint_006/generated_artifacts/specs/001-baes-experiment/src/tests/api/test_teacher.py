```python
import pytest
from flask import json
from app import create_app, db
from app.models import Teacher, Course

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Create the database tables
            yield testing_client  # Directly use the testing client in test cases
            db.drop_all()  # Drop the database tables after testing

def test_remove_teacher_from_course_success(test_client):
    # Setup - Create a teacher and course
    teacher = Teacher(name="John Doe", email="john@example.com")
    course = Course(name="Math 101", teacher_id=teacher.id)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Ensure the course has the teacher assigned
    response = test_client.get(f'/courses/{course.id}')
    assert response.status_code == 200
    assert response.json['teacher_id'] == teacher.id

    # Remove teacher from the course
    response = test_client.patch(f'/courses/{course.id}/remove-teacher')
    assert response.status_code == 200
    assert 'teacher_id' not in response.json  # Confirm that teacher_id is removed

    # Verify that the removal was successful
    updated_course = Course.query.get(course.id)
    assert updated_course.teacher_id is None

def test_remove_teacher_from_course_invalid_course(test_client):
    # Attempt to remove teacher from a non-existing course
    response = test_client.patch('/courses/999/remove-teacher')
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E404'  # Adjust error code as per implementation expectations

def test_remove_teacher_from_course_already_empty(test_client):
    # Setup - Create a teacher and course with no assigned teacher
    teacher = Teacher(name="Jane Doe", email="jane@example.com")
    course = Course(name="Science 101", teacher_id=None)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Attempt to remove teacher from a course with no teacher assigned
    response = test_client.patch(f'/courses/{course.id}/remove-teacher')
    assert response.status_code == 400  # Expecting a bad request
    assert response.json['error']['code'] == 'E400'  # Adjust error code as per the implementation expectations
```