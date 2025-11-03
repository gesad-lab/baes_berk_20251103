```python
import pytest
from httpx import AsyncClient
from src.main import app  # Assuming the FastAPI app is instantiated in main.py
from src.database import init_db  # Function to initialize and access the database
from src.models import Student, Course  # Importing the Student and Course models

@pytest.fixture(scope="module")
async def test_client():
    # Initialize the database before the tests and create the necessary tables
    await init_db()
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_enroll_student_in_courses(test_client):
    """Test to enroll a student in one or more courses."""
    student_id = 1  # Assuming a student with ID 1 exists in the db
    courses_payload = {"course_ids": [1, 2]}  # Assuming courses with IDs 1 and 2 exist

    response = await test_client.post(f"/students/{student_id}/courses", json=courses_payload)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Student enrolled in courses successfully."}

@pytest.mark.asyncio
async def test_get_student_details_with_courses(test_client):
    """Test to retrieve student details including their associated courses."""
    student_id = 1  # Assuming a student with ID 1 exists

    response = await test_client.get(f"/students/{student_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == student_id
    assert "courses" in data  # Ensure courses field is included
    assert isinstance(data["courses"], list)  # Ensure the courses are returned as a list

@pytest.mark.asyncio
async def test_enroll_student_with_invalid_course(test_client):
    """Test to ensure appropriate error when trying to enroll a student in non-existing courses."""
    student_id = 1  # Assuming a student with ID 1 exists
    invalid_courses_payload = {"course_ids": [999]}  # Course ID 999 assumed to not exist

    response = await test_client.post(f"/students/{student_id}/courses", json=invalid_courses_payload)

    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid course IDs provided."}}

@pytest.mark.asyncio
async def test_get_courses_for_student(test_client):
    """Test to retrieve all courses associated with a specific student."""
    student_id = 1  # Assuming a student with ID 1 exists

    response = await test_client.get(f"/students/{student_id}/courses")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Ensure the response is a list of courses
    # Further checks can be included to validate course contents if necessary
```