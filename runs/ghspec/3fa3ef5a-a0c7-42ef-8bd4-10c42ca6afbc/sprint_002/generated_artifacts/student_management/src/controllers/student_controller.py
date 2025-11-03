from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

# Assuming we have a service module that handles business logic
from src.services.student_service import create_student, get_all_students

router = APIRouter()

# Request model for creating a student
class StudentCreateRequest(BaseModel):
    name: str
    email: EmailStr  # Using Pydantic's EmailStr for email validation

# Response model for returning student data
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students/", response_model=StudentResponse)
async def create_new_student(student: StudentCreateRequest):
    """
    Create a new student and return the created student's details.
    
    :param student: StudentCreateRequest object containing name and email.
    :return: StudentResponse object with created student data.
    """
    try:
        new_student = await create_student(student.name, student.email)
        return StudentResponse(id=new_student.id, name=new_student.name, email=new_student.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/students/", response_model=List[StudentResponse])
async def list_students():
    """
    Retrieve the list of all students.
    
    :return: A list of StudentResponse objects.
    """
    students = await get_all_students()
    return [StudentResponse(id=student.id, name=student.name, email=student.email) for student in students]

# Ensure the router is included in your main FastAPI application in main.py
# app.include_router(router)