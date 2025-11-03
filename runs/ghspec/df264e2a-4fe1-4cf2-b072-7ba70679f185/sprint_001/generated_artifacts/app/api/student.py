from fastapi import APIRouter, HTTPException
from app.models import Student
from app.database import get_student_by_id

router = APIRouter()

@router.get("/students/{id}", response_model=Student)
async def get_student(id: int):
    """
    Retrieve a specific student by ID.

    Parameters:
    - id: The unique identifier for the student.

    Returns:
    - The details of the student if found.
    
    Raises:
    - HTTPException with status code 404 if the student is not found.
    """
    student = get_student_by_id(id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return student