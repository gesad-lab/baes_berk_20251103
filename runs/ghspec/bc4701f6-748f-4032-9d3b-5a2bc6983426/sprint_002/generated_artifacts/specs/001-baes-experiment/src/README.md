```
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import Response

app = FastAPI()

# Assume we have a simple in-memory data store for the sake of example
students = {}

@app.post("/students", status_code=201)
def create_student(name: str, email: str):
    """Creates a new student with the given name and email.

    Args:
        name (str): The name of the student.
        email (str): The email of the student.

    Returns:
        dict: Created student data including id, name, and email.
    """
    if not name:
        return {"error": {"code": "E001", "message": "Name is required."}}, 400
    if not email or "@" not in email:  # Basic email validation
        return {"error": {"code": "E002", "message": "Valid email is required."}}, 400
    student_id = len(students) + 1
    students[student_id] = {"id": student_id, "name": name, "email": email}
    return students[student_id]

@app.get("/students/{student_id}", response_model=dict)
def get_student(student_id: int):
    """Retrieves a student by their ID.

    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        dict: Student data if found, otherwise 404 Not Found.
    """
    student = students.get(student_id)
    if not student:
        return {"error": {"code": "E003", "message": "Student not found."}}, 404
    return student

# Test cases to verify the new email functionality
client = TestClient(app)

def test_create_student_with_valid_email():
    response = client.post("/students", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Alice", "email": "alice@example.com"}

def test_create_student_without_name():
    response = client.post("/students", json={"email": "bob@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}

def test_create_student_with_invalid_email():
    response = client.post("/students", json={"name": "Bob", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Valid email is required."}}

def test_get_student():
    client.post("/students", json={"name": "Charlie", "email": "charlie@example.com"})
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Charlie", "email": "charlie@example.com"}

def test_get_nonexistent_student():
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Student not found."}}
```