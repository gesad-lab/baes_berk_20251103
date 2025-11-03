```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.course import Course
from src.models.teacher import Teacher
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Create the database tables including Course and Teacher tables
    Base.metadata.create_all(bind=engine)
    
    # Add Teacher data for testing
    teacher_data = {'name': 'John Doe'}
    response = client.post("/teachers/", json=teacher_data)
    assert response.status_code == 201  # Check if the teacher was created successfully

    # Get the created Teacher ID
    teacher_id = response.json()['id']

    # Add a Course for testing
    course_data = {'name': 'Mathematics', 'teacher_id': teacher_id}
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 201  # Check if the course was created successfully

    yield  # This allows tests to run while setup is complete

    # Cleanup (optional, if needed) could go here

def test_assign_teacher_to_course():
    # Create data to assign Teacher to Course
    course_id = 1  # Assume this is the ID of the created course
    teacher_id = 1  # Assume this is the ID of the created teacher

    # Assign teacher to course
    response = client.put(f"/courses/{course_id}/assign-teacher", json={'teacher_id': teacher_id})
    
    assert response.status_code == 200  # Should return a 200 status
    assert response.json()['teacher_id'] == teacher_id  # Ensure the course has the correct teacher assigned

def test_validate_required_fields_for_course_update():
    # Attempt to assign a Teacher without a Course ID
    response = client.put("/courses/assign-teacher", json={'teacher_id': 1})
    
    assert response.status_code == 400  # Should return a 400 status
    assert response.json() == {"error": {"code": "E001", "message": "Course ID is required."}}  # Check error message

    # Attempt to assign a Teacher without a Teacher ID
    response = client.put("/courses/1/assign-teacher", json={})
    
    assert response.status_code == 400  # Should return a 400 status
    assert response.json() == {"error": {"code": "E002", "message": "Teacher ID is required."}}  # Check error message

def test_retrieve_course_with_teacher_assignment():
    course_id = 1  # Assume this is the ID of the created course

    # Retrieve the course information
    response = client.get(f"/courses/{course_id}")
    
    assert response.status_code == 200  # Should return a 200 status
    course_data = response.json()
    assert course_data['id'] == course_id  # Ensure the correct course is returned
    assert 'teacher_id' in course_data  # Ensure the teacher ID is part of the response
```