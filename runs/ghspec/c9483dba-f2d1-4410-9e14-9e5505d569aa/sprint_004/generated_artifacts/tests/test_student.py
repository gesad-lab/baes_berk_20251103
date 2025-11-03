```python
# tests/test_student.py
import pytest
from app import app  # Assuming 'app' is the Flask app instance
from models import Student, Course, db  # Assuming both models are defined in 'models.py'

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_assign_course_success(client):
    """Test assigning a course to a student with valid IDs."""
    # Set up necessary data
    course = Course(name='Mathematics', level='Beginner')
    student = Student(name='John Doe', email='john.doe@example.com')
    db.session.add(course)
    db.session.add(student)
    db.session.commit()

    # Assign course to student
    response = client.post(f'/students/{student.id}/courses', json={'course_id': course.id})
    assert response.status_code == 200
    assert response.json == {'id': student.id, 'courses': [course.id]}

def test_assign_course_invalid_student(client):
    """Test assigning a course to a non-existent student."""
    response = client.post('/students/999/courses', json={'course_id': '1'})
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E002'  # Assuming E002 indicates an invalid student ID

def test_assign_course_missing_course_id(client):
    """Test assigning a course to a student with missing course ID."""
    student = Student(name='Jane Doe', email='jane.doe@example.com')
    db.session.add(student)
    db.session.commit()

    response = client.post(f'/students/{student.id}/courses', json={})  # No course_id provided
    assert response.status_code == 400  # Bad Request due to missing data
    assert response.json['error']['code'] == 'E003'  # Assuming E003 is for missing course ID

def test_get_student_courses(client):
    """Test retrieving a student with their assigned courses."""
    course = Course(name='Mathematics', level='Beginner')
    student = Student(name='John Doe', email='john.doe@example.com', courses=[course])
    db.session.add(course)
    db.session.add(student)
    db.session.commit()

    response = client.get(f'/students/{student.id}')
    assert response.status_code == 200
    assert response.json['id'] == student.id
    assert response.json['courses'] == [course.id]
```