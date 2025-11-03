```python
# New file to specifically test course teacher assignment functionalities
import pytest
from fastapi.testclient import TestClient
from src.main import app  # FastAPI app reference
from src.db import init_db, shutdown_db  # Database management functions
from src.models import Teacher, Course  # Assuming you have Course and Teacher models

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Set up the database for testing."""
    init_db()
    
    # Create mock data for tests
    # Create a valid teacher and course in the database for testing
    valid_teacher = Teacher(name="John Doe", email="john.doe@example.com")
    valid_course = Course(title="Mathematics 101")
    
    # Add these instances to the database
    # Assuming you have methods to add items to the database
    # It is important to validate that the ids for the models get created.
    # Implement methods accordingly in the actual DB management functions
    teacher_id = valid_teacher.create()  # Replace with actual database insertion logic
    course_id = valid_course.create()     # Replace with actual database insertion logic
    
    yield (teacher_id, course_id)  # Yield the created IDs for test cases.

    shutdown_db()

def test_assign_teacher_to_course(setup_database):
    """Test assigning a teacher to a valid course."""
    teacher_id, course_id = setup_database
    response = client.put(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})
    
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher assigned successfully"
    assert response.json()["course"]["teacher_id"] == teacher_id

def test_retrieve_course_details(setup_database):
    """Test retrieving details of the course with an assigned teacher."""
    teacher_id, course_id = setup_database
    # First, assign the teacher to the course
    client.put(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})
    
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert "teacher" in response.json()
    assert response.json()["teacher"]["name"] == "John Doe"
    assert response.json()["teacher"]["email"] == "john.doe@example.com"

def test_assign_teacher_to_non_existent_course():
    """Test assigning a teacher to a non-existent course."""
    response = client.put("/courses/999/assign-teacher", json={"teacher_id": "1"})
    
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E001"
    assert response.json()["error"]["message"] == "Course does not exist."

def test_reassign_teacher():
    """Test reassigning a teacher to an existing course."""
    teacher_id, course_id = setup_database
    # Assign the first teacher
    client.put(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})
    
    # Create a new teacher for reassignment
    new_teacher = Teacher(name="Jane Smith", email="jane.smith@example.com")
    new_teacher_id = new_teacher.create()  # Ensure this is handled accordingly
    
    response = client.put(f"/courses/{course_id}/assign-teacher", json={"teacher_id": new_teacher_id})
    
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher assigned successfully"
    assert response.json()["course"]["teacher_id"] == new_teacher_id
```