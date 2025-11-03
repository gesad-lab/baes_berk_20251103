```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student  # Assuming a models.py defines the Student model and Base for SQLAlchemy
from main import app, get_db  # Assume the FastAPI app is in main.py with a dependency for db session

# Setting up the test database and FastAPI client
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope='module')
def db():
    # Create the database schema
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope='module')
def client():
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as c:
        yield c

def test_create_student_valid(client):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}

def test_retrieve_student(client):
    # First create a student to retrieve
    client.post("/students", json={"name": "Jane Doe"})
    response = client.get("/students/1")  # Assuming the ID of the student created is 1
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Jane Doe"}

def test_create_student_without_name(client):
    response = client.post("/students", json={})  # No name provided
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required"}}  # Assuming this is the error format

def test_schema_creation_on_startup(client):
    # The schema creation is implicitly tested, but we can validate by checking if the Student table exists
    with TestingSessionLocal() as session:
        result = session.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students';").fetchone()
        assert result is not None  # Ensure the 'students' table exists
```