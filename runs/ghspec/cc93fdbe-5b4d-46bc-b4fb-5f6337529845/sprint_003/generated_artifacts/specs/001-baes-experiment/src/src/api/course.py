```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from models import Course  # Assuming Course model exists in models.py
from database import get_db  # Assuming a dependency for session management

router = APIRouter()

class CourseCreate(BaseModel):
    name: str = Field(..., example="Mathematics", max_length=100)
    level: str = Field(..., example="Beginner", max_length=50)

@router.post("/courses", response_model=CourseCreate, status_code=201)
def create_course(course: CourseCreate, db: Session = next(get_db())):
    """
    Create a new course.

    Parameters:
    - course: CourseCreate - The course data containing name and level.

    Returns:
    - CourseCreate: The created course data.

    Raises:
    - HTTPException: If name or level is missing or already taken.
    """
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="E001: Both 'name' and 'level' are required.")

    # Check if course name already exists
    existing_course = db.query(Course).filter(Course.name == course.name).first()
    if existing_course:
        raise HTTPException(status_code=400, detail=f"E002: Course with name '{course.name}' already exists.")

    # Create and add new course to the database
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course
```