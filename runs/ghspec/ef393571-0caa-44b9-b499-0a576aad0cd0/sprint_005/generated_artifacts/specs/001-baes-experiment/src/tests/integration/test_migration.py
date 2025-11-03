```python
import pytest
from fastapi import FastAPI, HTTPException
from httpx import AsyncClient
from api.teachers import router as teachers_router
import aiosqlite

# Instantiate FastAPI app for testing purposes
app = FastAPI()
app.include_router(teachers_router)

DATABASE_URL = "database.db"

@pytest.fixture
async def setup_database():
    """Set up the database for testing and create the Teacher table."""
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS teacher (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        await db.commit()

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_create_teacher_success(client, setup_database):
    """Test creating a new Teacher with valid input."""
    teacher_data = {"name": "John Doe", "email": "john.doe@example.com"}
    response = await client.post("/teachers", json=teacher_data)
    
    assert response.status_code == 200
    assert response.json()["name"] == teacher_data["name"]
    assert response.json()["email"] == teacher_data["email"]

@pytest.mark.asyncio
async def test_create_teacher_invalid_email(client, setup_database):
    """Test creating a Teacher with an invalid email triggers an error."""
    teacher_data = {"name": "Jane Doe", "email": "invalid-email-format"}
    response = await client.post("/teachers", json=teacher_data)

    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"

@pytest.mark.asyncio
async def test_list_teachers(client, setup_database):
    """Test retrieving a list of all teachers."""
    teacher_data = {"name": "John Doe", "email": "john.doe@example.com"}
    await client.post("/teachers", json=teacher_data)  # Create a teacher for testing

    response = await client.get("/teachers")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Ensure we received at least one teacher
    assert response.json()[0]["name"] == teacher_data["name"]
    assert response.json()[0]["email"] == teacher_data["email"]

@pytest.mark.asyncio
async def test_create_teacher_duplicate_email(client, setup_database):
    """Test creating a Teacher with a duplicate email triggers an error."""
    teacher_data = {"name": "John Doe", "email": "john.doe@example.com"}
    await client.post("/teachers", json=teacher_data)  # Create first teacher

    response = await client.post("/teachers", json=teacher_data)  # Attempt to create duplicate
    assert response.status_code == 400  # Bad Request
    assert response.json()["detail"] == "UNIQUE constraint failed: teacher.email"

```