```python
import pytest
import json
from your_app_name import create_app, db  # Adjust according to your application structure
from your_app_name.models import Teacher, Course  # Import Teacher and Course models

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
    with app.app_context():
        db.create_all()  # Create all tables, including Teacher and Course
        # Setup test data
        teacher = Teacher(id=1, name='John Doe')
        course = Course(id=1, name='Physics 101')
        db.session.add(teacher)
        db.session.add(course)
        db.session.commit()  # Commit to save test data
        yield app

def test_assign_teacher_to_course(client):
    """Test successful teacher-course assignment."""
    response = client.patch('/courses/1/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 200
    assert response.json['message'] == "Teacher assigned to course successfully."

def test_assign_teacher_to_non_existing_course(client):
    """Test assignment attempt to a non-existing course."""
    response = client.patch('/courses/999/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 404

def test_assign_non_existing_teacher_to_course(client):
    """Test assignment of a non-existing teacher to a course."""
    response = client.patch('/courses/1/assign-teacher', json={'teacher_id': 999})
    assert response.json['error']['code'] == 'E001'
```