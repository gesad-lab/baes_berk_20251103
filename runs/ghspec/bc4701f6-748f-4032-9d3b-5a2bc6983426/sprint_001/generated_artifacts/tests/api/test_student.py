import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import Response

app = FastAPI()

# Assume we have a simple in-memory data store for the sake of example
students = {}

@app.post("/students", status_code=201)
def create_student(name: str):
    if not name:
        return {"error": {"code": "E001", "message": "Name is required."}}, 400
    student_id = len(students) + 1
    students[student_id] = {"id": student_id, "name": name}
    return students[student_id]

@app.get("/students/{student_id}")
def retrieve_student(student_id: int):
    student = students.get(student_id)
    if not student:
        return {"error": {"code": "E002", "message": "Student not found."}}, 404
    return student

# Test suite for the student API
client = TestClient(app)

def test_create_student():
    response: Response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}

def test_student_not_found():
    response: Response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not found."}}

def test_create_student_without_name():
    response: Response = client.post("/students", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}