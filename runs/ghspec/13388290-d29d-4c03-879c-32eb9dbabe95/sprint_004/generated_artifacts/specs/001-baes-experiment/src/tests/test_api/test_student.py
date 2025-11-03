```python
import pytest
from app import create_app, db
from app.models import StudentCourses, Course, Student
from http import HTTPStatus

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create schema for testing
            # Set up sample data
            student = Student(name="Sample Student")
            course = Course(name="Sample Course", level="Beginner")
            db.session.add(student)
            db.session.add(course)
            db.session.commit()
            # Create a StudentCourses entry
            student_course = StudentCourses(student_id=student.id, course_id=course.id)
            db.session.add(student_course)
            db.session.commit()
        yield client  # Provide access to the test client

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup the database after each test
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_delete_student_course(client):
    """Test that deleting a student's course successfully removes the association from the database."""
    # Assume we already have a student and a course set up in the fixtures
    student = Student.query.first()
    course = Course.query.first()
    student_course = StudentCourses.query.first()
    
    assert student_course is not None  # Ensure there's an association to delete

    response = client.delete(f'/students/{student.id}/courses/{course.id}')
    assert response.status_code == HTTPStatus.NO_CONTENT  # Expect a 204 No Content response
    
    # Confirm that the association has been deleted
    assert StudentCourses.query.count() == 0  # There should be no entries left in StudentCourses

def test_delete_non_existent_student_course(client):
    """Test that attempting to delete a non-existent student course returns a 404 error."""
    student_id = 999  # Non-existent student ID
    course_id = 999   # Non-existent course ID

    response = client.delete(f'/students/{student_id}/courses/{course_id}')
    assert response.status_code == HTTPStatus.NOT_FOUND  # Expect a 404 Not Found response
    assert response.get_json() == {"error": {"code": "E404", "message": "Student Course not found."}}
```