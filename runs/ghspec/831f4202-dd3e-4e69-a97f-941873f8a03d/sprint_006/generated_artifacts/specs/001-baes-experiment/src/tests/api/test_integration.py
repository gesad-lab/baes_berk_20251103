```python
import pytest
from httpx import AsyncClient
from src.main import app  # Assuming the FastAPI app is instantiated in main.py
from src.database import init_db  # Function to initialize and access the database
from src.models import Teacher  # Importing the new Teacher model
from src.models import Course  # Importing the Course model for updates

@pytest.fixture(scope="module")
async def test_client():
    # Initialize the database before the tests and create the necessary tables
    await init_db()
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_assign_teacher_to_course(test_client):
    # Test assigning a teacher to a course
    course_id = 1  # Assuming a course with ID 1 exists
    teacher_id = 1  # Assuming a teacher with ID 1 exists
    
    response = await test_client.post(f"/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher assigned successfully"

@pytest.mark.asyncio
async def test_assign_teacher_to_nonexistent_course(test_client):
    # Test assigning a teacher to a nonexistent course
    response = await test_client.post("/courses/999/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E404"
    assert response.json()["error"]["message"] == "Course not found"

@pytest.mark.asyncio
async def test_assign_teacher_with_invalid_teacher_id(test_client):
    # Test assigning a teacher with an invalid teacher_id
    course_id = 1  # Assuming a course with ID 1 exists
    response = await test_client.post(f"/courses/{course_id}/assign_teacher", json={"teacher_id": "invalid"})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E400"
    assert response.json()["error"]["message"] == "Invalid teacher ID"

@pytest.mark.asyncio
async def test_update_teacher_assignment(test_client):
    # Test updating the teacher assigned to a course
    course_id = 1  # Assuming a course with ID 1 exists
    new_teacher_id = 2  # Assuming a teacher with ID 2 exists

    response = await test_client.put(f"/courses/{course_id}/update_teacher", json={"teacher_id": new_teacher_id})
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher updated successfully"

@pytest.mark.asyncio
async def test_update_teacher_assignment_to_nonexistent_course(test_client):
    # Test updating a teacher assignment for a nonexistent course
    response = await test_client.put("/courses/999/update_teacher", json={"teacher_id": 2})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E404"
    assert response.json()["error"]["message"] == "Course not found"

@pytest.mark.asyncio
async def test_view_courses_with_assigned_teachers(test_client):
    # Test viewing courses with assigned teachers
    response = await test_client.get("/courses")
    assert response.status_code == 200
    # Expect at least one course returned with an assigned teacher
    assert len(response.json()) > 0
    for course in response.json():
        assert "teacher_id" in course  # Each course should have a teacher_id

@pytest.mark.asyncio
async def test_view_unassigned_courses(test_client):
    # Test the response for unassigned courses
    response = await test_client.get("/courses")
    assert response.status_code == 200
    unassigned_courses = [course for course in response.json() if course["teacher_id"] is None]
    assert len(unassigned_courses) > 0  # Expect at least one course to be unassigned
```
