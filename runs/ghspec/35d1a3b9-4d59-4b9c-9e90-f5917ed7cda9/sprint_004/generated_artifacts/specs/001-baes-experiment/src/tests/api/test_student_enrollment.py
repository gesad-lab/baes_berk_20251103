```python
import pytest
from httpx import AsyncClient
from src.api import app  # Import the FastAPI application
from src.repository import init_db, Student, Course, StudentCourse  # Import the models
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.fixture
async def client():
    # This fixture provides a test client for making API requests
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    # Setup the database before running the test
    async with AsyncSession(init_db()) as session:
        # Create necessary tables before tests run, if they don't exist
        await session.run_sync(Student.metadata.create_all)
        await session.run_sync(Course.metadata.create_all)
        await session.run_sync(StudentCourse.metadata.create_all)
        yield  # Run tests
        # Optionally, tear down database objects after tests are finished

@pytest.mark.asyncio
async def test_enroll_student_in_courses(client):
    # Example test to enroll a student in courses
    response = await client.post("/api/enroll", json={
        "student_id": 1, 
        "course_ids": [1, 2, 3]
    })
    assert response.status_code == 201  # Expecting Created status
    assert response.json() == {"message": "Student enrolled successfully"}

@pytest.mark.asyncio
async def test_retrieve_courses_for_student(client):
    # Example test to retrieve courses for a specific student
    response = await client.get("/api/courses/1")
    assert response.status_code == 200  # Expecting OK status
    assert isinstance(response.json(), list)  # Should return a list of courses
```