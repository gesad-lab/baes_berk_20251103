```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import List, Optional
from src.database import get_db
from src.models import Course  # Assuming Course model is defined in src/models.py

router = APIRouter()

# Request and response models
class CourseBase(BaseModel):
    name: str = Field(..., description="The name of the course")
    level: str = Field(..., description="The level of the course")

class CourseResponse(CourseBase):
    id: int = Field(..., description="The auto-generated ID of the course")

@router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseBase, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/courses", response_model=List[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses
```