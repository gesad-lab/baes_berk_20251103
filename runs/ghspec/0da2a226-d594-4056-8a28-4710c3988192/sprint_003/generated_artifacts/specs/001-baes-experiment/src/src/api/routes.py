```python
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, constr
from models import Course
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

# Pydantic model for course creation
class CourseCreate(BaseModel):
    name: constr(min_length=1)  # Course name must be at least 1 character
    level: constr(min_length=1)  # Course level must be at least 1 character

@router.post("/courses", response_model=Course)
def create_course(course: CourseCreate, db: Session = next(get_db())):
    """
    Create a new course with provided name and level.
    
    Parameters:
        course (CourseCreate): Course details.
        db (Session): Database session from dependency injection.
    
    Returns:
        Course: The created course object.

    Raises:
        HTTPException: If level is missing or invalid.
    """
    try:
        if not course.level.isascii():  # Example validation for the level
            raise HTTPException(status_code=400, detail="Invalid level provided.")
        
        new_course = Course(name=course.name, level=course.level)
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
        return new_course
    except Exception as e:  # Catch any unexpected exceptions
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int, db: Session = next(get_db())):
    """
    Retrieve course information by its ID.
    
    Parameters:
        course_id (int): ID of the course to retrieve.
        db (Session): Database session from dependency injection.
    
    Returns:
        Course: The requested course object.

    Raises:
        HTTPException: If course not found.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course
```