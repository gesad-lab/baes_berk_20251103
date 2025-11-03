```python
# Assuming the file is empty as no existing content was provided. 
# We will create unit tests for the FastAPI application in `test_api.py`.

import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Base, engine, Student
from sqlalchemy.orm import sessionmaker

# Create a test client
client = TestClient(app)

# Setup database for testing
@pytest.fixture(scope="module")
def setup_database():
    """Sets up the database for testing."""
    # Create the database and tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

# Test the creation of a student with a valid email
def test_create_student_with_valid_email(setup_database):
    response = client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Check for success
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

# Test the creation of a student with an invalid email
def test_create_student_with_invalid_email(setup_database):
    response = client.post("/students/", json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 422  # Check for Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"

# Test retrieving the created student
def test_get_student(setup_database):
    response = client.get("/students/1/")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

# Test updating a student's email
def test_update_student_email(setup_database):
    response = client.put("/students/1/", json={"name": "John Doe", "email": "john.new@example.com"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john.new@example.com"
    }

# Test retrieval of updated student
def test_get_updated_student(setup_database):
    response = client.get("/students/1/")
    assert response.status_code == 200
    assert response.json()["email"] == "john.new@example.com"
```