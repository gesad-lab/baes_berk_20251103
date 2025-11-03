from fastapi import APIRouter, HTTPException
from src.models.course import Course
from src.services.course_service import get_course_with_teacher_service

router = APIRouter()

@router.get("/courses/{course_id}")
async def get_course_with_teacher(course_id: int):
    """
    Retrieve a Course along with the associated Teacher information by Course ID.

    Parameters:
    - course_id: The ID of the Course to retrieve.

    Returns:
    - Course details, including information about the associated Teacher.

    Raises:
    - HTTPException: if the Course with the given ID does not exist.
    """
    course_with_teacher = await get_course_with_teacher_service(course_id)
    
    if not course_with_teacher:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    return course_with_teacher