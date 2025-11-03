```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI()

# Assuming we have a pre-defined database model Student
class Student(BaseModel):
    id: int
    name: str
    email: EmailStr  # New email field as per specifications

# Mock database (for demonstration purposes)
students_db = []

@app.post("/students", response_model=Student, status_code=201)
async def create_student(student: Student):
    """Create a new student and return the created student."""
    students_db.append(student)
    return student

@app.get("/students/{id}", response_model=Student)
async def get_student(id: int):
    """Retrieve a student by ID."""
    for student in students_db:
        if student.id == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{id}", response_model=Student)
async def update_student(id: int, student: Student):
    """Update an existing student by ID."""
    for index, existing_student in enumerate(students_db):
        if existing_student.id == id:
            students_db[index] = student
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.get("/students", response_model=List[Student])
async def list_students():
    """List all students."""
    return students_db

@app.delete("/students/{id}", status_code=204)
async def delete_student(id: int):
    """Delete a student by ID."""
    for index, student in enumerate(students_db):
        if student.id == id:
            del students_db[index]
            return
    raise HTTPException(status_code=404, detail="Student not found")
```