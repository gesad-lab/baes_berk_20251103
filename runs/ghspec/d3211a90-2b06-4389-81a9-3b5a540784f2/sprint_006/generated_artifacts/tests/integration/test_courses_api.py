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

@pytest.fixture
def setup_data():
    """
    Create initial data for course and teacher to use in tests.
    """
    teacher = Teacher(name="John Doe")
    session.add(teacher)
    session.commit()

    course = Course(name="Mathematics", teacher_id=None)
    session.add(course)
    session.commit()

    return course, teacher

def test_assign_teacher_to_course(client, setup_data):
    """
    Test case for assigning a Teacher to a Course.
    Endpoint: PUT /courses/<course_id>
    Expected Outcome: 
      Status code 200, confirmation message and updated Course details.
    """
    course, teacher = setup_data
    response = client.put(f'/courses/{course.id}', json={"teacher_id": teacher.id})

    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Teacher assigned successfully to course."
    assert data['course']['teacher_id'] == teacher.id

def test_get_course_with_teacher(client, setup_data):
    """
    Test case for retrieving Course details including the associated Teacher.
    Endpoint: GET /courses/<course_id>
    Expected Outcome: 
      Status code 200, returns Course details and Teacher info as JSON.
    """
    course, teacher = setup_data
    course.teacher_id = teacher.id
    session.commit()

    response = client.get(f'/courses/{course.id}')
  
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == course.name
    assert data['teacher']['id'] == teacher.id
    assert data['teacher']['name'] == teacher.name

def test_assign_teacher_to_non_existent_course(client):
    """
    Attempt to assign a Teacher to a non-existent Course.
    Expected Outcome: 
      Status code 404, error message indicating the Course is not found.
    """
    response = client.put('/courses/99999', json={"teacher_id": 1})

    assert response.status_code == 404
    data = response.get_json()
    assert data['error']['code'] == "E001"
    assert data['error']['message'] == "Course not found."
```