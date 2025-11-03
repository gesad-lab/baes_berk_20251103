```python
import json
import pytest
from api import create_app, db
from api.models import Course, Student  # Assuming the Student model is defined in models.py

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()  # Create the test client
        db.drop_all()  # Drop all tables after tests

def test_get_student_with_courses(test_client):
    """
    Test retrieving a student along with associated courses using the GET /students/{id} endpoint.
    The response should contain the student data and a list of associated courses.
    """
    # Create a test student and associated courses
    new_student = Student(name="Test Student")
    new_course_1 = Course(name="Math 101")
    new_course_2 = Course(name="History 201")
    
    with test_client.application.app_context():
        db.session.add(new_student)
        db.session.add(new_course_1)
        db.session.add(new_course_2)
        db.session.commit()
        
        # Assuming a function to associate courses with a student exists
        new_student.courses.append(new_course_1)
        new_student.courses.append(new_course_2)
        db.session.commit()

    # Retrieve the student with associated courses
    response = test_client.get(f'/students/{new_student.id}')
    
    # Validate the response
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == new_student.id
    assert data['name'] == new_student.name
    assert len(data['courses']) == 2  # Expecting 2 associated courses
    assert all(course['name'] in ["Math 101", "History 201"] for course in data['courses'])

def test_get_student_with_invalid_id(test_client):
    """
    Test retrieving a student with an invalid ID using the GET /students/{id} endpoint.
    The response should return a 404 status code.
    """
    response = test_client.get('/students/9999')  # Using a non-existent ID
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error']['code'] == 'E404'  # Assuming we have defined this error code for not found
    assert "Student not found" in data['error']['message']

```