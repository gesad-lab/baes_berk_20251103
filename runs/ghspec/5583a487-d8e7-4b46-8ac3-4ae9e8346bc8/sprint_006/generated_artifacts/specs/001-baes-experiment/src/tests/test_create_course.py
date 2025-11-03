```python
import pytest
from flask import jsonify
from app import app, db, Course, Teacher  # Import the Course and Teacher models

# Setup the Flask application for testing with an in-memory SQLite database
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables for tests
            yield client  # Provide the test client to the test functions

# Test for Course creation with Teacher association
def test_create_course_with_teacher(client):
    # First create a Teacher record
    teacher_data = {"name": "John Doe", "email": "john.doe@example.com"}
    response = client.post('/teachers', json=teacher_data)
    assert response.status_code == 201  # Ensure Teacher was created

    # Get the created Teacher ID for course association
    teacher_id = response.get_json()['id']

    # Now create a Course with the associated Teacher
    course_data = {"title": "Introduction to Python", "description": "Learn Python basics.", "teacher_id": teacher_id}
    response = client.post('/courses', json=course_data)
    assert response.status_code == 201  # Ensure Course was created successfully
    assert response.get_json()['message'] == "Course created successfully."  # Check success message

# Test for Course retrieval including Teacher information
def test_get_course_with_teacher(client):
    # Create a Teacher record first
    teacher_data = {"name": "Jane Smith", "email": "jane.smith@example.com"}
    response = client.post('/teachers', json=teacher_data)
    teacher_id = response.get_json()['id']  # Get Teacher ID

    # Create a Course associated with the Teacher
    course_data = {"title": "Advanced Python", "description": "Deep dive into Python features.", "teacher_id": teacher_id}
    client.post('/courses', json=course_data)

    # Retrieve the Course by ID
    response = client.get('/courses/1')  # Assuming 1 is the course ID
    assert response.status_code == 200  # Ensure the request was successful
    course = response.get_json()
    assert course['title'] == "Advanced Python"
    assert course['teacher']['id'] == teacher_id  # Validate Teacher association

# Test for creating a Course without a Teacher association
def test_create_course_without_teacher(client):
    course_data = {"title": "Physics 101", "description": "Basic principles of physics."}
    
    response = client.post('/courses', json=course_data)
    assert response.status_code == 400  # Ensure Bad Request status
    assert response.get_json()['error']['message'] == "Teacher ID is required."  # Check error message

# Run the tests
if __name__ == '__main__':
    pytest.main()
```