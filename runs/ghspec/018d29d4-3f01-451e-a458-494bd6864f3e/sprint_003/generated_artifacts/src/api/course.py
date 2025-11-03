```python
# src/api/course.py

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field, ValidationError
from typing import List
import logging

# Setting up structured logging
logger = logging.getLogger(__name__)

# Assuming there's a function to create database connection/session
from database import get_session  # Placeholder for actual database session retrieval
from models import Course  # Assuming Course is defined in models
from services import validate_course_data  # Assuming there's a service for validation

router = APIRouter()

# Pydantic model for course creation
class CourseCreate(BaseModel):
    name: str = Field(..., description="The name of the course")
    level: str = Field(..., description="The level of the course")

@router.post("/courses", response_model=Course, status_code=201)
async def create_course(course_data: CourseCreate, session: Depends(get_session)):
    """
    Create a new course entity in the database.
    
    Parameters:
    - course_data: CourseCreate model with required fields
    
    Returns:
    - Course instance created in the database
    """
    # Log incoming request
    logger.info("Creating course with name: %s and level: %s", course_data.name, course_data.level)
    
    # Validate course data using a separate service function
    try:
        validate_course_data(course_data)
    except ValidationError as e:
        logger.error("Validation failed for course data: %s", e.errors())
        raise HTTPException(status_code=400, detail="Validation error: Required fields are missing or invalid.")

    # Create the Course record in the database
    new_course = Course(name=course_data.name, level=course_data.level)

    # Persist to database
    session.add(new_course)
    try:
        session.commit()
        session.refresh(new_course)
        logger.info("Course created successfully with ID: %s", new_course.id)
    except Exception as e:
        logger.error("Error while creating course: %s", str(e))
        session.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error: Unable to create course.")

    return new_course

@router.get("/courses", response_model=List[Course], status_code=200)
async def get_courses(session: Depends(get_session)):
    """
    Retrieve all courses from the database.
    
    Returns:
    - A list of Course instances
    """
    logger.info("Fetching all courses.")
    courses = session.query(Course).all()
    logger.info("Fetched %d courses from database.", len(courses))
    return courses
```