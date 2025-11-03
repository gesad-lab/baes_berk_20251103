```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
from typing import Optional
from models import Student  # Assuming Student model is defined in models.py
from database import get_student_by_id, create_student_in_db, is_email_duplicate  # Assuming these methods are defined in a database module

app = FastAPI()

class StudentCreate(BaseModel):
    name: str  # Required field
    email: EmailStr  # Required field with email format validation

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate):
    if await is_email_duplicate(student.email):
        raise HTTPException(status_code=400, detail="Email already exists.")

    # Create new student in the database
    student_id = await create_student_in_db(student.name, student.email)
    
    return StudentResponse(id=student_id, name=student.name, email=student.email)

@app.get("/students/{student_id}", response_model=StudentResponse)
async def retrieve_student(student_id: int):
    student = await get_student_by_id(student_id)
    
    if student is None:
        raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "Student not found."}})

    return StudentResponse(id=student.id, name=student.name, email=student.email)
```