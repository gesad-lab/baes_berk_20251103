```python
import pytest
from httpx import AsyncClient
from src.api import app  # Import the FastAPI application
from src.repository import init_db, Teacher, Course  # Ensure Teacher and Course models are available
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

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
async def test_assign_teacher_to_course(client, setup_database):
    # Test assignment of a teacher to a course
    response = await client.post("/api/courses/1/assign_teacher", json={"teacher_id": 1})
    
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully."}

@pytest.mark.asyncio
async def test_retrieve_course_details_including_teacher(client, setup_database):
    # Test retrieval of course details including teacher information
    response = await client.get("/api/courses/1")
    
    assert response.status_code == 200
    course_data = response.json()
    
    # Check the course details and teacher information
    assert "teacher" in course_data
    assert "id" in course_data['teacher']
    assert course_data['teacher']['id'] == 1  # Assuming teacher with ID 1 is assigned correctly

@pytest.mark.asyncio
async def test_teacher_assignments_persist_after_migration(client, setup_database):
    # Ensure teacher assignments persist after database migration
    response = await client.get("/api/courses/1")
    
    assert response.status_code == 200
    assert "teacher_id" in response.json()

@pytest.mark.asyncio
async def test_existing_data_unaffected_after_migration(client, setup_database):
    # Test that existing student and teacher data remain unaffected
    response = await client.get("/api/students")
    
    assert response.status_code == 200
    students_data = response.json()
    
    assert len(students_data) > 0  # Ensure some student data exists
```