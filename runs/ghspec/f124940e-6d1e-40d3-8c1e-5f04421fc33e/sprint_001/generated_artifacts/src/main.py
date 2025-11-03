```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from myapp.database import init_db, drop_db
from myapp.models import Student
from myapp.main import app  # Assuming the main app is in main.py

app.dependency_overrides[init_db] = lambda: None  # Override db init for testing

@pytest.fixture(scope="module")
def client():
    # Initialize database and create test client
    init_db()
    with TestClient(app) as client:
        yield client
    drop_db()  # Clean up after tests

def test_delete_student(client):
    # First, create a student to be deleted
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    created_student = response.json()
    student_id = created_student["id"]

    # Now, delete the student by ID
    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 204  # No Content indicates successful deletion

    # Attempt to retrieve the deleted student to confirm it was removed
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404  # Student should not be found
    assert response.json() == {"detail": "Student not found"}  # Assuming this is the error response
```