import pytest
from app import create_app, db
from app.models import Student, Course, StudentCourse  # Import the StudentCourse model

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after tests

def test_remove_student_from_course(client):
    """Test removing a student from a course."""
    # Create a student and a course for testing
    student = Student(name="Test Student")
    course = Course(name="Test Course")
    
    # Add entities to the session and commit
    db.session.add(student)
    db.session.add(course)
    db.session.commit()
    
    # Enroll the student in the course
    enrollment = StudentCourse(student_id=student.id, course_id=course.id)
    db.session.add(enrollment)
    db.session.commit()
    
    # Verify the student is enrolled in the course
    assert StudentCourse.query.filter_by(student_id=student.id, course_id=course.id).first() is not None
    
    # Now remove the student from the course
    response = client.delete(f'/students/{student.id}/courses/{course.id}')
    
    # Check that the response status is 204 No Content
    assert response.status_code == 204
    
    # Ensure the relationship no longer exists in the database
    assert StudentCourse.query.filter_by(student_id=student.id, course_id=course.id).first() is None