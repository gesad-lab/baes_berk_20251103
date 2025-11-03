```python
import pytest
from app import app, db, Student, Course

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing
            # Creating sample courses for tests
            course1 = Course(name="Introduction to Python", level="Beginner")
            course2 = Course(name="Advanced JavaScript", level="Advanced")
            db.session.add(course1)
            db.session.add(course2)
            db.session.commit()
            
            # Adding a sample student for testing
            student = Student(name="John Doe")
            db.session.add(student)
            db.session.commit()
            
            yield client  # Provide the test client for tests
            
            db.drop_all()  # Clean up after tests

def test_assign_course_to_student_with_valid_course(client):
    # Assigning a valid course to a student
    response = client.post('/students/1/courses', json={"course_id": 1})
    assert response.status_code == 201
    assert response.json['student_id'] == 1
    assert len(response.json['courses']) == 1
    assert response.json['courses'][0]['id'] == 1
    assert response.json['courses'][0]['name'] == "Introduction to Python"

def test_assign_course_to_student_with_invalid_course(client):
    # Attempting to assign an invalid course ID
    response = client.post('/students/1/courses', json={"course_id": 999})
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E002", "message": "Invalid course ID."}}

def test_assign_course_to_nonexistent_student(client):
    # Attempting to assign a course to a non-existent student
    response = client.post('/students/999/courses', json={"course_id": 1})
    assert response.status_code == 404
    assert response.json == {"error": "Student not found"}

def test_get_courses_for_student(client):
    # Verify that a student has no courses initially
    response = client.get('/students/1/courses')
    assert response.status_code == 200
    assert response.json == []

    # Assigning a course first
    client.post('/students/1/courses', json={"course_id": 1})

    # Now retrieve courses for the student
    response = client.get('/students/1/courses')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == 1
    assert response.json[0]['name'] == "Introduction to Python"
```