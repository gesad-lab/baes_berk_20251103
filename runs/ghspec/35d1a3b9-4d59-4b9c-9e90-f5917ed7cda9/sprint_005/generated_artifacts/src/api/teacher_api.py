```python
# src/api/teacher_api.py

from fastapi import APIRouter, HTTPException
from src.services.teacher_service import service_create_teacher, service_get_teacher_by_id
from pydantic import BaseModel, EmailStr

router = APIRouter()

class TeacherCreateRequest(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/teachers/", response_model=TeacherResponse)
async def create_teacher(teacher: TeacherCreateRequest):
    """
    Create a new teacher in the system.
    
    Args:
        teacher (TeacherCreateRequest): The request body containing teacher's name and email.

    Returns:
        TeacherResponse: The created teacher's information.
    
    Raises:
        HTTPException: If there's an error creating the teacher, such as a duplicate email.
    """
    try:
        new_teacher = await service_create_teacher(teacher.name, teacher.email)
        return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
async def get_teacher(teacher_id: int):
    """
    Retrieve a teacher's information by ID.
    
    Args:
        teacher_id (int): The unique identifier of the teacher.

    Returns:
        TeacherResponse: The teacher's information.
    
    Raises:
        HTTPException: If the teacher is not found.
    """
    teacher = await service_get_teacher_by_id(teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)
```