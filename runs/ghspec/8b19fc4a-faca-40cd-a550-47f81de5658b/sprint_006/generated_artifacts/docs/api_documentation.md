# File: tests/test_courses.py

import pytest
from httpx import AsyncClient
from main import app  # Assuming the FastAPI app is defined in main.py
from models.course import Course
from models.teacher import Teacher
from db import get_db  # Assuming this provides the database session
from sqlalchemy.orm import Session

@pytest.mark.asyncio
async def test_assign_teacher_to_course_succeeds():
    """Test assigning a Teacher to a Course with valid IDs."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a Teacher
        teacher_response = await client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})
        teacher_id = teacher_response.json().get("id")

        # Create a Course
        course_response = await client.post("/courses", json={"name": "Math 101"})
        course_id = course_response.json().get("id")

        # Assign Teacher to Course
        response = await client.post(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})
        assert response.status_code == 200
        assert response.json() == {"message": "Teacher assigned successfully."}

@pytest.mark.asyncio
async def test_assign_teacher_to_non_existing_course_fails():
    """Test assigning a Teacher to a non-existing Course."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a Teacher
        teacher_response = await client.post("/teachers", json={"name": "Jane Doe", "email": "jane@example.com"})
        teacher_id = teacher_response.json().get("id")

        # Attempt to assign Teacher to non-existing Course
        response = await client.post("/courses/999/assign-teacher", json={"teacher_id": teacher_id})
        assert response.status_code == 404
        assert response.json() == {"error": {"code": "E003", "message": "Course not found."}}

@pytest.mark.asyncio
async def test_assign_non_existing_teacher_to_course_fails():
    """Test assigning a non-existing Teacher to a Course."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a Course
        course_response = await client.post("/courses", json={"name": "Science 101"})
        course_id = course_response.json().get("id")

        # Attempt to assign non-existing Teacher to Course
        response = await client.post(f"/courses/{course_id}/assign-teacher", json={"teacher_id": 999})
        assert response.status_code == 404
        assert response.json() == {"error": {"code": "E004", "message": "Teacher not found."}}

@pytest.mark.asyncio
async def test_assign_teacher_without_teacher_id_fails():
    """Test assigning Teacher without providing a teacher_id."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a Course
        course_response = await client.post("/courses", json={"name": "History 101"})
        course_id = course_response.json().get("id")

        # Attempt to assign Teacher without teacher_id
        response = await client.post(f"/courses/{course_id}/assign-teacher", json={})
        assert response.status_code == 422  # Unprocessable Entity
        assert "detail" in response.json()  # Validate that details are present

@pytest.mark.asyncio
async def test_get_course_with_assigned_teacher_succeeds():
    """Test retrieving a Course that has a Teacher assigned."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a Teacher
        teacher_response = await client.post("/teachers", json={"name": "Mark Smith", "email": "mark@example.com"})
        teacher_id = teacher_response.json().get("id")

        # Create a Course
        course_response = await client.post("/courses", json={"name": "Geography 101"})
        course_id = course_response.json().get("id")

        # Assign Teacher to Course
        await client.post(f"/courses/{course_id}/assign-teacher", json={"teacher_id": teacher_id})

        # Get the Course
        response = await client.get(f"/courses/{course_id}")
        assert response.status_code == 200
        assert response.json()["teacher_id"] == teacher_id  # Ensure the assigned teacher is correctly returned