```python
import pytest
from app import create_app, db
from app.models import Student, Course  # Assuming Course model has been defined

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the data...

def test_enroll_student_in_course(client):
    """Test enrolling a student in a course."""
    # Setup: Create a test student and course
    student = Student(id=1, name="Test Student")
    course = Course(id=1, name="Test Course", level="Beginner")
    db.session.add(student)
    db.session.add(course)
    db.session.commit()
    
    # Test: Enroll student in the course
    response = client.post('/students/1/courses', json={"course_id": "1"})
    
    # Verify: Check the response and status code
    assert response.status_code == 201  # Expect HTTP 201 Created
    assert response.json == {
        "student_id": "1",
        "course_id": "1"
    }

def test_retrieve_student_courses(client):
    """Test retrieving courses a student is enrolled in."""
    # Setup: Create a test student and assign it to a course
    student = Student(id=1, name="Test Student")
    course = Course(id=1, name="Test Course", level="Beginner")
    db.session.add(student)
    db.session.add(course)
    db.session.commit()
    
    # Enroll student
    client.post('/students/1/courses', json={"course_id": "1"})
    
    # Test: Retrieve student courses
    response = client.get('/students/1/courses')

    # Verify: Check the response and status code
    assert response.status_code == 200  # Expect HTTP 200 OK
    assert response.json == [{
        "course_id": "1",
        "name": "Test Course",
        "level": "Beginner"
    }]

def test_remove_student_from_course(client):
    """Test removing a student from a course."""
    # Setup: Create a test student and course
    student = Student(id=1, name="Test Student")
    course = Course(id=1, name="Test Course", level="Beginner")
    db.session.add(student)
    db.session.add(course)
    db.session.commit()
    
    # Enroll student
    client.post('/students/1/courses', json={"course_id": "1"})
    
    # Test: Remove student from the course
    response = client.delete('/students/1/courses/1')

    # Verify: Check the response and status code
    assert response.status_code == 204  # Expect HTTP 204 No Content
```