```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, constr
from src.repository import Course, get_session  # Assuming the Course model and get_session are defined
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

class CourseCreate(BaseModel):
    name: constr(min_length=1, max_length=100)  # Required string that cannot be empty
    level: constr(min_length=1, max_length=50)  # Required string that cannot be empty

@router.post("/courses/", response_model=CourseCreate)
async def create_course(course: CourseCreate):
    """
    Create a new course.

    Parameters:
    - course: The course data containing name and level.

    Returns:
    - The created course data.
    """
    db: Session = get_session()
    db_course = Course(name=course.name, level=course.level)  # Create course instance
    db.add(db_course)  # Add course to the session
    try:
        db.commit()  # Commit the transaction
        db.refresh(db_course)  # Refresh the instance to get the updated state
        return db_course  # Return the created course
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail="Could not create course.") from e

@router.get("/courses/", response_model=List[CourseCreate])
async def get_courses():
    """
    Retrieve all courses.

    Returns:
    - A list of courses with their name and level.
    """
    db: Session = get_session()
    courses = db.query(Course).all()  # Query to get all courses
    return courses  # Return the list of courses

# Include the router in the main FastAPI app in the 'main.py' file or equivalent.
```