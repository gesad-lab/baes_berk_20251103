from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, EmailStr, Field
from typing import List
from src.models import Student  # Importing the Student model
from src.database import get_students_from_db, add_student_to_db  # Database interactions

router = APIRouter()

class StudentCreate(BaseModel):
    name: str = Field(..., title="Name of the student", example="John Doe")
    email: EmailStr = Field(..., title="Email of the student", example="john.doe@example.com")

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate):
    """
    Create a new student record.
    
    - **student**: The student information to be stored, including name and email.
    
    Returns the created student's information if successful.
    """
    try:
        student_id = await add_student_to_db(student.name, student.email)
        return StudentResponse(id=student_id, name=student.name, email=student.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/students", response_model=List[StudentResponse])
async def get_students():
    """
    Retrieve a list of all student records.

    Returns a list of students including their names and email addresses.
    """
    students = await get_students_from_db()
    return [StudentResponse(id=student.id, name=student.name, email=student.email) for student in students]