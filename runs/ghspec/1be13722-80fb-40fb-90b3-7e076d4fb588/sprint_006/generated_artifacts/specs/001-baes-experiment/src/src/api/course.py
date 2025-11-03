```python
# src/api/course.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.course import Course
from models.teacher import Teacher
from services.course_service import update_course_teacher, get_course_with_teacher

router = APIRouter()

class CourseTeacherUpdate(BaseModel):
    teacher_id: int

@router.put("/courses/{course_id}", response_model=Course)
async def update_course(course_id: int, teacher_update: CourseTeacherUpdate):
    """
    Update the teacher assignment for a given course.

    Parameters:
    - course_id: The ID of the course to update.
    - teacher_update: An object containing the teacher_id to assign to the course.

    Returns:
    - The updated Course object if successful.

    Raises:
    - HTTPException: If the course does not exist (404)
                     If the teacher_id is invalid (400)
    """
    try:
        updated_course = await update_course_teacher(course_id, teacher_update.teacher_id)
        if updated_course is None:
            raise HTTPException(status_code=404, detail="Course not found.")
        return updated_course
    except ValueError as e:
        # Handling the case where teacher_id is invalid
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: int):
    """
    Retrieve the details of a course including its assigned teacher.

    Parameters:
    - course_id: The ID of the course to retrieve.

    Returns:
    - The Course object including the teacher details.

    Raises:
    - HTTPException: If the course does not exist (404)
    """
    course = await get_course_with_teacher(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")
    return course
```