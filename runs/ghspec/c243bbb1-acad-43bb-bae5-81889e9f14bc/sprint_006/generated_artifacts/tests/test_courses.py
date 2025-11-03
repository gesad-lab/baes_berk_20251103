```python
# tests/test_courses.py

import httpx
import pytest

BASE_URL = "http://localhost:8000/api/v1/courses"

@pytest.mark.asyncio
async def test_get_course_details_with_valid_id():
    """Test retrieving course details with a valid course ID."""
    course_id = 1  # Assuming a course with ID 1 exists

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{course_id}")
        assert response.status_code == 200  # Expecting a successful response
        assert "course_name" in response.json()  # Check if course details include the name
        assert "teacher_id" in response.json()  # Check if teacher association is present


@pytest.mark.asyncio
async def test_get_course_details_with_invalid_id():
    """Test retrieving course details with an invalid course ID."""
    course_id = 9999  # Assuming this course ID does not exist

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{course_id}")
        assert response.status_code == 404  # Expecting not found response
        assert response.json() == {"error": {"code": "E404", "message": "Course not found"}}  # Check specific error response
```