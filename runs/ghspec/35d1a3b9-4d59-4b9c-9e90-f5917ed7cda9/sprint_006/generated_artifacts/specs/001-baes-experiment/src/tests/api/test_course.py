```python
import pytest
from httpx import AsyncClient
from src.api import app  # Import the FastAPI application
from src.repository import init_db, Course, Teacher  # Import Course and Teacher models
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.fixture
async def client():
    # This fixture provides a test client for making API requests
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    # Initialize the database for tests
    async with AsyncSession() as session:
        await init_db(session)

@pytest.mark.asyncio
async def test_assign_teacher_to_course(client):
    """
    Test assigning a teacher to a course.
    This test assumes that both the Teacher and Course entities are already created.
    """
    teacher_id = 1  # Assuming there is a teacher with this ID
    course_id = 1    # Assuming there is a course with this ID

    response = await client.post(
        f"/api/courses/{course_id}/assign-teacher",
        json={"teacher_id": teacher_id}
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully."}

@pytest.mark.asyncio
async def test_retrieve_course_with_teacher(client):
    """
    Test retrieving course details along with the assigned teacher's information.
    This test assumes the course has been linked to a teacher.
    """
    course_id = 1  # Assuming a course with this ID exists

    response = await client.get(f"/api/courses/{course_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == course_id
    assert "teacher" in data  # Ensure teacher information is included
    assert data["teacher"]["id"] == 1  # Assuming the teacher ID is known

```