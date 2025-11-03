```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from src.models.course import Course  # Import Course model
from src.services.course_service import create_course, get_all_courses  # Import service functions
from src.validation.course_validation import validate_course_data  # Import validation function

router = APIRouter()

class CourseCreate(BaseModel):
    name: str
    level: str

class CourseResponse(BaseModel):
    name: str
    level: str

@router.post("/courses", response_model=CourseResponse, status_code=201)
async def post_course(course: CourseCreate):
    """
    Create a new course with the specified name and level.
    
    Parameters:
        course (CourseCreate): The course data including name and level.

    Returns:
        CourseResponse: The created course data.
    """
    try:
        # Validate course data
        validate_course_data(course.dict())
        
        # Create course in the database
        created_course = create_course(course.name, course.level)
        
        return created_course
    except ValueError as e:
        # Raise an error if data validation fails
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/courses", response_model=List[CourseResponse])
async def get_courses():
    """
    Retrieve all courses from the database.

    Returns:
        List[CourseResponse]: A list of all courses.
    """
    courses = get_all_courses()
    return courses
```