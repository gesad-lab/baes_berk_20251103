```python
# src/api/courses.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Dict
from src.database import get_db  # Assuming you have a function to get a DB session
from src.models import Course  # Assuming the Course model is defined in src/models.py

router = APIRouter()

# Pydantic model for request validation
class CourseUpdate(BaseModel):
    name: str
    level: str

@router.put("/api/v1/courses/{course_id}", response_model=CourseUpdate)
def update_course(course_id: int, course_data: CourseUpdate, db: Session = next(get_db())):
    """
    Update an existing course by ID.

    Parameters:
    - course_id: ID of the course to be updated.
    - course_data: Updated course information.

    Returns:
    A dictionary containing the updated course details.

    Raises:
    HTTPException: If the course ID is not found in the database.
    """
    # Retrieve the course from the database
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if course is None:
        # If the course does not exist, raise a 404 Not Found error
        raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found.")
    
    # Update the course attributes
    course.name = course_data.name
    course.level = course_data.level
    
    # Commit the changes to the database
    db.commit()
    
    # Return the updated course data
    return course_data
```