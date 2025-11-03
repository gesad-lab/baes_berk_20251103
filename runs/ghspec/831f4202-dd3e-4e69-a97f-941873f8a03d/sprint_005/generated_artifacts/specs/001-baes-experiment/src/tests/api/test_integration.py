```python
import pytest
from httpx import AsyncClient
from src.main import app  # Assuming the FastAPI app is instantiated in main.py
from src.database import init_db  # Function to initialize and access the database
from src.models import Teacher  # Importing the new Teacher model

@pytest.fixture(scope="module")
async def test_client():
    # Initialize the database before the tests and create the necessary tables
    await init_db()
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client  # This allows us to use the client in tests

@pytest.mark.asyncio
async def test_create_teacher():
    # Test creating a new teacher with valid data
    response = await test_client().post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Check that creation was successful
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

@pytest.mark.asyncio
async def test_create_teacher_with_invalid_email():
    # Test creating a teacher with an invalid email
    response = await test_client().post("/teachers", json={"name": "Jane Doe", "email": "invalid_email"})
    assert response.status_code == 400  # Bad request due to email validation

@pytest.mark.asyncio
async def test_get_all_teachers():
    # Test retrieving all teachers
    response = await test_client().get("/teachers")
    assert response.status_code == 200  # Successful retrieval
    assert isinstance(response.json(), list)  # Expect a list of teachers
    for teacher in response.json():
        assert "name" in teacher and "email" in teacher  # Ensure each teacher has name and email

@pytest.mark.asyncio
async def test_teacher_uniqueness():
    # Test that creating a teacher with the same email returns an error
    await test_client().post("/teachers", json={"name": "Alice Smith", "email": "alice.smith@example.com"})
    response = await test_client().post("/teachers", json={"name": "Bob Williams", "email": "alice.smith@example.com"})
    assert response.status_code == 400  # Conflicting email should cause a validation error
```