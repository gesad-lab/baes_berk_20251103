```python
# tests/test_student_course.py
import pytest
from fastapi.testclient import TestClient
from pydantic import BaseModel, conlist
from src.main import app  # Assuming FastAPI app is created in main.py
from src.services.student_course_service import StudentCourseService  # Assuming this service is implemented
from src.models.course import Course

client = TestClient(app)

class AssignCoursesRequest(BaseModel):
    student_id: int
    course_ids: conlist(int, min_items=1)  # Ensure at least one course ID is provided

class RetrieveStudentCoursesRequest(BaseModel):
    student_id: int

class RemoveCoursesRequest(BaseModel):
    student_id: int
    course_ids: conlist(int, min_items=1)  # Ensure at least one course ID is provided

@pytest.fixture
def create_courses():
    """Fixture to create course entries before tests."""
    course_data_list = [
        {"name": "Mathematics", "level": "Beginner"},
        {"name": "Science", "level": "Intermediate"}
    ]
    course_ids = []
    for course_data in course_data_list:
        response = client.post("/courses", json=course_data)
        course_ids.append(response.json().get("id"))
    return course_ids

def test_assign_courses_to_student(create_courses):
    """Test assigning courses to a specific student."""
    student_id = 1  # Assuming a student with ID 1 exists
    request_data = AssignCoursesRequest(student_id=student_id, course_ids=create_courses)
    response = client.post("/students/assign_courses", json=request_data.dict())
    assert response.status_code == 200
    assert "courses" in response.json()  # Ensure that the response contains updated courses

def test_retrieve_student_courses():
    """Test retrieving a student's courses."""
    student_id = 1  # Assuming a student with ID 1 exists
    request_data = RetrieveStudentCoursesRequest(student_id=student_id)
    response = client.get(f"/students/{student_id}/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses

def test_remove_courses_from_student(create_courses):
    """Test removing courses from a specific student."""
    student_id = 1  # Assuming a student with ID 1 exists
    request_data = RemoveCoursesRequest(student_id=student_id, course_ids=create_courses[:1])  # Remove one course
    response = client.post("/students/remove_courses", json=request_data.dict())
    assert response.status_code == 200
    assert "courses" in response.json()  # Ensure that the response reflects updated courses after removal
```