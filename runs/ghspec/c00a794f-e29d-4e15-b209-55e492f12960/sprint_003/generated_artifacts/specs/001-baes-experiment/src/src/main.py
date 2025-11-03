```python
# src/routes/course_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from models import Course
from database import get_db

router = APIRouter()

# Pydantic model for course creation
class CourseCreate(BaseModel):
    name: str
    level: str

# Pydantic model for course retrieval
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

@router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = next(get_db())):
    """
    Create a new course in the database.
    
    :param course: CourseCreate model containing the course name and level.
    :param db: Database session.
    :return: Created course response.
    """
    # Validate input
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Name and level are required")

    # Create a new course instance
    new_course = Course(name=course.name, level=course.level)

    # Add and commit the new course to the database
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course

@router.get("/courses", response_model=List[CourseResponse])
def get_courses(db: Session = next(get_db())):
    """
    Retrieve a list of all courses from the database.
    
    :param db: Database session.
    :return: List of courses.
    """
    # Query to get all courses
    courses = db.query(Course).all()
    return courses
```