```python
import pytest
from app import create_app, db
from app.models import Teacher, Course  # Ensure Course and Teacher models are imported
from http import HTTPStatus

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create schema for testing
            yield client
            db.drop_all()  # Clean up after testing

def test_assign_teacher_to_course(client):
    """Test successful assignment of a teacher to an existing course."""
    # Arrange
    teacher = Teacher(name="John Doe", email="john@example.com")
    course = Course(name="Math 101")
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Act
    response = client.post(f'/courses/{course.id}/assign-teacher/{teacher.id}')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json['message'] == 'Teacher assigned successfully.'

def test_view_course_with_teacher(client):
    """Test retrieving course details with teacher information."""
    # Arrange
    teacher = Teacher(name="John Doe", email="john@example.com")
    course = Course(name="Math 101", teacher_id=teacher.id)
    db.session.add(teacher)
    db.session.add(course)
    db.session.commit()

    # Act
    response = client.get(f'/courses/{course.id}')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json['teacher']['name'] == teacher.name
    assert response.json['teacher']['email'] == teacher.email

def test_assign_teacher_invalid_course(client):
    """Test attempting to assign a teacher to a non-existent course."""
    # Arrange
    teacher = Teacher(name="John Doe", email="john@example.com")
    db.session.add(teacher)
    db.session.commit()

    # Act
    response = client.post('/courses/999/assign-teacher/{teacher.id}')  # Assuming 999 does not exist

    # Assert
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json['error']['code'] == 'E001'
    assert response.json['error']['message'] == 'Course not found.'
```
