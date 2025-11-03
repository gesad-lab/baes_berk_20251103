```python
# /src/api/teacher.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.teacher import Teacher  # Import the Teacher model
from services.teacher_service import create_teacher_service, retrieve_teacher_service  # Import service methods

router = APIRouter()

class TeacherCreate(BaseModel):
    """Schema for creating a new teacher."""
    name: str
    email: str

@router.post("/teachers", response_model=Teacher, status_code=201)
async def create_teacher_endpoint(teacher: TeacherCreate):
    """
    Create a new teacher record.

    Parameters:
    - teacher: TeacherCreate - The details of the teacher to create.

    Returns:
    - Teacher: The created teacher record.
    
    Raises:
    - HTTPException: If the creation fails due to validation errors.
    """
    try:
        return await create_teacher_service(teacher.name, teacher.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/teachers/{teacher_id}", response_model=Teacher)
async def retrieve_teacher_endpoint(teacher_id: int):
    """
    Retrieve a teacher's details by their ID.

    Parameters:
    - teacher_id: int - The ID of the teacher to retrieve.

    Returns:
    - Teacher: The details of the requested teacher.

    Raises:
    - HTTPException: If the teacher with given ID is not found.
    """
    teacher = await retrieve_teacher_service(teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher
```