```python
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, validator
from src.database import get_db
from sqlalchemy.orm import Session
from src.models import Course  # Assuming the Course model is defined appropriately
from typing import List

router = APIRouter()

class CourseCreate(BaseModel):
    name: str
    level: str

    @validator('name')
    def name_must_not_be_empty(cls, value):
        if not value:
            raise ValueError('Course name must not be empty')
        return value

    @validator('level')
    def level_must_be_valid(cls, value):
        # Example validation for level; customize as per requirements
        valid_levels = ['beginner', 'intermediate', 'advanced']
        if value not in valid_levels:
            raise ValueError('Level must be one of: beginner, intermediate, advanced')
        return value

@router.post("/courses", response_description="Create a new course entry", response_model=CourseCreate)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course entry.

    Parameters:
    - course (CourseCreate): The course information provided by the user.
    - db (Session): The database session.

    Returns:
    - CourseCreate: The created course details.
    
    Raises:
    - HTTPException: 400 if the course creation fails due to invalid data.
    """
    try:
        # Create course instance
        new_course = Course(name=course.name, level=course.level)
        
        # Add the new course to the database
        db.add(new_course)
        db.commit()
        db.refresh(new_course)

        return new_course
    except Exception as e:
        db.rollback()  # Rollback for any errors
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/courses", response_description="Retrieve all courses", response_model=List[CourseCreate])
async def get_courses(db: Session = Depends(get_db)):
    """
    Retrieve a list of all courses.

    Parameters:
    - db (Session): The database session.

    Returns:
    - List[CourseCreate]: A list of all course entries.
    
    Raises:
    - HTTPException: 500 if fetching courses fails.
    """
    try:
        courses = db.query(Course).all()
        return courses
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not retrieve courses")
```