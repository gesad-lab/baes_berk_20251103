```python
import pytest
from app import app  # Import the Flask app
from flask import json
from models.course import Course  # Import the Course model
from models.teacher import Teacher  # Import the Teacher model
from database import session  # Import the database session


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_validate_course_update_with_existing_course(client):
    """
    Test case for assigning a Teacher to an existing Course.
    
    Expected Outcome: 
    Status code 200, confirms the Teacher is assigned to the Course.
    """
    course = Course(id=1, name="Mathematics", teacher_id=None)  # Sample course
    teacher = Teacher(id=1, name="John Doe")  # Sample teacher
    session.add(course)
    session.add(teacher)
    session.commit()
    
    response = client.put('/api/v1/courses/1/assign_teacher', json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json['message'] == "Teacher assigned successfully."
    
    updated_course = session.query(Course).get(1)
    assert updated_course.teacher_id == 1  # Check if Teacher is assigned


def test_validate_course_update_with_nonexistent_course(client):
    """
    Test case for attempting to assign a Teacher to a non-existent Course.
    
    Expected Outcome: 
    Status code 404, indicates the Course was not found.
    """
    response = client.put('/api/v1/courses/999/assign_teacher', json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json['error']['message'] == "Course not found."


def test_validate_course_update_with_nonexistent_teacher(client):
    """
    Test case for attempting to assign a non-existent Teacher to a Course.
    
    Expected Outcome: 
    Status code 404, indicates the Teacher does not exist.
    """
    course = Course(id=1, name="Mathematics", teacher_id=None)  # Sample course
    session.add(course)
    session.commit()
    
    response = client.put('/api/v1/courses/1/assign_teacher', json={"teacher_id": 999})
    assert response.status_code == 404
    assert response.json['error']['message'] == "Teacher not found."


def test_validate_course_update_multiple_courses_for_teacher(client):
    """
    Test case to check that a Teacher can be assigned to multiple Courses.
    
    Expected Outcome: 
    Status code 200, confirms the Teacher has been assigned to multiple Courses.
    """
    course1 = Course(id=1, name="Mathematics", teacher_id=None)
    course2 = Course(id=2, name="Science", teacher_id=None)
    teacher = Teacher(id=1, name="John Doe")
    
    session.add(course1)
    session.add(course2)
    session.add(teacher)
    session.commit()
    
    response1 = client.put('/api/v1/courses/1/assign_teacher', json={"teacher_id": 1})
    assert response1.status_code == 200

    response2 = client.put('/api/v1/courses/2/assign_teacher', json={"teacher_id": 1})
    assert response2.status_code == 200

    updated_course1 = session.query(Course).get(1)
    updated_course2 = session.query(Course).get(2)
    assert updated_course1.teacher_id == 1
    assert updated_course2.teacher_id == 1
```