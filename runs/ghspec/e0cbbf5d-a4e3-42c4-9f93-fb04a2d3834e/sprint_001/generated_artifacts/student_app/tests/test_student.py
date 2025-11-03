```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.database.db import get_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Setting up the database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture to create the database
@pytest.fixture(scope='module')
def test_app():
    # Create the database and tables
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)  # Cleanup after tests

def test_create_student(test_app):
    # Test successful student creation
    response = test_app.post("/students", json={"name": "Alice"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Alice"

    # Test creating a student without a name
    response = test_app.post("/students", json={"name": ""})
    assert response.status_code == 400
    assert response.json() == {"error": "E001: Name cannot be empty."}

    # Test creating a student with missing name field
    response = test_app.post("/students", json={})
    assert response.status_code == 400
    assert response.json() == {"error": "E001: Name is a required field."}

def test_retrieve_students(test_app):
    # First create a student to test retrieval
    test_app.post("/students", json={"name": "Bob"})
    
    # Retrieve all students
    response = test_app.get("/students")
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)  # Ensure it's a list
    assert len(data) > 0  # List should not be empty
    assert all("id" in student for student in data)
    assert all("name" in student for student in data)
```