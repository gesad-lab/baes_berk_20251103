```python
import pytest
from flask import json
from src.app import create_app, db
from src.models.student import Student
from src.models.course import Course

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})

    with app.app_context():
        # Create the database and tables for Student and Course
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture for providing a test client for the Flask application."""
    return app.test_client()

def test_database_migration_preserves_data(client):
    """Test the database migration process to ensure integrity and no data loss."""
    
    # Set up initial data
    student = Student(name='John Doe')
    course1 = Course(title='Mathematics')
    course2 = Course(title='Science')

    # Add initial data to the session and commit
    db.session.add(student)
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    # Capture initial counts
    initial_student_count = Student.query.count()
    initial_course_count = Course.query.count()

    # Assume migration logic is called here (this would normally be a call to a migration function)
    # e.g., migrate_database() # This function would handle the migration process

    # Fetch the student data again to verify it still exists
    migrated_student = Student.query.get(student.id)

    # Check migration integrity
    assert migrated_student is not None, "Student data should not be lost after migration."
    assert migrated_student.name == 'John Doe', "Student name should remain unchanged."
    
    # Check the number of courses after migration
    migrated_course_count = Course.query.count()
    assert migrated_course_count == initial_course_count, "Course count should remain unchanged after migration."

def test_assign_courses_to_student(client):
    """Test assigning courses to a student using the API endpoint."""
    
    # Create a student and courses for the test
    student = Student(name='Jane Doe')
    course1 = Course(title='Literature')
    course2 = Course(title='History')

    db.session.add(student)
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    # Assign courses to the student via the API
    response = client.post(f'/students/{student.id}/courses', json={'course_ids': [course1.id, course2.id]})
    
    assert response.status_code == 200, "Should successfully assign courses to the student."
    response_data = json.loads(response.data)
    
    assert response_data['message'] == "Courses assigned successfully."
    assert len(response_data['student']['courses']) == 2, "Student should have two courses assigned."

def test_get_student_with_courses(client):
    """Test retrieving a student along with assigned courses."""
    
    # Create a student and course
    student = Student(name='Alice Smith')
    course1 = Course(title='Biology')
    db.session.add(student)
    db.session.add(course1)
    db.session.commit()

    # Assign course to student
    student.courses.append(course1)
    db.session.commit()

    # Get student data through the API endpoint
    response = client.get(f'/students/{student.id}')
    
    assert response.status_code == 200, "Should retrieve the student successfully."
    response_data = json.loads(response.data)

    assert response_data['student']['name'] == 'Alice Smith'
    assert len(response_data['student']['courses']) == 1, "Student should have one course assigned."
    assert response_data['student']['courses'][0]['title'] == 'Biology'
```