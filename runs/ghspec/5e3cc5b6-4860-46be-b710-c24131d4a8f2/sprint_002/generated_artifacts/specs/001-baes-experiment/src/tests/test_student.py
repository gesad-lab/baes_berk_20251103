```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create the database tables
    yield
    Base.metadata.drop_all(bind=engine)    # Drop the database tables after tests

# Test Case for creating a student with valid email
def test_create_student_with_email():
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "john@example.com"

# Test Case for creating a student with an invalid email format
def test_create_student_with_invalid_email():
    response = client.post("/students", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json()["error"]["message"] == "Invalid email format"

# Test Case for retrieving a student by ID, including their email
def test_retrieve_student_by_id_with_email():
    # First, create a student to retrieve
    create_response = client.post("/students", json={"name": "Jane Doe", "email": "jane@example.com"})
    student_id = create_response.json()["id"]

    # Retrieve the student by ID
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "jane@example.com"

# Test Case for updating a student's email
def test_update_student_email():
    # First, create a student to update
    create_response = client.post("/students", json={"name": "Mark Smith", "email": "mark@example.com"})
    student_id = create_response.json()["id"]

    # Update the student's email
    response = client.put(f"/students/{student_id}", json={"name": "Mark Smith", "email": "mark.smith@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "mark.smith@example.com"

# Test Case for handling invalid email input on update
def test_update_student_with_invalid_email():
    # First, create a student to update
    create_response = client.post("/students", json={"name": "Lucy Brown", "email": "lucy@example.com"})
    student_id = create_response.json()["id"]

    # Attempt to update the student's email with an invalid format
    response = client.put(f"/students/{student_id}", json={"name": "Lucy Brown", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json()["error"]["message"] == "Invalid email format"
```