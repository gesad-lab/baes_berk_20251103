```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from src.models.course import Course  # Assuming the Course model is in src/models/course.py
from src.services.course_service import create_course, get_course, update_course, list_courses  # Assuming CRUD operations are in a service

router = APIRouter()

class CourseCreateRequest(BaseModel):
    name: str
    level: str

class CourseUpdateRequest(BaseModel):
    name: Optional[str] = None
    level: Optional[str] = None

@router.post("/courses", response_model=Course)
async def create_course_endpoint(course: CourseCreateRequest):
    """
    Create a new Course.

    Args:
        course (CourseCreateRequest): Information about the course to create.

    Returns:
        Course: The created course object with identifier.
    """
    return await create_course(course.name, course.level)

@router.get("/courses/{id}", response_model=Course)
async def get_course_endpoint(id: int):
    """
    Retrieve a specific Course by its ID.

    Args:
        id (int): The unique identifier for the course.

    Returns:
        Course: The requested course object.

    Raises:
        HTTPException: If the course does not exist.
    """
    course = await get_course(id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/courses/{id}", response_model=Course)
async def update_course_endpoint(id: int, course_update: CourseUpdateRequest):
    """
    Update the details of an existing Course.

    Args:
        id (int): The unique identifier for the course.
        course_update (CourseUpdateRequest): Fields to update for the course.

    Returns:
        Course: The updated course object.

    Raises:
        HTTPException: If the course does not exist.
    """
    updated_course = await update_course(id, course_update.name, course_update.level)
    if not updated_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course

@router.get("/courses", response_model=List[Course])
async def list_courses_endpoint():
    """
    List all Courses.

    Returns:
        List[Course]: A list of all course objects.
    """
    return await list_courses()
```