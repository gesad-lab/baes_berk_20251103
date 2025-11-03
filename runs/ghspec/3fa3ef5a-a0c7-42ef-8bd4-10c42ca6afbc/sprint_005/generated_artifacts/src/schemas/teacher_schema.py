```python
# src/controllers/teacher_controller.py
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from src.services.teacher_service import TeacherService

router = APIRouter()

class TeacherCreateRequest(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@router.post("/teachers", response_model=TeacherResponse, status_code=status.HTTP_201_CREATED)
async def create_teacher(teacher_request: TeacherCreateRequest):
    """
    Create a new teacher.

    Args:
        teacher_request (TeacherCreateRequest): The teacher details to create.

    Returns:
        TeacherResponse: The created teacher details.
    
    Raises:
        HTTPException: If a teacher with the same email already exists or if an error occurs during creation.
    """
    try:
        teacher = await TeacherService.create_teacher(teacher_request.name, teacher_request.email)
        return teacher
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/teachers/{id}", response_model=TeacherResponse)
async def get_teacher(id: int):
    """
    Retrieve teacher details by ID.

    Args:
        id (int): The ID of the teacher to retrieve.

    Returns:
        TeacherResponse: The teacher details.

    Raises:
        HTTPException: If the teacher does not exist.
    """
    teacher = await TeacherService.get_teacher_by_id(id)
    if teacher is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    return teacher
```