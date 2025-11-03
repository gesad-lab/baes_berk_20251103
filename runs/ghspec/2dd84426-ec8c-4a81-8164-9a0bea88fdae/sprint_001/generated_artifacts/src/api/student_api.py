from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.services.student_service import create_student_service, get_all_students_service
from src.database import initialize_database

app = FastAPI()

# Input model for creating a new student
class StudentCreate(BaseModel):
    name: str  # Student name field (required)

# Output model for a student
class Student(BaseModel):
    id: int
    name: str

# Initialize the database when the application starts
@app.on_event("startup")
async def startup_event():
    initialize_database()

# Route to create a new student
@app.post("/students", response_model=Student, status_code=201)
async def create_student(student: StudentCreate):
    # Call service function to create a student
    created_student = create_student_service(student.name)
    return created_student

# Route to retrieve all students
@app.get("/students", response_model=List[Student], status_code=200)
async def get_all_students():
    # Call service function to get all students
    students = get_all_students_service()
    return students