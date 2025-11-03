```python
# src/routers/student_router.py

from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel, EmailStr  # Importing EmailStr for email validation
from src.models import Student  # Assuming the Student model is located in src/models.py
from src.services import student_service  # Assuming the CRUD logic is folded in a service module

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Using EmailStr for built-in email validation

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students/", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate):
    """
    Create a new student in the database.
    
    Args:
        student (StudentCreate): The student data to create.
        
    Returns:
        StudentResponse: The created student record.
    """
    created_student = await student_service.create_student(student)
    return created_student

@router.get("/students/", response_model=List[StudentResponse], status_code=200)
async def get_students():
    """
    Retrieve all students.
    
    Returns:
        List[StudentResponse]: A list of student records.
    """
    students = await student_service.get_all_students()
    return students

@router.put("/students/{student_id}", response_model=StudentResponse, status_code=200)
async def update_student(student_id: int, student: StudentCreate):
    """
    Update an existing student.
    
    Args:
        student_id (int): The ID of the student to update.
        student (StudentCreate): The updated student data.
    
    Returns:
        StudentResponse: The updated student record.
    """
    updated_student = await student_service.update_student(student_id, student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student
```