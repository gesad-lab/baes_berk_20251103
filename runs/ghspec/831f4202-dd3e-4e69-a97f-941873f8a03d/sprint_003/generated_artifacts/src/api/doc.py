```python
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, constr
from typing import List
from src.models import Course  # Assuming the Course model is defined properly
from src.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

class CourseCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)  # Ensures name is not empty
    level: constr(regex=r'^[A-Z][0-9]*$')  # Validates level format (e.g., A1, B2)

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

@router.post("/courses/", response_model=CourseResponse, status_code=201)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course with the specified name and level.
    
    - **course**: CourseCreate model containing course name and level
    - Returns a CourseResponse model with the created course details.
    """
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/courses/", response_model=List[CourseResponse])
async def get_courses(db: Session = Depends(get_db)):
    """
    Retrieve a list of all existing courses.
    
    - Returns a list of CourseResponse models including all courses.
    """
    courses = db.query(Course).all()
    return courses

@router.exception_handler(ValueError)
async def validation_exception_handler(request, exc: ValueError):
    """
    Handle validation errors and return a 400 Bad Request with a helpful message.
    """
    raise HTTPException(status_code=400, detail=str(exc))
```