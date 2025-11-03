```python
# File: src/api/course.py

from fastapi import APIRouter, HTTPException
from services.course_service import CourseService
from validators.course_validator import CourseValidator  # Import the course validator

router = APIRouter()

@router.post("/courses/{course_id}/assign-teacher")
async def assign_teacher(course_id: int, teacher_data: dict):
    """
    Assign a teacher to a course.

    Parameters:
    - course_id (int): The ID of the course to which a teacher will be assigned.
    - teacher_data (dict): A dictionary containing the "teacher_id" key.

    Returns:
    - JSON response with the updated course information.

    Raises:
    - HTTPException: If the teacher_id is invalid or the assignment fails.
    """
    # Validate teacher ID from request body
    CourseValidator.validate_teacher_id(teacher_data['teacher_id'])

    # Attempt to assign the teacher to the course
    updated_course = await CourseService.assign_teacher(course_id, teacher_data)
    return updated_course

@router.get("/courses/{course_id}")
async def retrieve_course(course_id: int):
    """
    Retrieve course details, including the assigned teacher.

    Parameters:
    - course_id (int): The ID of the course to retrieve.

    Returns:
    - JSON object with course details and assigned teacher's information.

    Raises:
    - HTTPException: If the course_id is not found.
    """
    course = await CourseService.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
```