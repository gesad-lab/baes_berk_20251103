```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py
from models import Course, Teacher  # Make sure to import your models

# Initialize the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to set up the database state before tests and clean up afterwards."""
    # Here we would typically set up the database for tests, e.g. creating tables
    # and inserting necessary seed data. This is just a placeholder.
    pass

@pytest.fixture(scope="module")
def create_teacher(setup_database):
    """Fixture to create a teacher in the database for testing."""
    response = client.post("/teachers/", json={"name": "John Doe"})
    assert response.status_code == 201  # Ensure teacher creation is successful
    return response.json()  # Return the created teacher's data for further tests

@pytest.fixture(scope="module")
def create_course(setup_database):
    """Fixture to create a course in the database for testing."""
    response = client.post("/courses/", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201  # Ensure course creation is successful
    return response.json()  # Return the created course's data for further tests

def test_assign_teacher_to_course(create_teacher, create_course):
    """Test assigning a teacher to a course successfully."""
    course_id = create_course['id']
    teacher_id = create_teacher['id']

    response = client.put(f"/courses/{course_id}/assign_teacher/", json={"teacher_id": teacher_id})
    assert response.status_code == 200
    assert response.json()['teacher_id'] == teacher_id  # Verify the correct teacher is assigned

def test_get_course_with_teacher(create_teacher, create_course):
    """Test retrieving a course with its assigned teacher."""
    course_id = create_course['id']
    teacher_id = create_teacher['id']
    
    # First, assign the teacher to the course
    client.put(f"/courses/{course_id}/assign_teacher/", json={"teacher_id": teacher_id})

    response = client.get(f"/courses/{course_id}/")
    assert response.status_code == 200
    
    course_data = response.json()
    assert course_data['teacher_id'] == teacher_id  # Ensure the returned course data includes the expected teacher ID
    assert 'teacher' in course_data  # Ensure that teacher information is included
    assert course_data['teacher']['name'] == create_teacher['name']  # Verify teacher name is correct

def test_fail_assign_teacher_invalid_course(create_teacher):
    """Test failing to assign a teacher to a non-existent course."""
    teacher_id = create_teacher['id']
    
    response = client.put("/courses/999/assign_teacher/", json={"teacher_id": teacher_id})  # 999 is assumed not to exist
    assert response.status_code == 404  # Expected not found error

def test_fail_assign_teacher_invalid_teacher(create_course):
    """Test failing to assign a non-existent teacher to a course."""
    course_id = create_course['id']
    
    response = client.put(f"/courses/{course_id}/assign_teacher/", json={"teacher_id": 999})  # 999 is assumed not to exist
    assert response.status_code == 404  # Expected not found error
```