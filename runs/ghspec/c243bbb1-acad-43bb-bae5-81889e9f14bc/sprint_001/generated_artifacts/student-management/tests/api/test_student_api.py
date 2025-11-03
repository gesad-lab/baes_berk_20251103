```python
import pytest
from httpx import AsyncClient
from main import app  # Assuming main.py contains the FastAPI app instance

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_create_student(client):
    """Test creating a student via the API."""
    response = await client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # Expecting 201 Created
    assert response.json() == {
        "message": "Student created successfully.",
        "student": {"id": 1, "name": "John Doe"},
    }

@pytest.mark.asyncio
async def test_create_student_missing_name(client):
    """Test creating a student without a name returns a validation error."""
    response = await client.post("/students", json={})
    assert response.status_code == 400  # Expecting 400 Bad Request
    assert response.json() == {
        "detail": "The 'name' field is required."
    }

@pytest.mark.asyncio
async def test_get_students(client):
    """Test retrieving students from the API."""
    await client.post("/students", json={"name": "Jane Doe"})  # Create a student for the test
    response = await client.get("/students")
    assert response.status_code == 200  # Expecting 200 OK
    assert len(response.json()) == 2  # There should be 2 students now
    assert any(student["name"] == "John Doe" for student in response.json())
    assert any(student["name"] == "Jane Doe" for student in response.json())
```