```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from models.course import Course  # Assuming there's a Course model in the specified location
from database.db import get_db  # Database session utility, assuming a similar utility exists

router = APIRouter()

class CourseCreate(BaseModel):
    name: constr(strict=True, min_length=1)  # Course name must be a non-empty string
    level: constr(strict=True, min_length=1)  # Course level must be a non-empty string

@router.post("/courses", response_model=Course, status_code=201)
async def create_course(course: CourseCreate):
    """
    Create a new course.
    
    Parameters:
    - course: CourseCreate model including `name` and `level`.

    Returns:
    - Course object data with ID, name, and level.

    Raises:
    - HTTPException: If name or level is missing or invalid.
    """
    # Input validation is managed by Pydantic, if no validation errors are raised, we proceed to create the course

    db = get_db()  # Get the database session
    new_course = Course(name=course.name, level=course.level)  # Create a new course instance
    db.add(new_course)  # Add the course to the session
    try:
        db.commit()  # Commit the transaction to the database
        db.refresh(new_course)  # Refresh the instance to get the database assigned ID
    except Exception as e:
        db.rollback()  # Roll back the transaction on error
        raise HTTPException(status_code=500, detail="Failed to create course.")  # Handle unforeseen exceptions

    return new_course  # Return the created course data
```