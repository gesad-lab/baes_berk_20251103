```python
import pytest
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config

# Set up database connection
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize fastapi app
app = FastAPI()

@pytest.fixture(scope="module")
def client():
    # Initialize Alembic for migrations during startup
    alembic_cfg = Config("alembic.ini")
    
    # Execute migrations
    with engine.connect() as connection:
        command.upgrade(alembic_cfg, 'head')

    yield app.test_client()

def test_create_teacher(client):
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 201
    assert response.json() == {"message": "Teacher added successfully."}

def test_create_teacher_without_name(client):
    response = client.post("/teachers", json={"email": "jane@example.com"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name and email are required."
        }
    }

def test_get_teacher(client):
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane@example.com"
    }

def test_get_non_existing_teacher(client):
    response = client.get("/teachers/999")
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Teacher not found."
        }
    }
```