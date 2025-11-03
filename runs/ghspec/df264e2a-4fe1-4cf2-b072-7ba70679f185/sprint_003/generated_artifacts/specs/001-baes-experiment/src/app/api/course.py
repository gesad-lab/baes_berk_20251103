```python
# app/api/course.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.models.course import Course  # Assuming Course model is defined in models
from app.database import SessionLocal  # Assuming a database session is defined
from sqlalchemy.orm import Session

router = APIRouter()

# Pydantic model for course input
class CourseCreate(BaseModel):
    name: str
    level: str

@router.post("/courses", response_model=Course)
def create_course(course: CourseCreate):
    """Create a new course with the provided name and level."""
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both name and level are required.")
    
    db: Session = SessionLocal()  # Get a new database session
    new_course = Course(name=course.name, level=course.level)
    
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@router.get("/courses/{id}", response_model=Course)
def get_course(id: int):
    """Retrieve the course details using course ID."""
    db: Session = SessionLocal()  # Get a new database session
    course = db.query(Course).filter(Course.id == id).first()
    
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    return course
```