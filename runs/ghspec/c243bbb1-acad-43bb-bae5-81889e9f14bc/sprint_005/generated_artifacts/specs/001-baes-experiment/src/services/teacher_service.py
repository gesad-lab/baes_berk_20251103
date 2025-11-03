# api/teachers.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from services.teacher_service import create_teacher, get_teacher_by_id

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/teachers", response_model=TeacherResponse, status_code=201)
async def create_new_teacher(teacher: TeacherCreate):
    """
    Create a new Teacher.

    - **name**: The name of the teacher (required)
    - **email**: The email of the teacher (required)
    """
    try:
        created_teacher = await create_teacher(teacher.name, teacher.email)
        return TeacherResponse(id=created_teacher.id, name=created_teacher.name, email=created_teacher.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
async def retrieve_teacher(teacher_id: int):
    """
    Retrieve details of a teacher by ID.

    - **teacher_id**: The ID of the teacher (required)
    """
    teacher = await get_teacher_by_id(teacher_id)
    
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    return TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)