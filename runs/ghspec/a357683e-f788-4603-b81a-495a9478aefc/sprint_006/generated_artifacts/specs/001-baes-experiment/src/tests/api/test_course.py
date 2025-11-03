```python
import pytest
from flask import json
from app import create_app, db
from app.models import Course, Teacher

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Create the database tables
            yield testing_client
            db.drop_all()  # Cleanup after tests

def test_assign_teacher_to_course_success(test_client):
    # Create a new Teacher and Course for the test
    teacher = Teacher(name="John Doe", email="john@example.com")
    course = Course(name="Math 101")
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Assign the Teacher to the Course
    response = test_client.patch(f'/courses/{course.id}/assign-teacher', json={'teacher_id': teacher.id})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['teacher_id'] == teacher.id  # Check if the teacher was assigned successfully

def test_retrieve_course_with_assigned_teacher(test_client):
    # Create a Teacher and Course, and assign the Teacher to the Course
    teacher = Teacher(name="Jane Smith", email="jane@example.com")
    course = Course(name="Science 101")
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Assign the Teacher to the Course
    test_client.patch(f'/courses/{course.id}/assign-teacher', json={'teacher_id': teacher.id})

    # Retrieve the Course
    response = test_client.get(f'/courses/{course.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['teacher']['name'] == teacher.name  # Ensure the correct teacher name is returned

def test_remove_teacher_from_course_success(test_client):
    # Create a new Teacher and Course for removal test
    teacher = Teacher(name="Robert Brown", email="robert@example.com")
    course = Course(name="History 101")
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Assign the Teacher to the Course first
    test_client.patch(f'/courses/{course.id}/assign-teacher', json={'teacher_id': teacher.id})

    # Now remove the Teacher from the Course
    response = test_client.patch(f'/courses/{course.id}/remove-teacher')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['teacher_id'] is None  # Check that the teacher has been removed successfully

def test_query_courses_by_teacher(test_client):
    # Create Teacher and Courses for querying
    teacher = Teacher(name="Emily White", email="emily@example.com")
    course1 = Course(name="Geography 101")
    course2 = Course(name="Biology 101")
    db.session.add(teacher)
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    # Assign both courses to the same teacher
    test_client.patch(f'/courses/{course1.id}/assign-teacher', json={'teacher_id': teacher.id})
    test_client.patch(f'/courses/{course2.id}/assign-teacher', json={'teacher_id': teacher.id})

    # Query courses for the specific teacher
    response = test_client.get(f'/teachers/{teacher.id}/courses')
    assert response.status_code == 200
    data = json.loads(response.data)
    # Check that both courses are returned correctly
    assert len(data) == 2
    assert data[0]['name'] in ["Geography 101", "Biology 101"]
    assert data[1]['name'] in ["Geography 101", "Biology 101"]
```