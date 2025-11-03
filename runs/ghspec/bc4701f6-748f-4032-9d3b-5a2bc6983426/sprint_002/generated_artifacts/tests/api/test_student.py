```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from httpx import Response
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Data model for Student
class Student(BaseModel):
    id: int
    name: str
    email: EmailStr

# Assume we have a simple in-memory data store for the sake of example
students = {}

@app.post("/students", status_code=201)
def create_student(student: Student):
    if not student.name:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name is required."}})
    if not student.email:
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Email is required."}})
    
    student_id = len(students) + 1
    students[student_id] = student.dict()
    students[student_id]['id'] = student_id
    return students[student_id]

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Student not found."}})
    return students[student_id]

# Test cases for student creation
client = TestClient(app)

def test_create_student_with_email():
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_create_student_missing_email():
    response = client.post("/students", json={"name": "John Doe", "email": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email is required."}}

def test_create_student_missing_name():
    response = client.post("/students", json={"name": "", "email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}

def test_get_student():
    client.post("/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Jane Doe", "email": "jane.doe@example.com"}

def test_get_nonexistent_student():
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Student not found."}}
```