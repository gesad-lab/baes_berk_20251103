```python
import pytest
from app import create_app, db
from models.teacher import Teacher
from models.student import Student  # Assuming Student is an existing model
from models.course import Course      # Assuming Course is an existing model

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')  # Use appropriate config for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
            yield client
            db.drop_all()    # Clean up after tests

def test_create_teacher(test_client):
    response = test_client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json
    assert response.json["name"] == "John Doe"
    assert response.json["email"] == "john.doe@example.com"

def test_create_teacher_without_name(test_client):
    response = test_client.post('/teachers', json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"

def test_create_teacher_without_email(test_client):
    response = test_client.post('/teachers', json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"

def test_existing_students_integrity(test_client):
    # Assuming you have a way to add initial data for students and courses
    new_student = Student(name="Alice", email="alice@example.com")
    new_course = Course(name="Math 101")

    db.session.add(new_student)
    db.session.add(new_course)
    db.session.commit()

    # Now perform the teacher creation, this will also check integration with existing entities
    response = test_client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    
    # Check that the existing students are still retrievable
    student = Student.query.get(new_student.id)
    assert student is not None
    assert student.name == "Alice"
    
    # Check that the existing courses are still retrievable
    course = Course.query.get(new_course.id)
    assert course is not None
    assert course.name == "Math 101"
```