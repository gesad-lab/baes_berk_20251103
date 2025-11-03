```python
import pytest
from httpx import AsyncClient
from src.main import app  # Assuming the FastAPI app is instantiated in main.py
from src.database import init_db  # Function to initialize and access the database
from src.models import Teacher, Course  # Importing the new Course and Teacher models

@pytest.fixture(scope="module")
async def test_client():
    # Initialize the database before the tests and create the necessary tables
    await init_db()
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client  # This will be the test Client to interact with the API


@pytest.mark.asyncio
async def test_create_course_with_teacher(test_client):
    # Create a new teacher for assignment
    teacher_response = await test_client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})
    assert teacher_response.status_code == 201  # Check that teacher was created successfully
    teacher_id = teacher_response.json()['id']  # Retrieve the teacher ID for later use

    # Create a new course
    course_response = await test_client.post("/courses", json={"name": "Mathematics"})
    assert course_response.status_code == 201  # Check that course was created successfully
    course_id = course_response.json()['id']  # Retrieve the course ID for later use

    # Assign teacher to the course
    assign_teacher_response = await test_client.post(f"/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})
    assert assign_teacher_response.status_code == 200  # Check that teacher was assigned successfully

    # Verify that the course now has the assigned teacher
    get_course_response = await test_client.get(f"/courses/{course_id}")
    assert get_course_response.status_code == 200
    course_data = get_course_response.json()
    assert course_data['teacher_id'] == teacher_id  # Ensure the course has the correct teacher assigned


@pytest.mark.asyncio
async def test_create_course_without_teacher(test_client):
    # Create a new course that should not be assigned a teacher
    course_response = await test_client.post("/courses", json={"name": "Physics"})
    assert course_response.status_code == 201  # Check that course was created successfully
    course_id = course_response.json()['id']  # Retrieve the course ID for later use

    # Verify that the course does not have a teacher assigned
    get_course_response = await test_client.get(f"/courses/{course_id}")
    assert get_course_response.status_code == 200
    course_data = get_course_response.json()
    assert course_data['teacher_id'] is None  # Ensure the course has no teacher assigned


@pytest.mark.asyncio
async def test_update_teacher_for_course(test_client):
    # Create a new teacher for assignment
    teacher_response = await test_client.post("/teachers", json={"name": "Jane Smith", "email": "jane@example.com"})
    assert teacher_response.status_code == 201  # Check that teacher was created successfully
    teacher_id = teacher_response.json()['id']  # Retrieve the teacher ID for later use

    # Create a new course
    course_response = await test_client.post("/courses", json={"name": "Chemistry"})
    assert course_response.status_code == 201  # Check that course was created successfully
    course_id = course_response.json()['id']  # Retrieve the course ID for later use

    # Assign teacher to the course
    await test_client.post(f"/courses/{course_id}/assign_teacher", json={"teacher_id": teacher_id})

    # Now update the teacher for the course
    new_teacher_response = await test_client.post("/teachers", json={"name": "Mike Johnson", "email": "mike@example.com"})
    assert new_teacher_response.status_code == 201  # Check that new_teacher was created successfully
    new_teacher_id = new_teacher_response.json()['id']  # Retrieve new teacher ID

    update_teacher_response = await test_client.put(f"/courses/{course_id}/update_teacher", json={"teacher_id": new_teacher_id})
    assert update_teacher_response.status_code == 200  # Check that teacher was updated successfully

    # Verify that the course now has the updated teacher assigned
    get_course_response = await test_client.get(f"/courses/{course_id}")
    assert get_course_response.status_code == 200
    course_data = get_course_response.json()
    assert course_data['teacher_id'] == new_teacher_id  # Ensure the course has the updated teacher assigned
```