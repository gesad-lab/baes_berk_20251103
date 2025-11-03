```python
import pytest
from app import app, db, Course, Teacher

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema for testing

            # Creating sample teacher for tests
            teacher1 = Teacher(name="John Doe", email="johndoe@example.com")
            db.session.add(teacher1)
            
            # Creating a sample course for tests
            course1 = Course(name="Mathematics", level="Beginner")
            db.session.add(course1)

            db.session.commit()  # Commit the sample data
        yield client  # Provide the test client

@pytest.fixture
def create_invalid_teacher_id(client):
    # No invalid teacher ID is created. This is to test non-existent teacher assignment
    return 9999  # Non-existent teacher ID

def test_assign_non_existent_teacher(client, create_invalid_teacher_id):
    # Attempt to assign a non-existent teacher to the existing course
    response = client.patch('/courses/1/assign-teacher', json={"teacher_id": create_invalid_teacher_id})

    # Verify the response status code and error message
    assert response.status_code == 400
    assert response.get_json() == {"error": {"code": "E001", "message": "Teacher does not exist."}}

def test_successful_teacher_assignment(client):
    # Assign the existing teacher to the existing course
    response = client.patch('/courses/1/assign-teacher', json={"teacher_id": 1})

    # Verify the response status code and assigned teacher ID
    assert response.status_code == 200
    assert response.get_json()["teacher_id"] == 1

def test_retrieve_course_with_teacher(client):
    # First, assign a teacher to the course
    client.patch('/courses/1/assign-teacher', json={"teacher_id": 1})

    # Now retrieve the course details
    response = client.get('/courses/1')

    # Verify the course details and the assigned teacher information
    assert response.status_code == 200
    assert response.get_json()["teacher"]["id"] == 1
    assert response.get_json()["teacher"]["name"] == "John Doe"
```