```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.services.course_service import CourseService
from src.models.course import Course
from src.models.teacher import Teacher

# Initialize the FastAPI test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the in-memory database for testing."""
    # Setup logic to create required tables and seed initial data as necessary
    # This should include creating mock Course and Teacher entries.
    
    # Create a mock course and teacher for testing
    teacher = Teacher(id=1, name="John Doe")
    course = Course(id=1, title="Math 101", teacher_id=None)
    
    yield 
    # Cleanup logic if necessary

def test_assign_teacher_success(setup_database):
    """Test enabling a teacher to be assigned to a course successfully."""
    response = client.put("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully"}
    
    # Verify that the course now has the correct teacher assigned
    course = Course.get(1)
    assert course.teacher_id == 1

def test_assign_teacher_non_existent_course(setup_database):
    """Test assigning a teacher to a non-existent course."""
    response = client.put("/courses/999/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}

def test_assign_teacher_non_existent_teacher(setup_database):
    """Test assigning a non-existent teacher to a course."""
    response = client.put("/courses/1/assign-teacher", json={"teacher_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Teacher not found"}}

def test_unassign_teacher_success(setup_database):
    """Test that a teacher can be unassigned from a course successfully."""
    response = client.delete("/courses/1/unassign-teacher")
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher unassigned successfully"}
    
    # Verify that the teacher_id is now None
    course = Course.get(1)
    assert course.teacher_id is None

def test_unassign_teacher_non_existent_course(setup_database):
    """Test unassigning a teacher from a non-existent course."""
    response = client.delete("/courses/999/unassign-teacher")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}
```