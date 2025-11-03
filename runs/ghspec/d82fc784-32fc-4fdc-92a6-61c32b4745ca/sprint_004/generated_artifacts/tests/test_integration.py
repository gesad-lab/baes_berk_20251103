```python
import pytest
from app import create_app, db
from app.models import Student, Course  # Ensure models are imported
import json

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database

def test_remove_student_from_course(client):
    """Test removing a student from a course."""
    # Arrange: Create test data
    student = Student(name="Test Student")
    course = Course(name="Test Course")
    db.session.add(student)
    db.session.add(course)
    db.session.commit()
    
    # Enroll the student in the course
    response = client.post(f'/students/{student.id}/courses', 
                            data=json.dumps({"course_id": course.id}),
                            content_type='application/json')
    assert response.status_code == 201  # Enrollment should succeed

    # Act: Remove the student from the course
    response = client.delete(f'/students/{student.id}/courses/{course.id}')
    
    # Assert: Verify the removal was successful
    assert response.status_code == 204  # No Content is expected on successful deletion

    # Verify that the relationship no longer exists
    enrolled_courses = client.get(f'/students/{student.id}/courses')
    assert enrolled_courses.json == []  # Student should not be enrolled in any courses
```