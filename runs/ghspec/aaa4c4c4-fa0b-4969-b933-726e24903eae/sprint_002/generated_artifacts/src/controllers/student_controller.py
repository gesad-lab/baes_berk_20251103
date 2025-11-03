```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from models import Student  # Assuming Student model is defined in models.py
from database import get_students, create_student as save_student  # Assuming these functions interact with the database

router = APIRouter()


class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Validate email format


@router.post("/students", response_model=Student)
async def create_student(student: StudentCreate):
    """
    Create a new student record.

    Parameters:
    - student: StudentCreate model that includes name and email.

    Returns:
    - Student object containing the new student record.

    Raises:
    - HTTPException: If the email is missing or invalid.
    """
    if not student.email:  # Explicit check for email
        raise HTTPException(status_code=400, detail="Email is required.")
    
    # Create the student record in the database
    created_student = await save_student(student)
    
    return created_student


@router.get("/students", response_model=List[Student])
async def get_all_students():
    """
    Retrieve all student records.

    Returns:
    - List of Student objects.
    """
    students = await get_students()
    return students
```