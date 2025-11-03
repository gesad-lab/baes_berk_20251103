from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from models import Teacher
from services.teacher_service import TeacherService

app = FastAPI()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@app.post("/teachers", response_model=TeacherResponse)
async def create_teacher(teacher: TeacherCreate):
    """
    Create a new teacher record.

    Parameters:
    - teacher: TeacherCreate containing name and email of the teacher.

    Returns:
    - TeacherResponse: The created teacher's details.

    Raises:
    - HTTPException: If missing required fields or email already exists.
    """
    try:
        new_teacher = TeacherService.create_teacher(name=teacher.name, email=teacher.email)
        return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)
    except ValueError as e:  # Handle validation errors from TeacherService
        raise HTTPException(status_code=400, detail=str(e))  # Return a 400 error for client-side issues
    except Exception as e:  # Handle any unexpected errors
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")  # Return a 500 error for server issues