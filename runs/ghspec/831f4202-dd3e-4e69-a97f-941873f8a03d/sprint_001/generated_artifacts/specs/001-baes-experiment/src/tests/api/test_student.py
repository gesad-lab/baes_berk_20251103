import pytest
from httpx import AsyncClient
from src.main import app  # Assuming the FastAPI app is instantiated in main.py
from src.database import init_db  # This should contain a function to initialize the database
from src.models import Student  # The Student model should be defined appropriately to match the database schema


@pytest.fixture(scope="module")
async def test_client():
    # Initialize the database before the tests and create the necessary tables
    await init_db()
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_add_student_success(test_client):
    response = await test_client.post("/students", json={"name": "John Doe"})
    
    assert response.status_code == 201  # Check for the created status
    assert response.json() == {"message": "Student added successfully"}

    # Verify that the student was added to the database
    student = await Student.query.where(Student.name == "John Doe").gino.first()
    assert student is not None
    assert student.name == "John Doe"


@pytest.mark.asyncio
async def test_get_students_success(test_client):
    response = await test_client.get("/students")

    assert response.status_code == 200  # Check for successful retrieval
    data = response.json()
    assert isinstance(data, list)  # Ensure the response is a list
    assert any(student['name'] == "John Doe" for student in data)  # Verify that the previously added student is in the list


@pytest.mark.asyncio
async def test_add_student_empty_name(test_client):
    response = await test_client.post("/students", json={"name": ""})

    assert response.status_code == 400  # Check for bad request status
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required",
            "details": {}
        }
    }  # Check for the appropriate error message


@pytest.mark.asyncio
async def test_add_student_with_none_name(test_client):
    response = await test_client.post("/students", json={"name": None})

    assert response.status_code == 400  # Check for bad request status
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required",
            "details": {}
        }
    }  # Check for the appropriate error message