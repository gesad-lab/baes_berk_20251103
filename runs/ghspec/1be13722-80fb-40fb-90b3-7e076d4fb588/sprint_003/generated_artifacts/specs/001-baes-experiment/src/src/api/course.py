```python
# src/api/course.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from models.course import Course  # Assuming this is the model for the Course entity
from services.course_service import create_course, get_all_courses  # Assuming these functions exist

router = APIRouter()

class CourseCreate(BaseModel):
    name: str = Field(..., max_length=100, description="The name of the course, cannot exceed 100 characters.")
    level: str = Field(..., max_length=50, description="The level of the course, cannot exceed 50 characters.")

@router.post("/courses", response_model=Course, status_code=201)
async def create_course_endpoint(course: CourseCreate):
    """
    Create a new course in the system.
    Expects a JSON object with 'name' and 'level'.

    Args:
        course (CourseCreate): A CourseCreate object.

    Returns:
        Course: The created course object.
    """
    # Validate input (this will be handled by pydantic)
    return await create_course(course)

@router.get("/courses", response_model=List[Course])
async def retrieve_courses_endpoint():
    """
    Retrieve all courses from the system.

    Returns:
        List[Course]: A list of all courses in the system.
    """
    return await get_all_courses()
```