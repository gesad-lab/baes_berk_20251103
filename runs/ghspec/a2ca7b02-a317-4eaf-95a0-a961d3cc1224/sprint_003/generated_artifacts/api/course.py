```python
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, constr
from services.course_service import CourseService
from validators.course_validator import CourseValidator
from models.course import Course

router = APIRouter()

class CourseRequest(BaseModel):
    name: str
    level: constr(regex=r'^(beginner|intermediate|advanced)$')  # Valid levels only

@router.post("/courses", response_model=Course)
async def create_course(course: CourseRequest):
    """
    Create a new course.

    :param course: CourseRequest object containing name and level of the course.
    :raises HTTPException: If the input validation fails.
    :return: Created Course object.
    """
    if not course.name:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Course name is required."}}
        )
    
    if not course.level:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E002", "message": "Course level is required."}}
        )

    # Here we validate the level with predefined levels
    valid_levels = {'beginner', 'intermediate', 'advanced'}
    if course.level not in valid_levels:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E003", "message": "Invalid course level format."}}
        )

    # Call the CourseService to create the course
    return CourseService.create_course(course)
  
@router.get("/courses")
async def retrieve_courses():
    """
    Retrieve all courses.

    :return: List of Course objects.
    """
    return CourseService.get_all_courses()
```