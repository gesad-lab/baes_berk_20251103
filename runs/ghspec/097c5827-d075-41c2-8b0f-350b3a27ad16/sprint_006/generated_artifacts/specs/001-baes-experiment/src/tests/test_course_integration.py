```python
import pytest
from flask import json
from src.app import app
from src.models import Course, Teacher

@pytest.fixture
def client():
    """Create a test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def setup_courses_and_teachers():
    """Set up some test courses and teachers in the database."""
    with app.app_context():
        # Assuming there is a function to create sample courses and teachers
        teacher = Teacher(name='Jane Smith', email='jane.smith@example.com')
        course = Course(course_name='Mathematics', level='Beginner')
        # Add to database (method to save and commit would be needed)
        # db.session.add(teacher)
        # db.session.add(course)
        # db.session.commit()
        return teacher, course

def test_assign_teacher_to_course_success(client, setup_courses_and_teachers):
    """Test assigning an existing teacher to a course."""
    teacher, course = setup_courses_and_teachers
    response = client.patch(f'/courses/{course.id}/assign-teacher', 
                             data=json.dumps({'teacherId': teacher.id}),
                             content_type='application/json')
    
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Teacher assigned successfully', 'courseId': course.id, 'teacherId': teacher.id}

def test_assign_non_existent_teacher_fails(client, setup_courses_and_teachers):
    """Test error message when assigning a non-existent teacher."""
    course = setup_courses_and_teachers[1]
    response = client.patch(f'/courses/{course.id}/assign-teacher', 
                             data=json.dumps({'teacherId': 999}), 
                             content_type='application/json')
    
    assert response.status_code == 400
    assert response.get_json() == {'error': {'code': 'E001', 'message': 'Teacher does not exist'}}

def test_retrieve_course_details_with_teacher(client, setup_courses_and_teachers):
    """Test retrieving course details with assigned teacher information."""
    teacher, course = setup_courses_and_teachers
    # Assign teacher to course
    client.patch(f'/courses/{course.id}/assign-teacher', 
                 data=json.dumps({'teacherId': teacher.id}),
                 content_type='application/json')

    response = client.get(f'/courses/{course.id}')
    
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['courseId'] == course.id
    assert json_data['teacher']['name'] == teacher.name
    assert json_data['teacher']['email'] == teacher.email

def test_retrieve_course_details_without_teacher(client, setup_courses_and_teachers):
    """Test retrieving course details when no teacher is assigned."""
    course = setup_courses_and_teachers[1]
    
    response = client.get(f'/courses/{course.id}')
    
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['courseId'] == course.id
    assert 'teacher' not in json_data  # No teacher should be assigned

```