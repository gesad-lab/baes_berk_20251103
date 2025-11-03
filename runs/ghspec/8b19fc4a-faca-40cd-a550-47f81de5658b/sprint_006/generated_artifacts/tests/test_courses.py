```python
# tests/test_courses.py

import pytest
from httpx import AsyncClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.mark.asyncio
async def test_assign_teacher_to_course_succeeds():
    """Test assigning a Teacher to a Course successfully."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
        assert response.status_code == 200
        assert response.json() == {"message": "Teacher assigned successfully."}

@pytest.mark.asyncio
async def test_retrieve_course_info_including_teacher():
    """Test retrieving Course details along with Teacher info."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/courses/1")
        assert response.status_code == 200
        assert "teacher" in response.json()

@pytest.mark.asyncio
async def test_update_teacher_assignment_for_course_succeeds():
    """Test updating the Teacher assigned to a Course successfully."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/courses/1/assign-teacher", json={"teacher_id": 2})
        assert response.status_code == 200
        assert response.json() == {"message": "Teacher assignment updated successfully."}

@pytest.mark.asyncio
async def test_error_handling_for_invalid_course_teacher_relationship():
    """Test error handling for assigning a Teacher to a nonexistent Course."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/courses/999/assign-teacher", json={"teacher_id": 1})
        assert response.status_code == 404
        assert response.json() == {"error": {"code": "E003", "message": "Course not found."}}

@pytest.mark.asyncio
async def test_validate_teacher_assignment_limitations():
    """Test preventing multiple Teachers from being assigned to the same Course."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        await client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
        response = await client.post("/courses/1/assign-teacher", json={"teacher_id": 2})
        assert response.status_code == 400
        assert response.json() == {"error": {"code": "E004", "message": "Course already has an assigned Teacher."}}
```