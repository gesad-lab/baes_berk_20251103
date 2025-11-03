```
# tests/test_routes.py

import pytest
from flask import json
from src.database import get_db, init_db
from src.models import Course, Teacher
from sqlalchemy.exc import IntegrityError

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

def test_update_course_with_valid_teacher(test_client, db):
    """Test updating a course to assign a valid teacher."""
    # Create a teacher to assign to the course
    teacher_data = {"name": "Mr. Smith"}
    teacher_response = test_client.post('/teachers', json=teacher_data)
    assert teacher_response.status_code == 201
    
    # Retrieve the created teacher's ID
    teacher_id = teacher_response.get_json().get('id')
    
    # Create a course to update
    course_data = {"course_name": "Mathematics"}
    course_response = test_client.post('/courses', json=course_data)
    assert course_response.status_code == 201
    
    course_id = course_response.get_json().get('id')
    
    # Update the course to assign the teacher
    update_response = test_client.put(f'/courses/{course_id}', json={"teacher_id": teacher_id})
    assert update_response.status_code == 200
    assert update_response.get_json() == {"message": "Course updated successfully."}

def test_update_course_with_invalid_teacher(test_client, db):
    """Test updating a course to assign a non-existent teacher."""
    # Create a course to update
    course_data = {"course_name": "Science"}
    course_response = test_client.post('/courses', json=course_data)
    assert course_response.status_code == 201
    
    course_id = course_response.get_json().get('id')
    
    # Attempt to update the course with a non-existent teacher ID
    update_response = test_client.put(f'/courses/{course_id}', json={"teacher_id": 9999})
    assert update_response.status_code == 400
    assert update_response.get_json() == {"error": {"code": "E003", "message": "Teacher does not exist."}}
```