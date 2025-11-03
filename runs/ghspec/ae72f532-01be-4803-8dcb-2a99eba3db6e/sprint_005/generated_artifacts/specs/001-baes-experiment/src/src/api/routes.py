```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from src.services.teacher_service import create_teacher, get_teacher_by_id
from src.models.teacher import Teacher  # Assuming the Teacher model is defined in this module

router = APIRouter()

# Pydantic model for Teacher creation request
class TeacherCreateRequest(BaseModel):
    name: str
    email: EmailStr

# Response model for Teacher data
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@router.post("/teachers/", response_model=TeacherResponse)
def create_teacher_record(teacher: TeacherCreateRequest):
    """
    Create a new Teacher record.

    Args:
        teacher (TeacherCreateRequest): The Teacher data for creation.

    Returns:
        TeacherResponse: The created Teacher data.
    
    Raises:
        HTTPException: If creation fails due to validation errors or database issues.
    """
    try:
        new_teacher = create_teacher(teacher.name, teacher.email)
        return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)
    except Exception as e:  # Catch specific exceptions later as needed
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def retrieve_teacher(teacher_id: int):
    """
    Retrieve a Teacher record by ID.

    Args:
        teacher_id (int): The ID of the Teacher to retrieve.

    Returns:
        TeacherResponse: The Teacher data.
    
    Raises:
        HTTPException: If the Teacher is not found.
    """
    teacher = get_teacher_by_id(teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    return TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)
```