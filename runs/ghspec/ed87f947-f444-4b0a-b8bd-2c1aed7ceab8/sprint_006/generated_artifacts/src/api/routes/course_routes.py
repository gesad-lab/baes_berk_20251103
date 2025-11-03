```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.models import Course, Teacher  # Assuming these models exist
from src.database import get_course_by_id, update_course_teacher

router = APIRouter()

class UpdateTeacherAssignment(BaseModel):
    teacher_id: Optional[int]

@router.put("/courses/{course_id}/assignTeacher", response_model=Course)
async def update_teacher_assignment(course_id: int, assignment: UpdateTeacherAssignment):
    """
    Update the teacher assigned to a specific course by course ID.

    Parameters:
        course_id (int): The ID of the course to update.
        assignment (UpdateTeacherAssignment): The new teacher assignment containing teacher ID.

    Returns:
        Course: The updated course details with the associated teacher information.
    
    Raises:
        HTTPException: If the course ID or teacher ID is invalid.
    """
    # Fetch the existing course from the database
    course = await get_course_by_id(course_id)
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    if assignment.teacher_id:
        # Validate the teacher ID; assuming a function exists to validate
        teacher = await Teacher.get_by_id(assignment.teacher_id)
        if not teacher:
            raise HTTPException(status_code=400, detail="Invalid teacher ID")

        # Update the course with the new teacher ID
        course.teacher_id = assignment.teacher_id
    
    updated_course = await update_course_teacher(course)
    
    return updated_course
```