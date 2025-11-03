```python
import pytest
from flask import json
from src.database import get_db, init_db
from src.models import Teacher, Course

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

@pytest.fixture(scope='module')
def test_client(db):
    """Create a test client for making API requests."""
    from src.app import create_app
    app = create_app()
    with app.test_client() as client:
        yield client

def test_create_course_with_valid_teacher(db, test_client):
    """Test creating a new course with a valid teacher ID."""
    # First, create a teacher for the test
    teacher_response = test_client.post('/teachers', json={"name": "John Doe"})
    teacher_data = json.loads(teacher_response.data)
    assert teacher_response.status_code == 201
    teacher_id = teacher_data['id']  # Assuming the response returns the new teacher ID

    # Now create a course with the valid teacher ID
    course_response = test_client.post('/courses', json={"course_name": "Mathematics", "teacher_id": teacher_id})
    assert course_response.status_code == 201
    response_data = json.loads(course_response.data)
    assert response_data["message"] == "Course created successfully."

def test_create_course_with_non_existent_teacher(db, test_client):
    """Test response when trying to create a course with a non-existent teacher ID."""
    # Attempt to create a course with a non-existent teacher ID
    course_response = test_client.post('/courses', json={"course_name": "History", "teacher_id": 9999})  # Assuming 9999 does not exist
    assert course_response.status_code == 400
    response_data = json.loads(course_response.data)
    assert response_data["error"]["code"] == "E003"
    assert response_data["error"]["message"] == "Teacher does not exist."

def test_assign_teacher_to_existing_course(db, test_client):
    """Test assigning a teacher to an existing course."""
    # Create a teacher for the test
    teacher_response = test_client.post('/teachers', json={"name": "Alice Smith"})
    teacher_data = json.loads(teacher_response.data)
    assert teacher_response.status_code == 201
    teacher_id = teacher_data['id']

    # Create a course to update later
    course_response = test_client.post('/courses', json={"course_name": "Physics"})
    assert course_response.status_code == 201

    # Get the ID of the created course
    course_data = json.loads(course_response.data)

    # Assign the teacher to the created course
    update_response = test_client.put(f'/courses/{course_data["id"]}', json={"teacher_id": teacher_id})
    assert update_response.status_code == 200
    update_response_data = json.loads(update_response.data)
    assert update_response_data["message"] == "Course updated successfully."
```