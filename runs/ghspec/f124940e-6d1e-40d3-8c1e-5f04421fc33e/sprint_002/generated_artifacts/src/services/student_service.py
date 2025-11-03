```python
# src/routers/student_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from src.services.student_service import (
    create_student,
    get_students,
    update_student_email,
)

router = APIRouter()

# Pydantic models for request and response
class StudentCreateRequest(BaseModel):
    name: str
    email: EmailStr  # Ensure valid email format

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students", response_model=StudentResponse, status_code=201)
async def create_student_endpoint(student: StudentCreateRequest):
    """Create a new student record."""
    created_student = await create_student(student.name, student.email)
    return created_student

@router.get("/students", response_model=list[StudentResponse])
async def retrieve_students():
    """Retrieve all student records."""
    students = await get_students()
    return students

@router.put("/students/{student_id}/email", response_model=StudentResponse)
async def update_student_email_endpoint(student_id: int, email: EmailStr):
    """Update the email address of an existing student."""
    updated_student = await update_student_email(student_id, email)
    
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return updated_student
```