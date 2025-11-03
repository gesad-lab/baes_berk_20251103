```python
import pytest
from httpx import AsyncClient
from src.main import app  # FastAPI app instance
from src.database import init_db  # Database initialization function
from src.models import Student, Course  # Importing necessary models

@pytest.fixture(scope="module")
async def test_client():
    # Initialize the database before the tests and create the necessary tables
    await init_db()

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client  # This will allow tests to use the client

@pytest.mark.asyncio
async def test_associate_student_with_course(test_client):
    # Create a student and a course for testing
    student_data = {"name": "John Doe", "email": "john.doe@example.com"}
    course_data = {"title": "Mathematics 101"}

    # Step 1: Register the student
    response = await test_client.post("/api/v1/students", json=student_data)
    assert response.status_code == 201  # Check if creation is successful
    student_id = response.json().get("id")

    # Step 2: Create the course
    response = await test_client.post("/api/v1/courses", json=course_data)
    assert response.status_code == 201  # Check if creation is successful
    course_id = response.json().get("id")

    # Step 3: Associate the student with the course
    association_response = await test_client.post(f"/api/v1/students/{student_id}/courses/{course_id}")
    assert association_response.status_code == 200  # Check if association is successful
    assert association_response.json() == {"message": "Student associated with course successfully."}

    # Verify the student's course association
    student_courses_response = await test_client.get(f"/api/v1/students/{student_id}/courses")
    assert student_courses_response.status_code == 200
    associated_courses = student_courses_response.json()
    assert len(associated_courses) == 1
    assert associated_courses[0]['id'] == course_id

@pytest.mark.asyncio
async def test_associate_student_with_invalid_course(test_client):
    student_data = {"name": "Jane Doe", "email": "jane.doe@example.com"}
    
    # Step 1: Register a new student
    response = await test_client.post("/api/v1/students", json=student_data)
    assert response.status_code == 201
    student_id = response.json().get("id")

    # Step 2: Attempt to associate the student with an invalid course ID
    invalid_course_id = 9999  # Assuming this ID does not exist
    association_response = await test_client.post(f"/api/v1/students/{student_id}/courses/{invalid_course_id}")

    # Check if the error response is as expected
    assert association_response.status_code == 400
    error_response = association_response.json()
    assert error_response == {"error": {"code": "E002", "message": "Invalid course ID."}}

@pytest.mark.asyncio
async def test_get_courses_for_nonexistent_student(test_client):
    # Attempt to retrieve courses for a student that does not exist
    non_existent_student_id = 9999  # Assuming this ID does not exist
    response = await test_client.get(f"/api/v1/students/{non_existent_student_id}/courses")

    assert response.status_code == 404  # Expecting not found error
    error_response = response.json()
    assert error_response == {"error": {"code": "E001", "message": "Student not found."}}
```