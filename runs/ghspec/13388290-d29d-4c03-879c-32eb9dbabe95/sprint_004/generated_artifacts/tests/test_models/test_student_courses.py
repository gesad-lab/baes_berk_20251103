```python
import pytest
from app import create_app, db
from app.models import Student, Course, StudentCourses  # Ensure Student and Course models are imported

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create schema for testing
            # Create sample students and courses for testing
            student1 = Student(name="John Doe")
            student2 = Student(name="Jane Smith")
            course1 = Course(name="Mathematics", level="Beginner")
            course2 = Course(name="Science", level="Intermediate")
            db.session.add(student1)
            db.session.add(student2)
            db.session.add(course1)
            db.session.add(course2)
            db.session.commit()
            yield client  # Provide the test client for testing

            # Cleanup after tests
            db.session.remove()
            db.drop_all()

def test_assign_course(client):
    """Test assigning courses to a student."""
    response = client.post('/students/1/courses', json={"course_ids": [1]})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Courses successfully assigned."}

    # Verify the course assignment
    association = StudentCourses.query.filter_by(student_id=1, course_id=1).first()
    assert association is not None

def test_get_student_courses(client):
    """Test retrieving courses for a student."""
    client.post('/students/1/courses', json={"course_ids": [1, 2]})  # Assign two courses to student 1
    response = client.get('/students/1/courses')
    assert response.status_code == 200
    data = response.get_json()
    
    assert len(data) == 2  # Verify two courses were returned
    assert data[0]['course_id'] in [1, 2]
    assert data[1]['course_id'] in [1, 2]

def test_remove_course(client):
    """Test removing a course from a student's enrollment."""
    client.post('/students/1/courses', json={"course_ids": [1]})  # Assign course 1 to student 1
    response = client.delete('/students/1/courses/1')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Course successfully removed."}

    # Verify the course is no longer assigned
    association = StudentCourses.query.filter_by(student_id=1, course_id=1).first()
    assert association is None
```