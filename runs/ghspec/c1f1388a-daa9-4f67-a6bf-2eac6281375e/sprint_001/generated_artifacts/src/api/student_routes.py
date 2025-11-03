```python
from fastapi import APIRouter, HTTPException, status
from typing import List
from src.models.student import Student
from src.schemas.student import StudentCreate, StudentResponse
from src.services.student_service import (
    create_student,
    get_student_by_id,
    get_all_students
)

router = APIRouter()

@router.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_new_student(student: StudentCreate):
    """
    Create a new student entry.
    
    Parameters:
    - student: StudentCreate - Data model for creating a student.
    
    Returns:
    - StudentResponse: A response model with the created student's details.
    
    Raises:
    - HTTPException: If a database error occurs.
    """
    try:
        return await create_student(student)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/students/{student_id}", response_model=StudentResponse)
async def read_student(student_id: int):
    """
    Retrieve a student by their ID.
    
    Parameters:
    - student_id: int - The ID of the student to retrieve.
    
    Returns:
    - StudentResponse: A response model with the student's details.
    
    Raises:
    - HTTPException: If student is not found or a database error occurs.
    """
    student = await get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

@router.get("/students", response_model=List[StudentResponse])
async def read_all_students():
    """
    Retrieve all students.
    
    Returns:
    - List[StudentResponse]: A list of students.
    
    Raises:
    - HTTPException: If a database error occurs.
    """
    try:
        return await get_all_students()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```