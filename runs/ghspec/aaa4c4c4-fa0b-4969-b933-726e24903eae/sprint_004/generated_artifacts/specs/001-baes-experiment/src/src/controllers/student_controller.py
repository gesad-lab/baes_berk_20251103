```python
# src/controllers/student_controller.py

from fastapi import APIRouter, HTTPException, Path
from typing import List
from pydantic import BaseModel
from models import Student, Course  # Assuming these models exist based on provided context
from database import get_student_with_courses, enroll_student_in_courses  # Assuming these functions are defined in a service layer

router = APIRouter()

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

class StudentResponse(BaseModel):
    id: int
    name: str
    courses: List[CourseResponse]

@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_student_details(student_id: int = Path(..., title="The ID of the student to retrieve")):
    """
    Retrieve student details along with their enrolled courses.

    Args:
        student_id (int): The ID of the student.

    Returns:
        StudentResponse: The student's details including enrolled courses.
    
    Raises:
        HTTPException: If the student is not found.
    """
    student = await get_student_with_courses(student_id)
    
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return StudentResponse(
        id=student.id,
        name=student.name,
        courses=[CourseResponse(id=course.id, name=course.name, level=course.level) for course in student.courses]
    )
```