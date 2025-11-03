```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.course_service import CourseService
from models.course import Course as CourseModel

router = APIRouter()

# Pydantic model for course creation
class CourseCreate(BaseModel):
    name: str
    level: str

@router.post("/courses/", response_model=CourseModel)
async def create_course(course_create: CourseCreate, course_service: CourseService = Depends()):
    """
    Create a new course.

    :param course_create: Data for the course to be created
    :param course_service: CourseService dependency for business logic
    :return: The created course
    :raises HTTPException: If the course creation fails
    """
    # Validate the incoming data and create the course
    try:
        course = await course_service.create_course(course_create.name, course_create.level)
        return course
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```
