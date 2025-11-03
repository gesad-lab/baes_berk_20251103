# tests/test_students_api.py

import httpx
import pytest

BASE_URL = "http://localhost:8000/api/v1/students"

@pytest.mark.asyncio
async def test_enroll_student_in_course():
    """Test enrolling a student in a course."""
    # Assume we already have a student with ID 1 and a course with ID 1 in the database
    student_id = 1
    course_id = 1
    enrollment_data = {
        "course_id": course_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/{student_id}/enroll", json=enrollment_data)

    assert response.status_code == 200  # Expecting a 200 OK status for successful enrollment
    assert response.json() == {"message": "Student enrolled successfully."}  # Expecting a success message

@pytest.mark.asyncio
async def test_get_student_courses():
    """Test retrieving courses for a student."""
    student_id = 1  # Assume there is a student with ID 1

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{student_id}/courses")

    assert response.status_code == 200  # Expecting a 200 OK status for successful retrieval
    # Expecting a list of courses, assume the student is enrolled in two courses
    assert isinstance(response.json(), list)  # Must be a list
    assert len(response.json()) > 0  # Must be at least one course in the response