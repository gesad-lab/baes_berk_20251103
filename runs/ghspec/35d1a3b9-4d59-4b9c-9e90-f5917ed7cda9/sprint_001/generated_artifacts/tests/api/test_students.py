import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from src.api import app  # Import the FastAPI application
from src.repository import init_db, get_session, Student

@pytest.fixture
def client():
    # This fixture provides a test client for making API requests
    with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Setup the database before running the tests
    init_db()  # Function to initialize the database
    yield
    # Assume we do not drop the database in tests, but you can add cleanup if necessary

@pytest.mark.asyncio
async def test_create_student(client):
    # Test API endpoint for creating a student
    response = await client.post("/students/", json={"name": "John Doe"})
    assert response.status_code == 201  # Check if the response code is 201 Created
    data = response.json()
    assert data["name"] == "John Doe"  # Verify the name returned matches the input

@pytest.mark.asyncio
async def test_create_student_empty_name(client):
    # Test API endpoint for creating a student without a name (invalid case)
    response = await client.post("/students/", json={"name": ""})
    assert response.status_code == 400  # Bad Request due to empty name
    assert response.json()["error"]["code"] == "E001"  # Check for specific error code

@pytest.mark.asyncio
async def test_retrieve_students(client):
    # Test API endpoint for retrieving all students
    response = await client.get("/students/")
    assert response.status_code == 200  # Check if the response code is 200 OK
    data = response.json()
    assert isinstance(data, list)  # Verify that the response is a list
    assert len(data) > 0  # Ensure there is at least one student

@pytest.mark.asyncio
async def test_retrieve_students_no_records(client):
    # Test API endpoint for retrieving students when none exist
    # This logic may depend on dataset reset between tests
    await client.delete("/students/")  # Optional: Assume we can clear students for test
    response = await client.get("/students/")
    assert response.status_code == 200  # Check if the response code is still 200 OK
    assert response.json() == []  # Confirm that the list is empty