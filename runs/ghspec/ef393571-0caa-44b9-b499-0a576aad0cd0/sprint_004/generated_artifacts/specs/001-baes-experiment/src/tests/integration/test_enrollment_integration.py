```python
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from src.api.enrollment import router as enrollment_router

# Instantiate FastAPI app for testing purposes
app = FastAPI()
app.include_router(enrollment_router)

@pytest.mark.asyncio
async def test_enroll_student(client: AsyncClient, student_id: int, course_id: int):
    """Test successful enrollment of a student in a course."""
    response = await client.post(f"/students/{student_id}/courses", json={"course_id": course_id})
    assert response.status_code == 200
    assert response.json() == {"message": "Student enrolled successfully."}

@pytest.mark.asyncio
async def test_enroll_student_invalid_course(client: AsyncClient, student_id: int):
    """Test error response when trying to enroll a student in an invalid course."""
    response = await client.post(f"/students/{student_id}/courses", json={"course_id": -1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Course not found."}}

@pytest.mark.asyncio
async def test_get_student_courses(client: AsyncClient, student_id: int, expected_courses: list):
    """Test retrieving courses associated with a student."""
    response = await client.get(f"/students/{student_id}/courses")
    assert response.status_code == 200
    assert response.json() == {"courses": expected_courses}

@pytest.mark.asyncio
async def test_get_students_enrolled_in_course(client: AsyncClient, course_id: int, expected_students: list):
    """Test retrieving students enrolled in a specific course."""
    response = await client.get(f"/courses/{course_id}/students")
    assert response.status_code == 200
    assert response.json() == {"students": expected_students}
```