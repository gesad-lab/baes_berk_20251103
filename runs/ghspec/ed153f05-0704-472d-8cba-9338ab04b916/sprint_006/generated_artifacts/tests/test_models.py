```python
import pytest
from flask import json
from src.database import get_db, init_db
from src.models import Teacher, Course
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope='module')
def db():
    """Set up a fresh database for testing."""
    init_db()  # Initialize the database
    yield get_db()  # Provide the database to the test

def test_assign_non_existent_teacher_to_course(db):
    """Test response when assigning a non-existent teacher to a course."""
    # First, create a valid course
    valid_course_data = {"course_name": "Mathematics"}
    create_response = db.post('/courses', json=valid_course_data)
    assert create_response.status_code == 201  # Course creation should succeed

    course_id = create_response.json['id']  # Retrieve the created course ID

    # Now, attempt to assign a non-existent teacher ID (e.g., teacher_id = 999).
    update_data = {"teacher_id": 999}
    update_response = db.put(f'/courses/{course_id}', json=update_data)
    
    # Check that we receive the correct error response for non-existent teacher.
    assert update_response.status_code == 404  # Expect 404 Not Found
    assert update_response.json['error']['code'] == 'E003'  # Error code for missing teacher
    assert update_response.json['error']['message'] == 'Teacher does not exist.'  # Proper error message
```