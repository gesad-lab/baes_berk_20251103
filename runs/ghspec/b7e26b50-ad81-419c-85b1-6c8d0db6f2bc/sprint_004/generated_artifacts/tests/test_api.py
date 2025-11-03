```python
import json
import pytest
from flask import Flask, request, jsonify, abort
from your_app import create_app, db  # Adjust import based on your app structure
from your_app.models import Student, Course  # Adjust import for your Course model

app = create_app()

# Centralized error handling for missing course data
@app.errorhandler(400)
def handle_bad_request(error):
    response = {
        "error": {
            "code": "E400",
            "message": "Bad request",
            "details": {}
        }
    }
    return jsonify(response), 400

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_database():
    # Setup code to initialize the database with sample data
    db.create_all()

    # Create example students and courses
    student = Student(id=1, name="John Doe")
    course1 = Course(id=1, name="Course A", level="Beginner")
    course2 = Course(id=2, name="Course B", level="Intermediate")
    
    db.session.add(student)
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    yield  # This allows tests to run

    # Teardown code to drop all tables after tests
    db.session.remove()
    db.drop_all()

def test_fetch_student_courses(client, init_database):
    """Test fetching courses associated with the student."""
    response = client.get('/students/1/courses')
    assert response.status_code == 200
    data = response.get_json()
    
    # Check that the response contains correct course information
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]
    assert "level" in data[0]

def test_associate_courses_with_student(client, init_database):
    """Test associating courses with a student."""
    response = client.patch('/students/1/courses', json={"course_ids": [1, 2]})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Courses successfully associated with student."

def test_invalid_course_association(client, init_database):
    """Test associating non-existing course returns 404."""
    response = client.patch('/students/1/courses', json={"course_ids": [999]})
    assert response.status_code == 404
    data = response.get_json()
    assert data["error"]["message"] == "Course not found."
```