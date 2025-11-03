```python
import pytest
from flask import json
from app import create_app, db
from models import Student, Course, Teacher  # Importing the Teacher model
from teacher_service import create_teacher_service  # Assuming service layer exists

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

def test_assign_teacher(test_client):
    """Test for assigning a teacher to a course."""
    # First, create a course and a teacher to work with
    teacher = Teacher(name='John Doe')
    course = Course(title='Mathematics')
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Assign the teacher to the course
    response = test_client.put(f'/courses/{course.id}/assign-teacher/{teacher.id}')
    assert response.status_code == 200  # Assuming success returns 200

    # Verify that the teacher has been assigned
    updated_course = Course.query.get(course.id)
    assert updated_course.teacher_id == teacher.id

def test_unassign_teacher(test_client):
    """Test for unassigning a teacher from a course."""
    # Create a course and a teacher to work with
    teacher = Teacher(name='Jane Smith')
    course = Course(title='Science', teacher_id=teacher.id)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Unassign the teacher from the course
    response = test_client.delete(f'/courses/{course.id}/unassign-teacher')
    assert response.status_code == 204  # Assuming success returns 204

    # Verify that the teacher has been unassigned
    updated_course = Course.query.get(course.id)
    assert updated_course.teacher_id is None  # Teacher ID should be None

def test_get_course_with_teacher(test_client):
    """Test for retrieving course details with teacher information."""
    teacher = Teacher(name='Alice Johnson')
    course = Course(title='English Literature', teacher_id=teacher.id)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    response = test_client.get(f'/courses/{course.id}')
    assert response.status_code == 200  # Assuming success returns 200
    response_json = json.loads(response.data)
    
    # Check whether the response includes the teacher details
    assert response_json['teacher']['name'] == teacher.name

def test_list_courses_with_teachers(test_client):
    """Test for listing all courses including assigned teachers."""
    teacher1 = Teacher(name='Mr. Brown')
    teacher2 = Teacher(name='Ms. Green')
    course1 = Course(title='Biology', teacher_id=teacher1.id)
    course2 = Course(title='Chemistry', teacher_id=teacher2.id)
    db.session.add(teacher1)
    db.session.add(teacher2)
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    response = test_client.get('/courses')
    assert response.status_code == 200  # Assuming success returns 200
    response_json = json.loads(response.data)

    # Check if we have the correct number of courses listed
    assert len(response_json) == 2

    # Verify that the teachers' names are included
    assert any(course['teacher']['name'] == teacher1.name for course in response_json)
    assert any(course['teacher']['name'] == teacher2.name for course in response_json)

```