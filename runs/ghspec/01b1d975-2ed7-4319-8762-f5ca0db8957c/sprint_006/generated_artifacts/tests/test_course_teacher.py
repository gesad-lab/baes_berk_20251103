```python
import pytest
from flask import json
from src.app import create_app
from src.models import db, Course, Teacher

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app({'TESTING': True})  # Configure the app for testing
    with app.app_context():
        db.create_all()  # Create the database tables
        yield app
        db.drop_all()  # Clean up after tests

@pytest.fixture
def sample_teacher(app):
    """Create a sample Teacher for testing."""
    teacher = Teacher(name="John Doe", email="johndoe@example.com")
    db.session.add(teacher)
    db.session.commit()
    return teacher

@pytest.fixture
def sample_course(app):
    """Create a sample Course for testing."""
    course = Course(title="Test Course")
    db.session.add(course)
    db.session.commit()
    return course

def test_retrieve_course_details(app, sample_course, sample_teacher):
    """Test retrieving course details with associated teacher information."""
    # Assign the teacher to the course
    sample_course.teacher_id = sample_teacher.id
    db.session.commit()

    # Retrieve the course details
    response = app.test_client().get(f'/courses/{sample_course.id}')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['title'] == sample_course.title
    assert data['teacher']['name'] == sample_teacher.name
    assert data['teacher']['email'] == sample_teacher.email

def test_update_teacher_assignment(app, sample_course, sample_teacher):
    """Test updating the teacher assigned to a course."""
    second_teacher = Teacher(name="Jane Doe", email="janedoe@example.com")
    db.session.add(second_teacher)
    db.session.commit()

    # Assign the first teacher to the course
    sample_course.teacher_id = sample_teacher.id
    db.session.commit()

    # Now update to the second teacher
    response = app.test_client().put(
        f'/courses/{sample_course.id}/assign_teacher',
        json={'teacher_id': second_teacher.id}
    )

    assert response.status_code == 200
    # Verify the course now has the new teacher assigned
    updated_course = Course.query.get(sample_course.id)
    assert updated_course.teacher_id == second_teacher.id

def test_assign_non_existent_teacher(app, sample_course):
    """Test error handling when assigning a non-existent teacher to a course."""
    response = app.test_client().post(
        f'/courses/{sample_course.id}/assign_teacher',
        json={'teacher_id': 999}  # Assuming this ID does not exist
    )

    assert response.status_code == 404
    assert b'Teacher not found' in response.data

def test_integrity_after_relationship_creation(app, sample_course, sample_teacher):
    """Test data integrity after assigning a teacher to a course."""
    # Assign the teacher to the course
    sample_course.teacher_id = sample_teacher.id
    db.session.commit()

    # Immediately retrieve course data
    response = app.test_client().get(f'/courses/{sample_course.id}')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['teacher']['name'] == sample_teacher.name
```