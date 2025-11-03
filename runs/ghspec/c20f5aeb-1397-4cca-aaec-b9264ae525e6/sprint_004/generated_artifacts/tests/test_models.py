```python
import pytest
from src.models import Student, Course, StudentCourse  # Import StudentCourse for relationship testing
from src.database import get_db, init_db
from src.app import create_app

@pytest.fixture
def app():
    """Create a new Flask application instance for testing."""
    app = create_app({"TESTING": True})
    with app.app_context():
        init_db()  # Initialize the database with the schema
    yield app

@pytest.fixture
def client(app):
    """Create a test client for the application."""
    return app.test_client()

def test_student_course_relationship(client):
    """Test that a student can be assigned to courses through the StudentCourses relationship."""
    # Setup: Create a student and a couple of courses.
    student = Student(name="John Doe")
    course1 = Course(title="Math 101")
    course2 = Course(title="History 201")

    db.session.add(student)
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    # Enroll the student in both courses
    enrollment = StudentCourse(student_id=student.id, course_id=course1.id)
    db.session.add(enrollment)
    enrollment2 = StudentCourse(student_id=student.id, course_id=course2.id)
    db.session.add(enrollment2)
    db.session.commit()

    # Assert that the student is enrolled in the courses
    assert len(student.courses) == 2  # Check the student has 2 courses associated
    assert course1 in student.courses  # Verify student enrolled in Math 101
    assert course2 in student.courses  # Verify student enrolled in History 201

def test_student_invalid_enrollment(client):
    """Test that attempting to enroll a student with invalid student_id returns error."""
    response = client.post('/students/999/enroll', json={
        "course_ids": [1, 2, 3]  # Using invalid student
    })
    assert response.status_code == 404  # Ensure that a 404 Not Found is returned
    assert response.get_json()['error']['message'] == "Student not found"

def test_course_enrollment_validation(client):
    """Test that enrolling a student in courses that do not exist returns error."""
    response = client.post('/students/1/enroll', json={
        "course_ids": [999, 1000]  # Non-existent course IDs
    })
    assert response.status_code == 400  # Ensure a bad request is returned
    assert response.get_json()['error']['message'] == "Invalid course IDs"
```