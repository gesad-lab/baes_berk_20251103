```python
# tests/test_student_courses.py

import pytest
from httpx import AsyncClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.mark.asyncio
async def test_enroll_student_in_courses():
    """Test enrolling a student in valid courses."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a test student first
        student_response = await client.post("/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
        student_id = student_response.json().get("id")

        # Create test courses
        course_response = await client.post("/courses", json={"name": "Biology", "level": "Intermediate"})
        course_id = course_response.json().get("id")
        
        # Enroll student in created courses
        enroll_response = await client.post(f"/students/{student_id}/courses", json={"course_ids": [course_id]})
        
        # Assert that enrollment was successful
        assert enroll_response.status_code == 200
        assert enroll_response.json().get("message") == "Enrollment successful."

@pytest.mark.asyncio
async def test_retrieve_student_courses():
    """Test retrieving courses for a specific student."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a test student
        student_response = await client.post("/students", json={"name": "John Smith", "email": "john.smith@example.com"})
        student_id = student_response.json().get("id")

        # Create test courses
        course_response_1 = await client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
        course_response_2 = await client.post("/courses", json={"name": "Physics", "level": "Intermediate"})
        course_ids = [course_response_1.json().get("id"), course_response_2.json().get("id")]

        # Enroll student in these courses
        await client.post(f"/students/{student_id}/courses", json={"course_ids": course_ids})

        # Retrieve courses for the student
        retrieve_response = await client.get(f"/students/{student_id}/courses")
        
        # Assert correct courses are returned
        assert retrieve_response.status_code == 200
        assert len(retrieve_response.json()) == 2  # Student should have 2 courses

@pytest.mark.asyncio
async def test_enroll_student_in_non_existent_courses():
    """Test error handling when trying to enroll a student in non-existent courses."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a test student
        student_response = await client.post("/students", json={"name": "Alice", "email": "alice@example.com"})
        student_id = student_response.json().get("id")

        # Attempt to enroll in non-existent courses
        enroll_response = await client.post(f"/students/{student_id}/courses", json={"course_ids": [999, 1000]})

        # Assert that an error is returned
        assert enroll_response.status_code == 404
        assert enroll_response.json().get("error", {}).get("code") == "E003"  # COURSE_NOT_FOUND error code
        assert enroll_response.json().get("error", {}).get("message") == "Course not found."
```