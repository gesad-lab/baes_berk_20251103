```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Course  # Import the Course model
from src.schemas import CourseCreate, CourseResponse  # Import the Pydantic schemas

router = APIRouter()

@router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course.
    
    Args:
        course (CourseCreate): The course data to be created.
        db (Session, optional): Database session dependency.
        
    Returns:
        CourseResponse: The created course data with its ID.
        
    Raises:
        HTTPException: If the course creation fails.
    """
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/courses", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    """
    Retrieve a list of all courses.
    
    Args:
        db (Session, optional): Database session dependency.
        
    Returns:
        list[CourseResponse]: A list of all course records.
    """
    courses = db.query(Course).all()
    return courses
```