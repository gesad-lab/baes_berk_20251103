```python
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from src.models.course import Course
from src.services.course_service import CourseService

router = APIRouter()

# Pydantic model for input validation when creating a course
class CourseCreate(BaseModel):
    name: str = Field(..., description="The name of the course")
    level: str = Field(..., description="The level of the course (e.g., beginner, intermediate, advanced)")

@router.post("/courses", response_model=Course, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate):
    """
    Create a new course in the system.

    Parameters:
    - course: CourseCreate - The course details

    Returns:
    - Course - The created course object
    """
    try:
        new_course = CourseService.create_course(course.name, course.level)
        return new_course
    except ValueError as ve:
        # Handle validation or business logic errors from the CourseService
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e:
        # Log unexpected errors and raise a server error
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An unexpected error occurred")
```