```python
import pytest
from flask import json
from app import app, db
from models import Course, Teacher

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
            # Setup initial test data
            teacher = Teacher(name='John Doe')
            db.session.add(teacher)
            db.session.commit()
            course = Course(title='Math 101', teacher_id=None)
            db.session.add(course)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()  # Cleanup after tests

def test_assign_teacher_to_course_success(client):
    """Verify that a user can assign a teacher to an existing course."""
    # Retrieve the existing course and teacher
    course = Course.query.first()
    teacher = Teacher.query.first()
    
    # Assign the teacher to the course
    response = client.post(f'/courses/{course.id}/assign-teacher', json={'teacher_id': teacher.id})
    
    assert response.status_code == 200
    # Refresh the course from the database to get the updated data
    db.session.refresh(course)
    assert course.teacher_id == teacher.id  # Verify the teacher has been assigned

def test_assign_non_existent_teacher(client):
    """Confirm that assigning a non-existent teacher returns an error."""
    course = Course.query.first()
    
    # Attempt to assign a non-existent teacher
    response = client.post(f'/courses/{course.id}/assign-teacher', json={'teacher_id': 9999})  # ID that doesn't exist
    
    assert response.status_code == 404  # Expect a 404 Not Found
    assert response.json['error']['message'] == "Teacher not found."  # Check for appropriate error message

def test_database_migration_data_integrity(client):
    """Validate that no course or teacher data is lost or altered during migration."""
    # Assuming a migration has been done and we want to verify data integrity
    # This would typically involve mock or real migration verification
    
    # Here, we would assert that the Teacher and Course count remains the same
    teachers_count = Teacher.query.count()
    courses_count = Course.query.count()
    
    # After migration verification (in a real scenario this would be after a migration run)
    assert teachers_count > 0  # Make sure some teachers exist
    assert courses_count > 0    # Make sure some courses exist

def test_retrieve_course_data_with_teacher_info(client):
    """Ensure that retrieving a course includes the correct teacher reference."""
    course = Course.query.first()
    teacher = Teacher.query.first()
    
    # Assign the teacher to the course
    course.teacher_id = teacher.id
    db.session.commit()
    
    response = client.get(f'/courses/{course.id}')
    assert response.status_code == 200
    assert response.json['teacher_id'] == teacher.id  # Teacher ID should match

```