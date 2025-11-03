from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from .models.student import StudentCreate, StudentResponse  # Assuming these models exist

app = FastAPI()

# Sample in-memory storage for illustration purposes; replace with your database logic
students_db = []

class StudentCreate(BaseModel):
    name: str
    email: EmailStr

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate):
    # Check for unique email before creating a new student record
    if any(existing_student['email'] == student.email for existing_student in students_db):
        raise HTTPException(status_code=400, detail={"code": "E003", "message": "Email already exists"})
    
    # Create student record
    student_id = len(students_db) + 1  # Auto-incrementing ID
    new_student = {"id": student_id, "name": student.name, "email": student.email}
    students_db.append(new_student)
    return StudentResponse(**new_student)

@app.get("/students", response_model=List[StudentResponse])
async def get_students():
    if not students_db:
        raise HTTPException(status_code=404, detail={"code": "E004", "message": "No students found"})
    
    return [StudentResponse(**student) for student in students_db]  # Return all students with emails in JSON format