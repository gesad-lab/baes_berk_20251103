```python
# tests/test_students.py

import httpx
import pytest

BASE_URL = "http://localhost:8000/api/v1/students"

@pytest.mark.asyncio
async def test_enroll_student_in_course_with_valid_data():
    """Test enrolling a student in a course with a valid course ID."""
    student_id = 1  # Assuming this student exists
    course_id = 1   # Assuming this course exists
    enroll_url = f"{BASE_URL}/{student_id}/courses"

    async with httpx.AsyncClient() as client:
        response = await client.post(enroll_url, json={"course_id": course_id})

    assert response.status_code == 200
    assert response.json() == {"message": "Student successfully enrolled in course."}

@pytest.mark.asyncio
async def test_retrieve_student_courses():
    """Test retrieving courses for a student."""
    student_id = 1  # Assuming this student exists
    courses_url = f"{BASE_URL}/{student_id}/courses"

    async with httpx.AsyncClient() as client:
        response = await client.get(courses_url)

    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of courses
    # Further assertions can be made about course attributes if needed

@pytest.mark.asyncio
async def test_enroll_student_in_course_with_invalid_course_id():
    """Test enrolling a student with an invalid course ID."""
    student_id = 1  # Assuming this student exists
    invalid_course_id = 9999  # Assuming this does not exist
    enroll_url = f"{BASE_URL}/{student_id}/courses"

    async with httpx.AsyncClient() as client:
        response = await client.post(enroll_url, json={"course_id": invalid_course_id})

    assert response.status_code == 400  # Expecting a 400 Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "The specified course does not exist."}}
```