```python
import json
from fastapi import APIRouter, HTTPException
from src.db.models import Course, Teacher
from src.validations.course_validators import validate_teacher_id

router = APIRouter()

@router.patch("/courses/{course_id}")
async def assign_teacher_to_course(course_id: int, teacher_id: int):
    """Assign a teacher to a course.

    Args:
        course_id (int): The ID of the course to update.
        teacher_id (int): The ID of the teacher to assign to the course.

    Raises:
        HTTPException: If the teacher_id is invalid or if the course doesn't exist.
    
    Returns:
        JSON: Details of the updated course.
    """
    
    # Validate the teacher ID
    if not await validate_teacher_id(teacher_id):
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Invalid teacher_id", "details": {}}}
        )

    # Retrieve the course from the database
    course = await Course.get(course_id)
    if not course:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E002", "message": "Course not found", "details": {}}}
        )

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    await course.save()

    # Return the updated course details
    return {"course_id": course.id, "teacher_id": course.teacher_id}
```