```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.teacher import Teacher
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create the database tables
    yield
    Base.metadata.drop_all(bind=engine)  # Clean up after tests

# Test case for creating a Teacher
def test_create_teacher():
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

# Test case for validating required fields
def test_create_teacher_missing_fields():
    response = client.post("/teachers", json={"name": ""})  # Missing email
    assert response.status_code == 400
    assert "name" in response.json()["error"]["message"]  # Check for error message

# Test case for retrieving a Teacher
def test_get_teacher():
    # First, create a Teacher to retrieve
    create_response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    teacher_id = create_response.json()["id"]

    response = client.get(f"/teachers/{teacher_id}")  # Use the created teacher's ID
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane.doe@example.com"

# Test case for verifying existing data remains intact
def test_preserve_existing_data():
    # Create a Teacher while assuming existing Students and Courses exist
    response = client.post("/teachers", json={"name": "Jim Beam", "email": "jim.beam@example.com"})
    assert response.status_code == 201

    # Check existing data (stub for demonstration, needs your specific check)
    response_students = client.get("/students")
    response_courses = client.get("/courses")
    assert response_students.status_code == 200
    assert response_courses.status_code == 200
```