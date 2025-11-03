```python
import pytest
from flask import json
from src.app import app  # Import the Flask app
from src.models import Course, Teacher  # Import models
from src.repositories import CourseRepository, TeacherRepository  # Import repositories

# Sample Data
@pytest.fixture
def sample_teacher():
    teacher = Teacher(name="John Doe")
    TeacherRepository.save(teacher)
    return teacher

@pytest.fixture
def sample_course():
    course = Course(title="Math 101")
    CourseRepository.save(course)
    return course

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_assign_teacher(client, sample_course, sample_teacher):
    """Test assigning a teacher to a course."""
    response = client.post(f'/courses/{sample_course.id}/assign-teacher',
                            data=json.dumps({'teacher_id': sample_teacher.id}),
                            content_type='application/json')
    
    # Assert that the response is successful
    assert response.status_code == 200
    assert response.json['message'] == "Teacher assigned successfully"

    # Retrieve the updated course and assert teacher is assigned
    course_response = client.get(f'/courses/{sample_course.id}')
    assert course_response.status_code == 200
    assert course_response.json['teacher_id'] == sample_teacher.id


def test_get_course_with_teacher(client, sample_course, sample_teacher):
    """Test retrieving course information including assigned teacher."""
    # First, assign a teacher to the course
    client.post(f'/courses/{sample_course.id}/assign-teacher',
                data=json.dumps({'teacher_id': sample_teacher.id}),
                content_type='application/json')

    # Now, retrieve the course info
    response = client.get(f'/courses/{sample_course.id}')
    
    # Assert that the response is successful and includes teacher information
    assert response.status_code == 200
    assert response.json['id'] == sample_course.id
    assert response.json['teacher_id'] == sample_teacher.id


def test_update_teacher(client, sample_course, sample_teacher):
    """Test updating the assigned teacher for a course."""
    new_teacher = Teacher(name="Jane Smith")
    TeacherRepository.save(new_teacher)

    # Assign the first teacher
    client.post(f'/courses/{sample_course.id}/assign-teacher',
                data=json.dumps({'teacher_id': sample_teacher.id}),
                content_type='application/json')

    # Update to the new teacher
    response = client.put(f'/courses/{sample_course.id}/update-teacher',
                          data=json.dumps({'teacher_id': new_teacher.id}),
                          content_type='application/json')

    # Assert successful update
    assert response.status_code == 200
    assert response.json['message'] == "Teacher updated successfully"

    # Fetch course info to verify the update
    updated_course_response = client.get(f'/courses/{sample_course.id}')
    assert updated_course_response.json['teacher_id'] == new_teacher.id
```