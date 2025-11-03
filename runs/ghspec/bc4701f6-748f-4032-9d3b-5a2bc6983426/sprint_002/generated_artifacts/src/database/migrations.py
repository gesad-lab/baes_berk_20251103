```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, EmailStr
from typing import Dict

app = FastAPI()

# Assume we have a simple in-memory data store for the sake of example
students: Dict[int, Dict[str, str]] = {}

# Pydantic model for student creation
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr for email validation

# Pydantic model for student response
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    # Check for required fields (validated by Pydantic)
    student_id = len(students) + 1
    students[student_id] = {"id": student_id, "name": student.name, "email": student.email}
    return students[student_id]

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    # Retrieve student details by ID
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]
```