```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py
from models.teacher import Teacher  # Importing the Teacher model
from schemas.teacher_schema import CreateTeacherRequestSchema, TeacherSchema  # Importing schemas
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.course import Course  # Importing the Course model
from schemas.course_schema import UpdateCourseRequestSchema  # Importing course update schema
from database import get_db  # Importing the database session dependency

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up and tear down the database for integration tests.
    """
    # Code to set up the database
    pass

def test_assign_teacher_to_course_with_valid_teacher_id(setup_database):
    # Step 1: Create a teacher
    response = client.post("/teachers/", json={"name": "John Doe", "email": "john@example.com"})
    teacher_id = response.json().get("id")
    
    # Step 2: Create a course
    response = client.post("/courses/", json={"name": "Math 101"})
    course_id = response.json().get("id")
    
    # Step 3: Assign the teacher to the course
    update_request = {"teacher_id": teacher_id}
    response = client.patch(f"/courses/{course_id}", json=update_request)

    # Step 4: Assert the response contains updated course information with teacher details
    assert response.status_code == 200
    assert response.json()["teacher_id"] == teacher_id

def test_assign_teacher_to_course_with_invalid_teacher_id(setup_database):
    # Step 1: Create a course
    response = client.post("/courses/", json={"name": "Science 101"})
    course_id = response.json().get("id")
    
    # Step 2: Attempt to assign a non-existent teacher to the course
    update_request = {"teacher_id": 9999}  # Assuming this ID does not exist
    response = client.patch(f"/courses/{course_id}", json=update_request)

    # Step 3: Assert an error response is returned
    assert response.status_code == 400  # Expect Bad Request
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Teacher does not exist.",
            "details": {}
        }
    }
```