```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from src.service.student_service import create_student, get_student_by_id
from src.model.student import Student

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use Pydantic's built-in email validation

@router.post("/students", status_code=201)
async def create_student_endpoint(student: StudentCreate):
    """
    Create a new student with name and email.
    Parameters:
    - student: StudentCreate model containing name and email.

    Returns:
    - The created student's details including id, name, and email.
    """
    try:
        created_student = await create_student(student.name, student.email)
        return {"id": created_student.id, "name": created_student.name, "email": created_student.email}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/students/{student_id}")
async def get_student_endpoint(student_id: int):
    """
    Retrieve a student by ID.
    Parameters:
    - student_id: ID of the student to retrieve.

    Returns:
    - The student's details including name and email.
    """
    student = await get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return {"id": student.id, "name": student.name, "email": student.email}
```