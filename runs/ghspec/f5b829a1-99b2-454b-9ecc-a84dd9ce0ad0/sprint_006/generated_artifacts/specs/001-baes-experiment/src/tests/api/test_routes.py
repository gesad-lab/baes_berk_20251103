```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.services.course_service import CourseService

# Initialize the FastAPI test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to setup the in-memory database for testing."""
    # Setup logic to create required tables and seed initial data as necessary
    yield
    # Cleanup logic if necessary (e.g., drop tables, if applicable)

def test_unassign_teacher_from_course_success(setup_database):
    """Test unassigning a teacher from an existing course successfully."""
    course_id = 1  # Assuming a course with ID 1 exists
    response = client.delete(f"/courses/{course_id}/unassign-teacher")
    
    assert response.status_code == 200  # Expecting success status code
    data = response.json()
    assert data['message'] == "Teacher unassigned successfully."  # Expecting confirmation message
    
    # Verify that the course no longer has the teacher assigned
    course_response = client.get(f"/courses/{course_id}")
    course_data = course_response.json()
    assert course_data['teacher_id'] is None  # Teacher ID should be none after unassignment

def test_unassign_teacher_from_nonexistent_course(setup_database):
    """Test attempting to unassign a teacher from a non-existent course."""
    course_id = 999  # Assuming a course with ID 999 does not exist
    response = client.delete(f"/courses/{course_id}/unassign-teacher")
    
    assert response.status_code == 404  # Expecting not found status code
    assert response.json() == {"error": {"code": "E404", "message": "Course not found."}}  # Error message

def test_unassign_teacher_with_no_teacher_assigned(setup_database):
    """Test unassigning a teacher when no teacher is assigned."""
    course_id = 2  # Assuming course ID 2 has no teacher assigned
    response = client.delete(f"/courses/{course_id}/unassign-teacher")
    
    assert response.status_code == 400  # Expecting bad request status code
    assert response.json() == {"error": {"code": "E400", "message": "No teacher is currently assigned to this course."}}  # Error message

```