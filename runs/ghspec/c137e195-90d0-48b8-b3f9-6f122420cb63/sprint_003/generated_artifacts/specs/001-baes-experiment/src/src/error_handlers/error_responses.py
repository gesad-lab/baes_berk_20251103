```python
from fastapi import APIRouter, HTTPException
from typing import List
from models.course import Course
from database.db import SessionLocal
from pydantic import BaseModel

router = APIRouter()

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

@router.get("/courses", response_model=List[CourseResponse], status_code=200)
def get_courses():
    """
    Retrieve a list of all courses.

    Returns a JSON array with the details of each course, including
    the course ID, name, and level.
    """
    db = SessionLocal()
    try:
        # Fetch all courses from the database
        courses = db.query(Course).all()
    except Exception as e:
        # Log the exception (could implement a logging mechanism here)
        raise HTTPException(status_code=500, detail="Failed to retrieve courses")
    return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
```